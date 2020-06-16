import argparse
from collections import namedtuple


def argsParse():
    SourceInfo = namedtuple('TrimInfo', 'into out videopath_txt timepath_txt max_processes')
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i','--into', default = '/Users/linyutian/Desktop/video_cut', 
                           help= 'figure out where to find your input video')
    argparser.add_argument('-o','--out',default = '/Users/linyutian/OneDrive - Singapore University of Technology and Design/edited_bilibili',
                           help= 'figure out where to output your edited videos')
    argparser.add_argument('-v','--videopath_txt', default = 'video_path.txt',
                           help= 'figure out where to get your ffmpeg params')
    argparser.add_argument('-t','--timepath_txt', default='time.txt',
                           help= 'figure out where to get timeInfo')
    argparser.add_argument('-m','--max_processes',default= 3, 
                            help= 'figure out the maximum process number')
    args = argparser.parse_args()
    return SourceInfo(args.into, args.out, args.videopath_txt, args.timepath_txt, args.max_processes)