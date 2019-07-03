import cv2
import numpy as np
import io
from PIL import Image

def maskGreenBack(img):
  #リクエストをPIL→opencvへ変換(※rgb→bgrに変換を忘れたら青くなる)
  img_pil = Image.open(img)
  img_cv2 = np.asarray(np.array(img_pil))[:, :, ::-1].copy()
      
  #透過画像に変換
  green_min = np.array([60/2,100,40])
  green_max = np.array([120/2,255,255])

  img_hsv = cv2.cvtColor(img_cv2,cv2.COLOR_BGR2HSV)

  mask_green = cv2.inRange(img_hsv,green_min,green_max)
  mask = cv2.bitwise_not(mask_green)
  
  bgr = cv2.split(img_cv2)
  bgra = cv2.merge(bgr + [mask])
  #bgra→rgbaに変換
  rgba = cv2.cvtColor(bgra,cv2.COLOR_BGRA2RGBA)
      
  #再びopencv→PILへ
  mask_img_pil = Image.fromarray(rgba)

  return mask_img_pil