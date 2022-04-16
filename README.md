# shitty-png-to-svg
so you know how the whole purpose of an svg is so you can scale it? i mean its literally in the name.  
yea, i fucked that up.  
this program takes a png file, and replaces every pixel with a 1 by 1 square, basically creating a pixel in a file format thats supposed to not have pixels.  
i know, very useful  
how to use:  

```bash
pip install pillow # setup, use pip install --user pillow, if you lack root permissions
./main.py <inputfile>
# hereafter you should find your generated svg in output.html in the current directory
```

### warning: in my experience, pictures bigger than 200pixels cause lag on your browser when its trying to render it. do that at your own risk. im not responsible if your shit catches on fire
