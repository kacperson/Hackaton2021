import PIL
from PIL import Image

__pictureNumber = 0
imgName="ss"

def saveScreenshot(img):
    global __pictureNumber
    __pictureNumber = __pictureNumber+1
    img.save(imgName + str(__pictureNumber) + ".png", "png")
    return imgName + str(__pictureNumber) + ".png"