#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 0014 14:47
# @Author  : jiaojianglong




import os
import re
import json
import urllib
import base64
import requests
from io import BytesIO
from PIL import Image


API_Key = "6uDrivVmqzyZGptXb73PrC2C"
Secret_Key = "xuUcScZGLm6jl6n5Ui2dlXokn1UgBs5f "
access_token = "24.7873a1896bf6a54f2461daeebb5068f2.2592000.1542286280.282335-14454239"

accurate_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
accurate_url = accurate_url+"?access_token="+access_token

general_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
general_url = general_url+"?access_token="+access_token

path = os.path.join(os.path.dirname(__file__).replace("/","\\"),"pictures")

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files

def get_text_from_picture(picture_path):
    if not (picture_path.endswith(".jpg") or picture_path.endswith(".png") or picture_path.endswith(".jpeg")):
        picture_name = picture_path.split(".")[0]
        im = Image.open(picture_path)
        im.save(picture_name+".png")
        picture = "%s.png" % picture_name

    f = open(os.path.join(path,picture),"rb")
    ls_f = base64.b64encode(f.read())
    f.close()
    common_body = {"image":ls_f,"probability":"true"}
    res = requests.post(general_url,data=common_body).text
    res = json.loads(res)
    words_result = res["words_result"]

    return{"name":picture,"words_result":words_result}





def get_picture_from_WX():

    emoticon_url = "http://www.gaoxiaogif.com/qqbiaoqing/liaotian/gzxx/"
    res = requests.get(emoticon_url).text
    urls = re.findall(r"<span><img src=\"(?P<url>http://www\.gaoxiaogif.com/d/file/.*?)\" alt=",res)
    print(urls)
    print(len(urls))

    response = requests.get(urls[0])
    print(response.content)
    image = Image.open(BytesIO(response.content))
    image.save('9.gif')

if __name__ == "__main__":
    pass
    # picture_list = get_text_from_picture()
    # print(picture_list)
#"http://mmbiz.qpic.cn/mmemoticon/ajNVdqHZLLCmxPqI7fND1u5cSg7vHlreicSBlpT9wiaNhrOnUibsp3TVQCVHTa9Njg5/0"