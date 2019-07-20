import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
import scipy.io as sio
import os
import sys
import cv2
import argparse
from models.VGGM import VGGM
import torch
import torchvision.transforms as transforms
import PIL.Image as Image
from torch.autograd import Variable
from models.triplet_loss_model import Tripletnet

parser = argparse.ArgumentParser(description='CMC')
parser.add_argument('--feature_layer', dest='feature_layer',
                    default=0, type=int)
parser.add_argument('--list_file', dest='list_file',
                    help='test list file',
                    default='', type=str)
parser.add_argument('--query_list_file', dest='query_list_file',
                    help='test list file',
                    default='', type=str)
parser.add_argument('--ext', dest='ext',
                    help='image file extension',
                    default='.jpg', type=str)
parser.add_argument('--image_dir', dest='image_dir',
                    help='image directory',
                    default='', type=str)
parser.add_argument('--repeat', dest='repeat',
                    help='repeat times, do not use in wild dataset',
                    default=1, type=int)
parser.add_argument('--maxg', dest='maxg',
                    help='max number of a class id in gallery',
                    default=1000, type=int)
parser.add_argument('--save', dest='save',
                    help='save to file',
                    default='', type=str)
parser.add_argument('--save_dir', dest='save_dir',
                    default='checkpoints/car_cyclegan_VGGM/', type=str)
parser.add_argument('--im_height', dest='im_height',
                    help = 'im_height',
                    default=224, type=int)
parser.add_argument('--im_width', dest='im_width',
                    help = 'im_width',
                    default=224, type=int)
args = parser.parse_args()


def load_query_reference(imagelist_file,query_file):
    gallery = {}
    probe = {}
    for line in open(imagelist_file).readlines():
        line = line.strip()
        t = line.split('/')
        if int(t[0]) not in gallery:
            gallery[int(t[0])] = []
        gallery[int(t[0])].append(line)
    for line in open(query_file).readlines():
        line = line.strip()
        t = line.split('/')
        if int(t[0]) not in probe:
            probe[int(t[0])] = []
        probe[int(t[0])].append(line)
    return gallery, probe

## Load network
net = VGGM()
tnet = Tripletnet(net)
tnet.cuda()
print("=> loading checkpoint '{}'".format(args.save_dir.strip()))
checkpoint = torch.load(args.save_dir.strip())
start_epoch = checkpoint['epoch']
tnet.load_state_dict(checkpoint['state_dict'])
print("=> loaded checkpoint '{}' (epoch {})"
        .format(args.save_dir.strip(), checkpoint['epoch']))

## transform
tnet.eval()
transform_list = []
transform_list += [transforms.Scale([args.im_width, args.im_height], Image.BICUBIC)]
transform_list += [transforms.ToTensor()]
transform_list += [transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])]
#transform_list += [transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))]
transformer = transforms.Compose(transform_list)

# analyze the top 50 rank score
ext = args.ext
length = 1024 
RANK_LIST = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]


average_rank_rate = np.zeros([len(RANK_LIST), ])
for r_id in xrange(args.repeat):  # repeat = 1
    gallery, probe = load_query_reference(args.list_file, args.query_list_file)
    if r_id==0:
        print 'Gallery size: %d' % (len(gallery.keys()))
    FEAT_SIZE = length
    g_n = 0
    p_n = 0
    for gid in gallery:
        g_n += len(gallery[gid])
    for pid in probe:
        p_n += len(probe[pid])
    print g_n,p_n
    g_feat = np.zeros([g_n, FEAT_SIZE], dtype=np.float32)
    g_ids = np.zeros([g_n, ], dtype=np.float32)
    k = 0
    # load all gallery set
    for gid in gallery.keys():
        for s in gallery[gid]:
            img = Image.open(os.path.join(args.image_dir.strip(), s + ext))
            im = transformer(img)
            im = torch.unsqueeze(im, 0)
            im = im.cuda()
            im = Variable(im)
            out = net(im)[0]
            g_feat[k] = torch.squeeze(out, 0).data.cpu().numpy()
            g_ids[k] = gid
            k += 1
    if r_id==0:
        print 'Gallery feature extraction finished'

    rank_rate = np.zeros([len(RANK_LIST), ])
    cnt = 0
    # for every probe image, calculate the score
    for pid in probe:
        for psample in probe[pid]:
            g_dist = np.zeros([g_n, ], dtype=np.float32)
            p_feat = np.zeros([FEAT_SIZE,], dtype=np.float32)
            img  = Image.open(os.path.join(args.image_dir.strip(), psample + ext))
            im = transformer(img)
            im = torch.unsqueeze(im, 0)
            im = im.cuda()
            im = Variable(im)
            out = net(im)[0]
            p_feat = torch.squeeze(out, 0).data.cpu().numpy()

            for i in xrange(g_n):
                g_dist[i] = np.linalg.norm(g_feat[i]-p_feat)
            g_sorted = [g_ids[i] for i in g_dist.argsort()]
            for k, r in enumerate(RANK_LIST):
                if pid in g_sorted[:r]:
                    rank_rate[k] += 1

            cnt += 1

    rank_rate /= cnt
    print '============================= ITERATION %d =============================' % (r_id+1)
    print RANK_LIST
    print rank_rate
    average_rank_rate += rank_rate
average_rank_rate /= args.repeat
print 'Average rank rate: '
print average_rank_rate
if args.save != '':
    with open(args.save, 'a') as fd:
        fd.write('%.6f\n' % average_rank_rate)
