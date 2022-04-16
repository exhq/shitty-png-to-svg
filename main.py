#!/usr/bin/env python3
#opening the image file
import os
from PIL import Image as image
import random
import sys

if len(sys.argv) != 2:
    print("Please provide input image")
    exit(1)

im = image.open(sys.argv[1])
pix = im.load()
#opening the text file
file1 = open(os.path.join(sys.path[0], "output.txt"), "w+")
def fileprint(x):
    file1.write(x)

wid, hgt = im.size
#opening tag
fileprint(f"<svg width=\"{wid}\" height=\"{hgt}\"> \n")


for i in range(1 , wid):
    for b in range(1 ,hgt):
            fileprint(f"<rect width=\"1\" height=\"1\" x=\"{abs(i)}\" y=\"{abs(b)}\" style=\"fill:rgb{str(pix[i,b]) };\" />\n")
            
#closing tag
fileprint("</svg>")
os.rename(os.path.join(sys.path[0], "output.txt"),os.path.join(sys.path[0], "output.html")) 
print("done")
