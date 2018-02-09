# testing the image libraries in python
# Maxim Sarandev || All Rights Reserved

from PIL import Image
import random
"""
# img1 = raw_input("First image URL: ")
file_name = "test.jpg"

# urllib.urlretrieve(img1, file_name)

im = Image.open(file_name)
pix = im.load()
# print pix[1,1]
first_image = []
second_image = []

# first img to array
for x in range(im.size[0]):
    for y in range(im.size[1]):
        first_image.append(pix[x,y])

print len(first_image)

# second img to array
file_name = "fbi.jpeg"
im = Image.open(file_name)
pix = im.load()

for x in range(im.size[0]):
    for y in range(im.size[1]):
        second_image.append(pix[x,y])

print len(second_image)
"""
# compare pixels
nm = Image.new("RGB",(250,250),0)
src_img = Image.open("test.jpg")
px_src = src_img.load()
pix = nm.load()

black = 0
white = 0
other = 0

for x in range(nm.size[0]):
    for y in range(nm.size[1]):
        if px_src[x,y] == (255,255,255):
            white += 1
            #pix[x, y] = (255,255,255)
        elif px_src[x,y] == (0,0,0):
            black += 1
            #pix[x, y] = (0,0,0)
        else:
            other += 1
            pix[x,y] = px_src[x,y]

print black, white, other
nm.show()
