#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 0014 14:47
# @Author  : jiaojianglong



import requests


appid = "14454239"
API_Key = "6uDrivVmqzyZGptXb73PrC2C"
Secret_Key = "xuUcScZGLm6jl6n5Ui2dlXokn1UgBs5f "

# token_url = "https://aip.baidubce.com/oauth/2.0/token"
# # token_data = {"grant_type":"client_credentials","client_id":API_Key,"client_secret":Secret_Key}
# # a = requests.post(token_url,json=token_data).text
# # print(a)
access_token = "24.7873a1896bf6a54f2461daeebb5068f2.2592000.1542286280.282335-14454239"

request_head = {"accept-encoding": "gzip, deflate",
                "x-bce-date":" 2015-03-24T13:02:00Z",
                "connection": "keep-alive",
                "accept": "*/*",
                "host": "aip.baidubce.com",
                "x-bce-request-id": "73c4e74c-3101-4a00-bf44-fe246959c05e",
                "content-type": "application/x-www-form-urlencoded",
                "authorization": "bce-auth-v1/46bd9968a6194b4bbdf0341f2286ccce/2015-03-24T13:02:00Z/1800/host;x-bce-date/994014d96b0eb26578e039fa053a4f9003425da4bfedf33f4790882fb4c54903"}











# f=open(r'767590a2b368899fdbe358e70b434380.png','rb') #二进制方式打开图文件
# print(f.read())
# # ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
# f1=open(r'767590a2b368899fdbe358e70b434380.jpg','rb')
# print(f1.read())
# f.close()
# f1.close()


# common_body = {"image":ls_f,"probability":"true"}
# res = requests.post(common_url,data=common_body)
# print(res)
# print(res.text)

import os
import re
import json
import urllib
import base64
from io import BytesIO
from PIL import Image
accurate_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
accurate_url = accurate_url+"?access_token="+access_token

general_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
general_url = general_url+"?access_token="+access_token

path = os.path.join(os.path.dirname(__file__).replace("/","\\"),"pictures")

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files

def get_text_from_picture():
    picture_name_list = file_name(path)
    picture_list = []
    for picture in picture_name_list:#"PNG、JPG、JPEG、BMP"
        if not (picture.endswith(".jpg") or picture.endswith(".png") or picture.endswith(".jpeg")):
            picture_name = picture.split(".")[0]
            im = Image.open(os.path.join(path, picture))
            im.save(os.path.join(path, "%s.png" % picture_name))
            picture = "%s.png" % picture_name

        f = open(os.path.join(path,picture),"rb")
        ls_f = base64.b64encode(f.read())
        f.close()
        common_body = {"image":ls_f,"probability":"true"}
        res = requests.post(general_url,data=common_body).text
        res = json.loads(res)
        words_result = res["words_result"]

        picture_list.append({"name":picture,"words_result":words_result})

    return picture_list


emoticon_url = "http://www.gaoxiaogif.com/qqbiaoqing/liaotian/gzxx/"
res = requests.get(emoticon_url).text
urls = re.findall(r"<span><img src=\"(?P<url>http://www\.gaoxiaogif.com/d/file/.*?)\" alt=",res)
print(urls)
print(len(urls))

# urllib.urlretrieve(urls[0], os.path.dirname(__file__).replace("/","\\")+"\1.jpg")
response = requests.get(urls[0])
print(response.content)
image = Image.open(BytesIO(response.content))
image.save('9.gif')

if __name__ == "__main__":
    pass
    # picture_list = get_text_from_picture()
    # print(picture_list)