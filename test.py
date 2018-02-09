from PIL import Image

nm = Image.new("RGB",(1920,1080),(255,255,255))
px_new = nm.load()

# first source
src_img = Image.open("img1-1.jpg")
px_src = src_img.load()

# second source
second_img = Image.open("img2-2.jpg")
px_sec = second_img.load()

for x in range(src_img.size[0]):
    for y in range(src_img.size[1]):
        if px_sec[x,y][0] - 50 < px_src[x,y][0] < px_sec[x,y][0] + 50:
            px_new[x,y] = px_src[x,y]
        else:
            px_new[x, y] = (0,0,0)

        if px_sec[x,y][1] - 50 < px_src[x,y][1] < px_sec[x,y][1] + 50:
            px_new[x, y] = px_src[x, y]
        else:
            px_new[x,y] = (0,0,0)

        if px_sec[x, y][2] - 50 < px_src[x, y][2] < px_sec[x, y][2] + 50:
            px_new[x, y] = px_src[x, y]
        else:
            px_new[x,y] = (0,0,0)


src_img.show()
nm.show()