# shitty-png-to-svg
so you know how the whole purpose of an svg is so you can scale it? i mean its literally in the name.  
yea, i fucked that up.  
this program takes a png file, and replaces every pixel with a 1 by 1 square, basically creating a pixel in a file format thats supposed to not have pixels.  
i know, very useful  
how to use:  
youll need pillow (`pip install pillow` in terminal).  
in a folder, put an empty html file called "output.txt", put your png image and rename it to "input.png". run the py file, it should print "done" when its done, duh 
after the txt file is done, you can change the file extention to .html or .svg
### warning: in my experience, pictures bigger than 200pixels cause lag on your browser when its trying to render it. do that at your own risk. im not responsible if your shit catches on fire
