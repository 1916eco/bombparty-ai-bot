from itertools import permutations
import enchant
import pyautogui
from PIL import Image
import time
import pytesseract
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


d=enchant.Dict("en_US")
op=set()

def word(name):
    print(name)
    lettr = [x.lower() for x in name]
    for n in range(5,len(name)):
        for y in list(permutations(lettr,n)):
            z="".join(y)
            if d.check(z):
                op.add(z)
    print(op)


# Press the green button in the gutter to run the script.
if name == 'main':
    while True:
        img = pyautogui.screenshot(region=(450, 550, 60, 40))
        img.save(r'Screenshot_1.png')
        savedImg = Image.open("Screenshot_1.png")
        something = pytesseract.image_to_string(savedImg)
        something = something.strip()
        something = something.lower()
        test = something +"a"
        word(test)
        time.sleep(1)
        op.clear()