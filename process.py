from PIL import Image

img = Image.open('qvp-short-logo.png')
imga = img.convert("RGBA")
datas = imga.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append((255, 255, 255, 255))

img.putdata(newData)
img.save("qvp-short-logo-processed.png", "PNG")
