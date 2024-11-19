import os
import cv2

PATH = os.getcwd()

list_image = os.listdir(os.path.join(PATH,'multiresize')) #check file
print(list_image)

for img in list_image:
    image_path = os.path.join(PATH,'multiresize',img)
    img_resize = cv2.imread(image_path, cv2.IMREAD_COLOR)
    resized = cv2.resize(img_resize,(0,0),fx=0.5,fy=0.5)
    newfile = 'resized_' + img # resized_cat.jpg
    save_loc = os.path.join(PATH,'multiresize',newfile)
    cv2.imwrite(save_loc,resized)
