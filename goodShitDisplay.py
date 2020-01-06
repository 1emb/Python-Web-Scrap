import pandas as pd
import xlrd
import cv2
import requests
import shutil


title = []
file = 'RedditContent.xlsx'
wb = xlrd.open_workbook('RedditContent.xlsx')
sheet = wb.sheet_by_index(0) 
for i in range(sheet.ncols):
    title.append(sheet.cell_value(0, i))

img_url = sheet.cell_value(1, 3)
res = requests.get(img_url, stream = True)
local_file = open('local_image.jpg', 'wb')
res.raw.decode_content = True
shutil.copyfileobj(res.raw, local_file)



    



