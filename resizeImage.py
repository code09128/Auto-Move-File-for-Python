from PIL import Image
import matplotlib.pyplot as plt
import os

input_source_folder_path = './testSize'
output_source_folder_path = './testSize2'

width = 1500
height = 1500

def resizePhoto(input_source_folder_path):
    img_names_list = os.listdir(input_source_folder_path)
    print(img_names_list)

    for img_name in img_names_list:
        print(img_name)

        #開啟圖片
        im = Image.open(input_source_folder_path+"/"+img_name)
        print(im)

        #重新處理圖片解析度
        out = im.resize((width, height),Image.ANTIALIAS)
        out.save(output_source_folder_path+"/"+img_name)

        # plt.imshow(out)
        # plt.show()

