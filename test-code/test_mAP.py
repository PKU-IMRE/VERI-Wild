import os
import argparse
import torch.optim as optim
import numpy as np
import sys
from data.car_dataset import CarDataset
import torch.utils.data
from models.VGGM import VGGM
import  models.resnet as resnet
import  models.vgg as vgg
from models.triplet_loss_model import Tripletnet
from torch.autograd import Variable
import shutil
import mAP
from torch.optim import lr_scheduler
import time
parser = argparse.ArgumentParser(description= 'Train a TripletModel')
parser.add_argument('--test_list_file', dest='test_list_file',
                    help = 'test_list_file',
                    default='', type=str)
parser.add_argument('--query_list_file', dest='query_list_file',
                    help = 'query_list_file',
                    default='', type=str)
parser.add_argument('--test_ext', dest='test_ext',
                    help = 'test image file ext',
                    default='', type=str)
parser.add_argument('--image_dir', dest='image_dir',
                    help = 'image directory',
                    default='', type=str)
parser.add_argument('--scale', dest='scale',
                    help = 'image input scale',
                    default=255.0, type=float)
parser.add_argument('--feat_size', dest='feat_size',
                    help = 'feat_size',
                    default=1024, type=int)
parser.add_argument('--batch_size', dest='batch_size',
                    help = 'batch_size',
                    default=9, type=int)
parser.add_argument('--ID_net', type=str, default='VGGM',
                    dest='ID_net', help='ID_net')
parser.add_argument('--im_width', dest='im_width',
                    help = 'im_width',
                    default=224, type=int)
parser.add_argument('--im_height', dest='im_height',
                    help = 'im_height',
                    default=224, type=int)
parser.add_argument('--resume', default='', type=str,
                    help='path to latest checkpoint (default: none)')

parser.add_argument('--log_name', default="log.txt", type=str,
                    help='name for log')

best_acc = 0

def main():
    global args, best_acc
    args = parser.parse_args()


    f = file(args.log_name,"a+")
    f.truncate()
    
    if(args.ID_net == 'VGGM'):
        model = VGGM()
    else:
        model = resnet.resnet50(pretrained=False)
    tnet = Tripletnet(model)
    tnet.cuda()

    # resume from a checkpoint
    if args.resume:
        if os.path.isfile(args.resume):
            print("=> loading checkpoint '{}'".format(args.resume))
            checkpoint = torch.load(args.resume)
            args.start_epoch = checkpoint['epoch']
            tnet.load_state_dict(checkpoint['state_dict'])
            print("=> loaded checkpoint '{}' (epoch {})"
                    .format(args.resume, checkpoint['epoch']))
        else:
            print("=> no checkpoint found at '{}'".format(args.resume))

    n_parameters = sum([p.data.nelement() for p in tnet.parameters()])
    print(tnet)
    print('  + Number of params: {}'.format(n_parameters))
    tnet.eval() 
    mAP.Cal_mAP(model,f,list_file = args.test_list_file, query_file = args.query_list_file, ext = args.test_ext,image_dir=args.image_dir,im_height=args.im_height,im_width= args.im_width,FEAT_SIZE = args.feat_size)
    f.close()


if __name__ == '__main__':
    main()





