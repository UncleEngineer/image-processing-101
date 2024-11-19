import os
import cv2

PATH = os.getcwd()

img_path = os.path.join(PATH,'img','cat.jpg')
img_cat = cv2.imread(img_path, cv2.IMREAD_COLOR)
# print(img_cat.shape)
# print(img_path)

# resized = cv2.resize(img_cat,(400,200))
# resized = cv2.resize(img_cat,(0,0),fx=0.5,fy=0.5)

cropped = img_cat[77:319,143:412]

save_loc = os.path.join(PATH,'img','cat-cropped.jpg')
cv2.imwrite(save_loc,cropped)

# cv2.imshow('image',cropped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()