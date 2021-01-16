import PIL
from CompareImages import *
import pyautogui
from PIL import ImageGrab


imgsimilarity=0.90

print("hit enter on left up[ corner")
input()
lu=pyautogui.position()
print("hit enter on right down corner")
input()
rd=pyautogui.position()
print(lu+rd)

pyautogui.sleep(3)

newimg = ImageGrab.grab(lu+rd)
oldimg = ImageGrab.grab(lu+rd)
while True:
    pyautogui.sleep(3)

    oldimg=newimg
    newimg = ImageGrab.grab(lu + rd)
    if(compareImages()>imgsimilarity)
        pass


