from PIL import Image
import pyautogui
from time import sleep
import sys
import pyocr
import pyocr.builders

sleep(5)
for i in range (100):
    img = pyautogui.screenshot(imageFilename="screenshot"+str(i)+".png",region=(537,502,265,30))

    tools = pyocr.get_available_tools()
    tool = tools[0]

    langs = tool.get_available_languages()
    lang = langs[0]
    txt = tool.image_to_string(
            Image.open('screenshot'+str(i)+'.png'),
            lang="eng",
            builder=pyocr.builders.TextBuilder(tesseract_layout=6)

    )
    Text = list(txt)
    count = len(Text)
    i = 0
    while True:
            if i >= count:
                break
            if Text[i] < 'a' or Text[i] > 'z':
                if Text[i] != '-':
                    del Text[i]
                    count -= 1
                else:
                        i +=1

            else:
                i += 1

    txt = str(''.join(Text))
    pyautogui.typewrite(txt, interval = 0.0)
