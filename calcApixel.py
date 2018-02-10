# Calculates the weight of a colour in an image
# Created by Maxim Sarandev, All rights reserved

from PIL import Image, ImageDraw

# first source
src_img = Image.open("img2.jpg")
px_src = src_img.load()

# new image
nm = Image.new("RGB",(src_img.size[0],src_img.size[1]),(0,0,0))
px_new = nm.load()

ca = 0
c = 0

# values store
pixels = {}

# already drawn values
drawn = {}

draw = ImageDraw.Draw(nm)

q_size = 1
# get the pixel values
for x in range(src_img.size[0]):
    for y in range(src_img.size[1]):
        # for cols..rows..
        if px_src[x,y] not in pixels:
            # the colour is new, add
            pixels[px_src[x,y]] = 1
        elif px_src[x,y] in pixels:
            # the colour exists, add weight
            pixels[px_src[x,y]] += 1

            q_size = pixels[px_src[x,y]]

            # draw all
            if px_src[x,y] not in drawn:
                draw.rectangle([(c, ca), (c, ca + src_img.size[0])], px_src[x,y])

                drawn[px_src[x,y]] = 1

                c += 1

nm.show()
"""
Fairly dangerous, crashes Excel

f = open("imageData.csv", 'a')
for x in pixels:
    f.write(str(pixels.get(x))+"\r\n")
f.close()
"""
