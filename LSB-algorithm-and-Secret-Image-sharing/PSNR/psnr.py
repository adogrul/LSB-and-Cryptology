import cv2
import numpy as np

def psnr(image1, image2):
    image1 = image1.astype(np.float64)
    image2 = image2.astype(np.float64)
    mse = np.mean((image1 - image2) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr_value = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr_value


image1 = cv2.imread('LSB\\images\\1.jpg')
image2 = cv2.imread('LSB\\images\\stego_image.jpg')

psnr_value = psnr(image1, image2)
print("PSNR değeri:", psnr_value)
