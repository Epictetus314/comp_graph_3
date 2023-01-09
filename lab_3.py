from math import radians, cos, sin #import the trigonometric functions we need
from PIL import Image, ImageDraw # ImageDraw module provides simple 2D graphics
dot = 480
inscr = Image.new('RGBA', (960, 960), (255, 255, 255)) # a new image is created 960x960
fig = ImageDraw.Draw(inscr) #an object is created from this image
ang = radians(10*(4+1)) #envelopes

with open('DS4.txt') as file: # open the file
    for line in file: #Using loop the file is divided into lines
        coordArray = list(map(int, line.split())) #using the split() method a pair of coordinates is formed from each line 
        x = cos(ang)*(coordArray[1]-dot)-sin(ang)*(coordArray[00]-dot)
        y = sin(ang)*(coordArray[1]-dot)+cos(ang)*(coordArray[0]-dot)
        #according to the new coordinates
        fig.line((x+480, y+480, x+481, y+481), fill=(0, 190, 255))

#derivation of the result
inscr.show()
inscr.save('DS4_result.png', "PNG")