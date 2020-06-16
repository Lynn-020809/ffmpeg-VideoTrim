import re
from collections import namedtuple

TrimInfo = namedtuple('TrimStruct','infile initial_time terminal_time outfile')


def triminfo(path,video_time):
    list_i=[]
    infile = path.strip()
    time_name = re.findall("BV(.*?).mp4",infile)
    pattern_i = re.compile(time_name[0]+':i:"(.*?)"')
    pattern_t = re.compile(time_name[0]+':t:"(.*?)"')
    for line in video_time:
        if(re.findall(pattern_i,line)!=[]):
            list_i = re.findall(pattern_i,line)
        if(re.findall(pattern_t,line)!=[]):
            list_t = re.findall(pattern_t,line)
    initial_time = list_i[0].split(',')
    terminal_time = list_t[0].split(',')
    length = len(initial_time)
    for i in range(length):
        outfile = str(i)+ path
    return TrimInfo(infile, initial_time, terminal_time, outfile)
