import os, sys
import random
import shutil
from PIL import Image

def random_copyfile(srcPath, dstPath):
    #檢查資料夾下子資料夾檔案
    for root, dirs, files in os.walk(srcPath):
        #查看各資料夾數量
        filesCount = len(files)
        print("filesCount:", filesCount)

        #資料夾數量大於兩張做移動處理
        if filesCount >= 1:
            temp = [] #儲存資料夾檔案陣列
            for file_name in files:
                temp.append(file_name)

            #隨機取檔案數量
            randomfile = random.sample(temp,1)
            print(randomfile)

            for name in randomfile:
                #shutil.copyfile(root+"/"+name, dstPath +"/"+ name) #複製搬移檔案
                shutil.move(root+"/"+name, dstPath +"/"+ name) #移動搬移檔案

if __name__  == '__main__':
    srcPath = './/sort1311N' #來源資料夾
    dstPath = './/train1311N' #丟的目的地資料夾

    if not os.path.isdir(dstPath):
        os.mkdir(dstPath)
        random_copyfile(srcPath, dstPath)