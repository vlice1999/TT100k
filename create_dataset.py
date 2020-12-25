'''
用于创建图像识别数据集
'''

import os
import cv2
import json

with open("annotations.json") as f:
    json_data = json.load(f)

with open("types.json") as f:
    types = json.load(f)

# 裁剪图像
def cut_img(img_path, x0,x1,y0,y1):
    img = cv2.imread(img_path)
    cropped = img[int(y0):int(y1),int(x0):int(x1)]
    return cropped

index = 0
for img in json_data["imgs"]:
    img = json_data["imgs"][img]
    if len(img["objects"]) == 0:
        continue 
    for i,obj_img in enumerate(img["objects"]):
        Img = cut_img(img["path"],obj_img["bbox"]["xmin"],\
              obj_img["bbox"]["xmax"],obj_img["bbox"]["ymin"],\
              obj_img["bbox"]["ymax"])
        Img_path = "images/"+str(img["id"])+'_'+str(i)+'.jpg'
        if(Img.size == 0):
            continue 
        cv2.imwrite(Img_path,Img)
        with open("labels.txt","a+",encoding='utf-8') as f:
            f.write(Img_path+'\t'+str(types[obj_img["category"]])+\
                "\t"+obj_img["category"])
            f.write("\n")
        index += 1
print(index)
