

# import the necessary packages
from __future__ import print_function
import numpy as np
import cv2
import string
import random
import os
from tqdm import tqdm
# load the image

def addWaterMark(name, image, text,opacity,BGRColor, x, y ):
    opacity= opacity/100
    overlay = image.copy()
    output = image.copy()
    
    cv2.putText(overlay, text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, BGRColor, 2)
    # apply the overlay
    cv2.addWeighted(overlay, opacity, output, 1 - opacity,
                    0, output)
    # show the output image
    cv2.imwrite('/Volumes/Work/Project/Research/Watermark/noise2noise/dataset/500_w/{}.jpg'.format(name), output)
if __name__ == '__main__':
    #put the text , Opacity, BGR Color
    imgdir = '/Volumes/Work/Project/Research/Watermark/noise2noise/dataset/500'
    imagenames = os.listdir(imgdir)
    for imgname in tqdm(imagenames):
        imgpath = os.path.join(imgdir, imgname)
        image = cv2.imread(imgpath)

        text = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase , k=random.randint(5,10)))
        h,w = image.shape[:2]
        y = random.randint(0, int(0.9 * h))
        x = random.randint(0, int(0.7 * w))
        opacity = random.randint(20,80)
        addWaterMark(imgname.split('.')[0], image, text,opacity,(255,255,255), x, y)