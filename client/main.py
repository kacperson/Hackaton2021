from  screen_to_text.CompareImages import *
import PIL
import pyautogui
import codecs
import sys
from voice_recorder.project2 import *
from PIL import Image
from PIL import ImageGrab
from screen_to_text.saveScreenshot import *
from screen_to_text.ImgToText import *

pictureNumber =0
imgName="ss"
nr_note = 0

global endflag
global newslaid
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
picture_with_screen = saveScreenshot(newimg)
nr_note = nr_note + 1
text_file = codecs.open("Output" + str(nr_note) + ".txt", "w", "UTF-8")
slide = ocr_core(picture_with_screen)
text_file.write(slide)
text_file.close()
thread1 = voiceRecordThred(1, "t1", 1)
thread1.start()

while True:
    pyautogui.sleep(1)
    if (keyboard.is_pressed('q')):
        print("exiting program")
        voiceRecordThred.endflag = True
        break
    oldimg=newimg
    newimg = ImageGrab.grab(lu + rd)
    print(compareImages(oldimg, newimg))
    if compareImages(oldimg, newimg)>imgsimilarity:
        voiceRecordThred.newslaid=True;
        picture_with_screen = saveScreenshot(newimg)
        nr_note = nr_note + 1
        text_file = codecs.open("Output" + str(nr_note) + ".txt", "w", "UTF-8")
        slide = ocr_core(picture_with_screen)
        print(type(slide))
        text_file.write(slide)
        text_file.close()
        #nowa notatka
    if(keyboard.is_pressed('q')):
        print("exiting program")
        voiceRecordThred.endflag=True
        break
