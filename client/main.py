from screen_to_text.CompareImages import *
import PIL
import pyautogui
import codecs
import sys
from PIL import Image
from PIL import ImageGrab
from screen_to_text.saveScreenshot import *
from screen_to_text.ImgToText import *

pictureNumber =0
imgName="ss"

imgsimilarity=0.03

print("hit enter on left upper corner")
input()
lu=pyautogui.position()
print("hit enter on right bottom corner")
input()
rd=pyautogui.position()
print(lu+rd)

newimg = ImageGrab.grab(lu+rd)
oldimg = ImageGrab.grab(lu+rd)

while True:
    pyautogui.sleep(1)

    oldimg=newimg
    newimg = ImageGrab.grab(lu + rd)
    print(compareImages(oldimg, newimg))
    if compareImages(oldimg, newimg)>imgsimilarity:
        dir = saveScreenshot(newimg)
        print("saved")
        text_file = codecs.open("Output" + str(pictureNumber) + ".txt", "w", "UTF-8")
        text_file.write(ocr_core(dir))
        text_file.close()
        #nowa notatka


