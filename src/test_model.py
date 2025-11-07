"""Test script to visualize model predictions.

This script loads images and displays them with predictions.
"""

import matplotlib.pyplot as plt
from torchvision.io import read_image

# Load and display test images
image = read_image("archive/dataspeed/data/train/images/newonetwww (1).jpg")
mask = read_image("archive/dataspeed/data/train/images/newonetzwww (1).jpg")

plt.figure(figsize=(16, 8))
plt.subplot(121)
plt.title("Image")
plt.imshow(image.permute(1, 2, 0))
plt.subplot(122)
plt.title("Mask")
plt.imshow(mask.permute(1, 2, 0))
plt.show()
