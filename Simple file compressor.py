# %%
import PIL
from time import sleep
from PIL import Image
from tkinter.filedialog import *

print(' What would you like to compress?\n')
sel = int(input(' 1: PNG(no guarantee)\n 2: JPG\n 3: JPEG\n 4: GIF\n:'))

if sel == 1:
    path = askopenfilename()
    img = PIL.Image.open(path)

    myHeight, myWidth = img.size

    img = img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)
    save_path = asksaveasfilename()

    img.save(save_path+"-compressed.png")
    print('Compress succesfully!\n')
    sleep(3)
    exit()

if sel == 2:
    path = askopenfilename()
    img = PIL.Image.open(path)

    myHeight, myWidth = img.size

    img = img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)
    save_path = asksaveasfilename()

    img.save(save_path+"-compressed.jpg")
    print('Compress succesfully!\n')
    sleep(3)
    exit()

if sel == 3:
    path = askopenfilename()
    img = PIL.Image.open(path)

    myHeight, myWidth = img.size

    img = img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)
    save_path = asksaveasfilename()

    img.save(save_path+"-compressed.jpeg")
    print('Compress succesfully!\n')
    sleep(3)
    exit()

if sel == 4:
    path = askopenfilename()
    img = PIL.Image.open(path)

    myHeight, myWidth = img.size

    img = img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)
    save_path = asksaveasfilename()

    img.save(save_path+"-compressed.gif")
    print('Compress succesfully!\n')
    sleep(3)
    exit()
# %%
