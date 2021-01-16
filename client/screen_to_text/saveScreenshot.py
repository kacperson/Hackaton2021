import PIL
from PIL import Image

__pictureNumber =0
imgName="ss"

def saveScreenshot(img):
    img.save(imgName + str(__pictureNumber) + ".png", "png")
    __pictureNumber = __pictureNumber+1