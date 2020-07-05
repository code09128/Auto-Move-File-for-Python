import os
# 引入 pathlib 模組
from pathlib import Path
import shutil
from os.path import isfile, isdir, join
from os import walk

# 檔案或目錄路徑
# my_file = Path("\AI\openCV\isfile\ ")
my_file = Path("./newPhoto")

# 指定要列出所有檔案的目錄
mypath = r"D:\Dustin\AI\isFile\files"

# 檢查路徑是否存在
# if not my_file.exists():
#   os.makedirs(my_file)
#   shutil.move(r'D:\Dustin\AI\isFile\IMG-0679-00001.jpg', my_file)
#   print("路徑存在。")
# else:
#   shutil.move(r'D:\Dustin\AI\isFile\IMG-0679-00001.jpg', my_file)
#   print("路徑不存在。")

# 取得所有檔案與子目錄名稱
# files = os.listdir(mypath)

# 以迴圈處理
# for f in files:
#   # 產生檔案的絕對路徑
#   fullpath = join(mypath, f)
#   # 判斷 fullpath 是檔案還是目錄
#   if isfile(fullpath):
#     print("檔案：", f)
#   elif isdir(fullpath):
#     print("目錄：", f)


# 遞迴列出所有子目錄與檔案
# for root, dirs, files in walk(mypath):
#   print("路徑：", root)
#   print(" 目錄：", dirs)
#   print(" 檔案：", files)

# 遞迴列出所有子目錄與檔案
# for root, dirs, files in walk(mypath):
#   for f in files:
#     fullpath = join(root, f)
#     if isfile(fullpath):
#       print(fullpath)
#
#     else:
#       print("沒檔案")


allList = os.walk(mypath)
filesIMG = []
#列出所有子目錄與子目錄底下所有的檔案
for root, dirs, files in allList:
  # #列出目前讀取到的路徑
  # print("path：", root)
  # #列出在這個路徑下讀取到的資料夾(第一層讀完才會讀第二層)
  # print("directory：", dirs)
  #列出在這個路徑下讀取到的所有檔案
  print("file：", files)



