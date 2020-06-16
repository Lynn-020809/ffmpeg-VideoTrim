import re
import os
import subprocess

video_path = open("video_path.txt", "r").readlines()
video_time = open("time.txt","r").readlines()
os.system("cd /Users/linyutian/Desktop/video_cut")

for path in video_path:
    list_i=[]
    path = path.strip()
    time_name = re.findall("BV(.*?).mp4",path)
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
        initial = initial_time[i]
        terminal = terminal_time[i]
        outfile = str(i)+ path
        subprocess.run(f'/usr/local/bin/ffmpeg -i "{path}" -ss {initial} -to {terminal} -c copy -f mp4 -copyts "{outfile}"', shell=True)