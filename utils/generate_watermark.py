from PIL import Image
import random
import os

def create_watermark(image_path, final_image_path, watermark):
    main = Image.open(image_path)
    mark = Image.open(watermark)
    
    #Brightness of mask
    Brightness = random.randint(50, 65)
    mask = mark.convert('L').point(lambda x: min(x, Brightness))
    mark.putalpha(mask)

    mark_width, mark_height = mark.size
    main_width, main_height = main.size
    aspect_ratio = mark_width / mark_height

    tmp_img = Image.new('RGB', main.size)

    x = tmp_img.size[0]
    y = tmp_img.size[1]
    # points = [[0,0],[0, 0.87*y],[0.8* x , 0],[0.8*x, 0.87* y], [0.4 *x  , 0.4 * y]]
    # for item in points:
    for idx in range(6):
        i = random.randint(0, x)
        j = random.randint(0, y)
        # i = int(item[0])
        # j = int(item[1])
        #size of watermark
        size = random.uniform(0.1, 0.3)
        new_mark_width = main_width * size
        mark.thumbnail((new_mark_width, new_mark_width / aspect_ratio), Image.ANTIALIAS)
        main.paste(mark, (i, j), mark)
        main.thumbnail((8000, 8000), Image.ANTIALIAS)
        main.save(final_image_path, quality=100)

if __name__ == '__main__':

    imgdir = '/Volumes/Work/Project/Research/Watermark/noise2noise/dataset/test/clean'
    imgdes = '/Volumes/Work/Project/Research/Watermark/noise2noise/dataset/test/tmp_noise'
    imgnames = os.listdir(imgdir)
    for imgname in imgnames:
        if imgname == '.DS_Store':
            continue
        print(imgname)
        imgpath = os.path.join(imgdir, imgname)
        imgdes_path = os.path.join(imgdes, imgname)

        create_watermark(imgpath,
                        imgdes_path,
                        '/Volumes/Work/Project/Research/Watermark/noise2noise/utils/bds_bi.png')

# import cv2
# import numpy as np
# img = '/Volumes/Work/Project/Research/Watermark/noise2noise/utils/bds.png'
# im_gray = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
# (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# # thresh = 127
# # im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
# bit_not = cv2.bitwise_not(im_bw)
# h,w  = bit_not.shape

# tmpimg = np.zeros((h,w,3))
# tmpimg[:,:,0] = bit_not
# tmpimg[:,:,1] = bit_not
# tmpimg[:,:,2] = bit_not

# cv2.imwrite('bds_bi.png', tmpimg)
