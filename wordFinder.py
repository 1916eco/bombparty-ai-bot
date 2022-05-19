from itertools import permutations
import pyautogui
from PIL import Image
import time
import clipboard as cb
import pytesseract
import sys
from pytesseract import *
import keyboard
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
with open(r"wordlist.txt",
          encoding="utf8") as f:
    content = f.readlines()

found=[]

def word(name):
    found.clear()
    print(name)
    for i in content:
        if (i.find(name) != -1):
            found.append(i)
    if found:
        print(found)
        longest_string = max(found, key=len)
        cb.copy(longest_string)
        print("longest - " + longest_string)
def screenCheck(x):

    while True:
        img = pyautogui.screenshot(region=(x[0], x[1], 60, 40))
        img.save(r'Screenshot_1.png')
        savedImg = Image.open("Screenshot_1.png")
        something = pytesseract.image_to_string(savedImg)
        s = ''.join(filter(str.isalnum, something))
        something = s.lower()
        time.sleep(0.6)
        if something != "":
            found.clear()
            word(something)

while True:
    if keyboard.read_key() == "1":
        print("start")
        x = pyautogui.position()
        screenCheck(x)
        print(x[0])

