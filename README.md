# Noise2Noise

This is an unofficial and partial Keras implementation of "Noise2Noise: Learning Image Restoration without Clean Data" [1].


Updates:
- [Sep. 21, 2018] Random-valued impulse noise model and L0 loss were added
- [Aug. 25, 2018] UNet model can be used in training
- [Aug. 25, 2018] Add trained weights

## Dependencies
- Keras >= 2.1.2, TensorFlow, NumPy, OpenCV

## Train Noise2Noise

### Download Dataset

Using VOC dataset for training
Any dataset can be used in training and validation instead of the above dataset.

### Train Model
Please see `python3 train.py -h` for optional arguments.

#### Train with Gaussian noise

[1] J. Lehtinen, J. Munkberg, J. Hasselgren, S. Laine, T. Karras, M. Aittala, 
T. Aila, "Noise2Noise: Learning Image Restoration without Clean Data," in Proc. of ICML, 2018.

[2] J. Kim, J. K. Lee, and K. M. Lee, "Accurate Image Super-Resolution Using Very Deep Convolutional Networks," in Proc. of CVPR, 2016.

[3] X.-J. Mao, C. Shen, and Y.-B. Yang, "Image
Restoration Using Convolutional Auto-Encoders with
Symmetric Skip Connections," in Proc. of NIPS, 2016.

[4] C. Ledig, et al., "Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network," in Proc. of CVPR, 2017.

[5] O. Ronneberger, P. Fischer, and T. Brox, "U-Net: Convolutional Networks for Biomedical Image Segmentation," in MICCAI, 2015.
