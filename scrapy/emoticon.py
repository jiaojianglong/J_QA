#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 0014 14:47
# @Author  : jiaojianglong




import os
import re
import json
import urllib
import time
import base64
import requests
import chardet
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
from models.mongodb.emoticon import EmoticonModel


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

class GaoXiaoGifCOM():
    root_url = "http://www.gaoxiaogif.com"
    save_path = "../static/emoticon/gaoxiao/"
    re_save_path = "../static/emoticon/gaoxiao_re/"
    emoticon_model = EmoticonModel()
    def get_fu_tags(self):
        fu_tags_url = "http://www.gaoxiaogif.com/weixinbiaoqing/"
        res = requests.get(fu_tags_url).text
        soup = BeautifulSoup(res)
        sul = soup.find_all("ul")[1].find_all("a")
        urls = []
        for url in sul:
            name = url.text.encode("latin1").decode("gbk").encode("utf8").decode("utf8")
            url = url.attrs['href']
            if not url.startswith("http://"):
                url = self.root_url + url
            urls.append({"url":url,"text":name,"tag":"fu"})
        print("父标签url:",urls)
        return urls
    def get_zi_tags(self):
        fu_tag_urls = self.get_fu_tags()
        for fu_url in fu_tag_urls:
            res = requests.get(fu_url["url"]).text
            soup = BeautifulSoup(res)
            sul = soup.find_all("ul")[1].find_all("a")
            urls = []
            with open("../static/emoticon/tag_url.txt", "a", encoding="utf8") as f:
                for url in sul:
                    name = url.text.encode("latin1").decode("gbk").encode("utf8").decode("utf8")
                    url = url.attrs['href']
                    if not url.startswith("http://"):
                        url = self.root_url + url
                    urls.append(dict(url=url,text=name,tag="zi"))
                    f.write("%s!!! %s!!! %s\n\n"%(fu_url['text'],name,url,))


    def del_duplication(self):
        fu_urls = self.get_fu_tags()
        urls = []
        urls_dict = []
        with open("../static/emoticon/tag_url.txt", "r", encoding="utf8") as f:
            res = f.read()
            tags = res.split("\n\n")
            for tag in tags:
                if tag:
                    fu_name = tag.split("!!! ")[0]
                    zi_name = tag.split("!!! ")[1]
                    url = tag.split("!!! ")[2]
                    if url in urls:
                        print(fu_name,zi_name,url)
                    else:
                        urls.append(url)
                        urls_dict.append(dict(fu_name=fu_name,zi_name=zi_name,url=url))
        for fu_url in fu_urls:
            if not fu_url['url'] in urls:
                urls.append(fu_url['url'])
                urls_dict.append(dict(fu_name=fu_url['text'],zi_name=fu_url['text'],url=fu_url['url']))
        print(len(urls_dict))
        with open("../static/emoticon/tag_url_duplication.txt","w",encoding="utf8") as ff:
            for url in urls_dict:
                ff.write("%s  %s  %s\n\n"%(url['fu_name'],url['zi_name'],url["url"]))
        return urls_dict

    def get_all_emoticons(self):
        with open("../static/emoticon/tag_url_duplication.txt","r",encoding="utf8") as f:
            url_dicts = f.read().split("\n\n")
            for url_dict in url_dicts:
                tag_name = url_dict.split("  ")[1]
                url = url_dict.split("  ")[2]
                self.get_emoticon(tag_name,url)
    def get_emoticon(self,tag,url):
        res = requests.get(url).text
        re_urls = re.findall(r"<span><img src=\"(?P<url>.*?)\"",res)
        for image_url in re_urls:
            try:
                file_name = image_url.split("/")[-1]
                print(file_name)
                response = requests.get(image_url)
                print(response.content)
                image = Image.open(BytesIO(response.content))
                try:
                    image.save(self.save_path+file_name)
                except OSError:
                    file_name = file_name.split(".")[0]+".gif"
                    image.save(self.save_path + file_name)

                EmoticonModel().create(dict(url=image_url,tags=[tag],file_name=file_name))

            except:
                print("*"*200)

    def get_text_from_picture(self,picture):
        if not (picture.endswith(".jpg") or picture.endswith(".png") or picture.endswith(".jpeg")):
            picture_name = picture.split(".")[0]
            im = Image.open(self.save_path + picture)
            im.save(self.save_path + picture_name + ".png")
            picture = picture_name + ".png"

        f = open(os.path.join(self.save_path, picture), "rb")
        ls_f = base64.b64encode(f.read())
        f.close()
        common_body = {"image": ls_f, "probability": "true"}
        try:
            res = requests.post(accurate_url, data=common_body).text
            res = json.loads(res)
            print(res)
            words_result = res["words_result"]
        except:
            time.sleep(2)
            res = requests.post(accurate_url, data=common_body).text
            res = json.loads(res)
            print(res)
            words_result = res["words_result"]
        words = ""
        for word_result in words_result:
            print(word_result)
            min = word_result["probability"]["min"]
            variance = word_result["probability"]['variance']
            if min >0.9 and variance<0.01:
                words+=word_result['words']
        return words

    def update_content(self):
        emoticons = EmoticonModel().coll.find()
        for emoticon in emoticons:
            file_name = emoticon['file_name']
            id = emoticon['id']
            words = self.get_text_from_picture(file_name)
            if words:
                print(words,id)
                try:
                    self.emoticon_model.update(dict(content=words),query_params={"id":id})
                except:
                    print("更新报错")
if __name__ == "__main__":
    GaoXiaoGifCOM().update_content()
    pass

    # picture_list = get_text_from_picture()
    # print(picture_list)
#"http://mmbiz.qpic.cn/mmemoticon/ajNVdqHZLLCmxPqI7fND1u5cSg7vHlreicSBlpT9wiaNhrOnUibsp3TVQCVHTa9Njg5/0"