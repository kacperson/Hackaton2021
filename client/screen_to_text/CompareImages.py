from PIL import ImageChops
from PIL import Image


def compareImages(image1, image2):
    diff = ImageChops.difference(image1, image2)

    pixels = list(diff.getdata())
    fDiff=0
    for point in pixels:
        fDiff+=(point[0]+point[1]+point[2])/768
    fDiff= fDiff / len(pixels)

    return fDiff
