from os.path import join 
import subprocess


def trim(infile,initial_time,terminal_time,outfile):
    for i in range(len(initial_time)):
        initial = initial_time[i]
        terminal = terminal_time[i]
        subprocess.run(f'ffmpeg -i {infile} -ss {initial} -to {terminal} -c copy -f mp4 -copyts {outfile}')

class Trimmer:
    def __init__(self, into, out):
        self.into = into
        self.out = out
        
    def trim(self,infile,initial_time,terminal_time,outfile):
        infile = join(self.into, infile)
        outfile = join(self.out, outfile)
        trim(infile, initial_time,terminal_time,outfile)
