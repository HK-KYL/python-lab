# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
from PIL import Image 
from PIL import ImageEnhance 

img = Image.open('images/flower.jpg')
imgCombined = ImageEnhance.Brightness(img.copy()).enhance(2.0)

for i in range(0,361,5):
    imgCombined = Image.blend(img.rotate(i), imgCombined.rotate(i+2.5), 0.5)

imgCombined.show()