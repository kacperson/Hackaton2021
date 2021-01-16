from PIL import ImageChops


def compareImages(image1 , image2):
    diff=ImageChops.difference(image1, image2)

    return