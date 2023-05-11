import cv2
import os
from tkinter import filedialog
import tkinter

os.chdir(os.path.dirname(__file__))

tkinter.Tk().withdraw()
image = str(filedialog.askopenfile())
image = image.split('name=\'')[1]
image = image.split('\' mode=\'r\'')[0]
print(image)
img = cv2.imread(image)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 
cv2.imwrite(image, img_gray)