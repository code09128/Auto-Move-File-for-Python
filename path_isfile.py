import os
# 引入 pathlib 模組
from pathlib import Path
import shutil
from datetime import datetime

from keras.preprocessing import image
from PIL import Image
import numpy as np

# 檔案或目錄路徑
my_file = Path("\AI\openCV\isfile\ " + datetime.now().strftime("%Y%m%d_%H%M%S"))
# 要檢查的檔案路徑
filepath = r"D:\AI\openCV\isfile\origin\N250 (190).jpg"

filetest = r"D:\AI\openCV\isfile\origin\\"

# 檢查路徑是否存在
if my_file.exists():
  print("路徑存在。")
else:
  print("路徑不存在。")

# 檢查路徑是否存在
if not my_file.exists():
  os.makedirs(my_file)
  # shutil.move(r'D:\AI\openCV\isfile\N250 (6).jpg', my_file)
  print("路徑存在。")
else:
  # shutil.move(r'D:\AI\openCV\isfile\N250 (6).jpg', my_file)
  print("路徑不存在。")

# # 檢查路徑是否為檔案
# if my_file.is_file():
#   print("路徑是檔案。")
# else:
#   print("路徑不是檔案。")
#
# # 檢查路徑是否為目錄
# if my_file.is_dir():
#   print("路徑是目錄。")
# else:
#   print("路徑不是目錄。")
#
# # 檢查路徑檔案是否存在
# if os.path.isfile(filepath):
#   print("檔案存在。")
# else:
#   print("檔案不存在。")
#
# if os.listdir(filetest):
#   print("有檔案。")
#   shutil.rmtree(filetest)
#   print("資料夾檔案整個刪除")
# else:
#   print("沒檔案。")
#=======================================================================
trainPath = r"D:\Dustin\AI\imageData\test\\"

images = []
labels = []
pixel = 100

imgs_train = os.listdir(trainPath)  # 列出訓練資料檔案夾內所有檔案名稱

firstImage = Image.open(trainPath + imgs_train[0])  # 開啟第一張圖片
# pixel = firstImage.size[0]  # 照片尺寸大小

# 訓練集
for fileName in imgs_train:
    img_path = trainPath + fileName  # 完整路徑名稱
    img = image.load_img(img_path, grayscale=False, target_size=(pixel, pixel))
    img_array = image.img_to_array(img)  # 將圖片轉成陣列
    images.append(img_array)  # 放入list

    # label = int(fileName.split('.')[0])#從檔名切出標籤
    label = fileName[0]
    print(label)
    # if label == "N":
    if label == "N":
       label = 0
       print(label)
    else:
       label = 1
       print(label)

    labels.append(label)  # 放到list

traindata = np.array(images)  # 將整個list變成陣列
trainlabels = np.array(labels)  # 將整個list變成陣列

print("訓練資料集data:", traindata.shape)
print("訓練資料集label:", trainlabels.shape)

images.clear()  # 清空list,以便複用
labels.clear()  # 清空list,以便複用
