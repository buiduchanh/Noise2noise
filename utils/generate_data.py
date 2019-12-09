from tensorflow.keras.preprocessing import image
import os
import cv2
from tqdm import tqdm
import shutil
# imgdir = '/Volumes/Work/Project/Research/Watermark/noise2noise/dataset/bds_2019'
# imgdes = '/Volumes/Work/Project/Research/Watermark/noise2noise/dataset/bds_2019_500'

# imgnames = os.listdir(imgdir)
# for imgname in tqdm(imgnames):

#     img_A = os.path.join(imgdir, imgname)
#     img_A = image.load_img(img_A, color_mode='rgb', target_size=(500, 500))
#     img_A = image.img_to_array(img_A).astype('float32')[:,:,::-1]

#     des_img = os.path.join(imgdes, imgname)
#     cv2.imwrite(des_img, img_A)

########################Move file
ROOT = '/Volumes/Work/Project/Research/Watermark/noise2noise/dataset'

cleandir = '/Volumes/Work/Project/Research/Watermark/noise2noise/dataset/500'
water_dir = '/Volumes/Work/Project/Research/Watermark/noise2noise/dataset/500_w'
mode  = None
imgnames = os.listdir(cleandir)
for idx , imgname in enumerate(imgnames):
    if imgname == '.DS_Store':
        continue
    print(imgname)
    if idx < int(0.8 * len(imgnames)):
        mode = 'train'
    else:
        mode = 'test'
    
    img_clean_path = os.path.join(cleandir, imgname)
    img_wterm_path = os.path.join(water_dir, imgname)

    des_clean_dir = os.path.join(ROOT, '{}/clean'.format(mode))
    des_water_dir = os.path.join(ROOT, '{}/noise'.format(mode))
    if not os.path.exists(des_clean_dir):
        os.makedirs(des_clean_dir)
    if not os.path.exists(des_water_dir):
        os.makedirs(des_water_dir)
    

    shutil.copy2(img_clean_path, des_clean_dir)
    shutil.copy2(img_wterm_path, des_water_dir)