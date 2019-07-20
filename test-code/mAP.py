import os
import argparse
import sys
import numpy as np
import torch
import torchvision.transforms as transforms
import PIL.Image as Image
from torch.autograd import Variable

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

def Cal_mAP(net,f , repeat = 1, list_file = '',query_file = '', ext = '', save = 'mAP.txt', maxg=1000, FEAT_SIZE = 4096 ,image_dir= '',raw_scale = 255,im_height = 224, im_width = 224):
    mean_avg_prec = np.zeros([repeat, ])
    transform_list = []
    transform_list += [transforms.Scale([im_width, im_height], Image.BICUBIC)]
    transform_list += [transforms.ToTensor()]
    transform_list += [transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])]
    transformer = transforms.Compose(transform_list)
    if ext != '':
        ext = '.' + ext
    for r_id in xrange(repeat):
        gallery, probe = load_query_reference(list_file, query_file)
        if r_id == 0:
            print 'Gallery size: %d' % (len(gallery.keys()))
        g_n = 0
        p_n = 0
        for gid in gallery:
            g_n += len(gallery[gid])
        for pid in probe:
            p_n += len(probe[pid])
        g_feat = np.zeros([g_n, FEAT_SIZE], dtype=np.float32)
        g_ids = np.zeros([g_n, ], dtype=np.float32)
        k = 0
        # load gallery set
        for gid in gallery.keys():
            for s in gallery[gid]:
                img = Image.open(os.path.join(image_dir, s + ext))
                im = transformer(img)
                im = torch.unsqueeze(im, 0)
                im = im.cuda()
                im = Variable(im)
                out = net(im)[0]
                g_feat[k] = torch.squeeze(out, 0).data.cpu().numpy()
                g_ids[k] = gid
                #print gid, s
                k += 1
        if r_id == 0:
            print 'Gallery feature extraction finished'
        # for every probe image, calculate the AP
        for pid in probe:
            for psample in probe[pid]:
                #print pid, psample
                g_dist = np.zeros([g_n, ], dtype=np.float32)
                img  = Image.open(os.path.join(image_dir, psample + ext))
                im = transformer(img)
                im = torch.unsqueeze(im, 0)
                im = im.cuda()
                im = Variable(im)
                out = net(im)[0]
                p_feat = torch.squeeze(out, 0).data.cpu().numpy()
                for i in xrange(g_n):
                    g_dist[i] = np.linalg.norm(g_feat[i] - p_feat)
                g_sorted = np.array([g_ids[i] for i in g_dist.argsort()])
                n = np.sum(g_sorted == pid)
                hit_inds = np.where(g_sorted == pid)[0]
                map_ = 0
                for i, ind in enumerate(hit_inds):
                    map_ += (i + 1) * 1.0 / (ind + 1)
                map_ /= n
                mean_avg_prec[r_id] += map_
        mean_avg_prec[r_id] /= p_n
        print '============================= ITERATION %d =============================' % (r_id + 1)
        f.write('============================= ITERATION %{} ============================='.format(r_id + 1))
        print mean_avg_prec[r_id]
        f.write(str(mean_avg_prec[r_id]))
    print 'Average MAP:', np.mean(mean_avg_prec)
    f.write( 'Average MAP:{}'.format(np.mean(mean_avg_prec)))
    if save != '':
        with open(save, 'a') as fd:
            fd.write('%.6f\n' % np.mean(mean_avg_prec))
