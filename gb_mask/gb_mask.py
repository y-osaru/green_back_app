import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

if __name__ == '__main__':
  green_min = np.array([60/2,100,40])
  green_max = np.array([120/2,255,255])
  
  img = cv2.imread('input.png')
  img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
  
  mask_green = cv2.inRange(img_hsv,green_min,green_max)
  mask = cv2.bitwise_not(mask_green)
  mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)

  masked_img = cv2.bitwise_and(img, mask_rgb)
  masked_img_rgb = cv2.cvtColor(masked_img, cv2.COLOR_BGR2RGB)

  plt.imshow(mask_rgb)

  bgr = cv2.split(img)

  bgra = cv2.merge(bgr + [mask])
  cv2.imwrite("output.png",bgra)