import os
import cv2
import math
import matplotlib.pyplot as plt
import numpy as np

"""
fotograflari al
plakalar nerde?
"""

data= os.listdir("veriseti")

for d in data:
    img = cv2.imread("veriseti/"+d)
    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.show() 
