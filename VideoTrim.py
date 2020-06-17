from os.path import join
from argsparse import argsParse
from TrimInfo import triminfo
from trimmer import Trimmer

def main():
    into, out, videopath_txt, timepath_txt, max_processes = argsParse()
    videopath_txt = join(into, videopath_txt)
    timepath_txt = join(into, timepath_txt)
    video_path = open(videopath_txt, "r").readlines()
    video_time = open(timepath_txt,"r").readlines()
    for path in video_path:
        infile,initial_time,terminal_time,outfile = triminfo(path, video_time)
        trimmer = Trimmer(into, out)
        trimmer.trim()
    
if __name__ == '__main__':
    main()
    
