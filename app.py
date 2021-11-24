from PIL import Image

def average(l):
    try:
        res = round(sum(l)/len(l))
        return res
    except:
        pass
   

def sampleArea(pixels,x,y):
    rs = []
    gs = []
    bs = []
    samplingRange = 3
    for i in range(x-samplingRange,x+samplingRange+1):
        for j in range(x-samplingRange,x+samplingRange+1):
            try:
                pixel = pixels[x+i,y+j]
                rs.append(pixel[0])
                gs.append(pixel[1])
                bs.append(pixel[2])
            except:
                pass
    px = (average(rs), average(gs), average(bs))
    return px
    

img = Image.open("image.jpg")
pixels = img.load()
pixel = pixels[0,0]

newImg = img.copy()
newImgPixels = newImg.load()

for x in range(img.size[0]):
    for y in range(img.size[1]):
        try:
            newImgPixels[x,y] = sampleArea(pixels,x,y)
        except:
            pass
        
    

newImg.show()
