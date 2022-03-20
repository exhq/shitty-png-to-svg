#opening the image file
from PIL import Image as image
im = image.open('input.png')
pix = im.load()
#opening the text file
file1 = open("output.html","w+")
def fileprint(x):
    file1.write(x)

wid, hgt = im.size
#opening tag
fileprint(f"<svg width=\"{wid}\" height=\"{hgt}\"> \n")



for i in range(1 , wid):
    for b in range(1 ,hgt):
            fileprint(f"<rect width=\"1\" height=\"1\" x=\"{i}\" y=\"{b}\" style=\"fill:rgb{str(pix[i,b]) };\" />\n")
#closing tag
fileprint("</svg>")
print("done")
