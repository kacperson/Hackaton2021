import PIL
from PIL import Image

__pictureNumber = 0
imgName="ss"

def saveScreenshot(img):
    global __pictureNumber
    img.save(imgName + str(__pictureNumber) + ".png", "png")
    __pictureNumber = __pictureNumber+1
    