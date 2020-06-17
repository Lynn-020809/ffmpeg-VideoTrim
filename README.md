# VideoTrim --FFMPEG

    This is a python package used to achieve an automatic and simple video trim by ffmpeg.
    To use this one, you need provide the filename of your video, the initial time and terminal time of the part you want to trim.
    Also, you can set up some default parameters such as file_path of the input file and the output file. 

### Usage:

    Since it takes too much time to use Pr for simple but large amounts of video trims, this package uses the ffmpeg package to help batch video editing.

### Version: 

    ### Simple version: It is a simple one which can not accept some specific parameters like the path of the infiles and outfiles.
                        That means the infiles and outfiles will all be searched in the folder which package can be found.
    ### Advanced version: It can deal with some specific parameters submitted by the user, you can deal with the path of all kinds of files you need flexibly. 

### Guidance for the simple one:
   
    You need to prepare two txt files which is put in the same folder as the package.
    Also, you need to put all the videos you want edit in the same folder.
    The first file named video_path should include all the names of the videos you want to trim.
    Also, one file's name one line! 
    
    For the second file:
    ### DEMO:
    video_id(like 111myy...):i:01:20,02:30,...(all the initial times)
    video_id(like 111myy...):t:01:28,02:40,...(all the terminal times)
    
    //Pay attention the initial time should match the terminal time, please input according to the order.
    
    *please modify the simple_version files according to your needs which means you need to input the correct file_path instead of just running the provided file.
    
### Guidance for the advanced one:

  #### Specific parameters:   
  
    -i (--into)               //help= 'figure out where to find your input video'
    -o (--out)                //help= 'figure out where to output your edited videos'
    -v (--videopath_txt)      //help= 'figure out where to get your ffmpeg params'
    -t (--timepath_txt)       //help= 'figure out where to get timeInfo'
    
    * Note: If you want to fork the package, please remember to modify the default value to set up the default paths.
    
  #### Input Demo:     [Click here to review](#Guidance for the simple one)
  
    You need to prepare two files just like the guidance of the simple one.
    All the instructions are the same as the simple version.

    Moreover, if you want to operate the specific params, just key in the params and the value you want to set.
    
    
    
