#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 0016 19:57
# @Author  : jiaojianglong
from models.connect.mongodb import MongoDB
from tools.md5lib import md5


class EmoticonModel(MongoDB):
    name = "j_qa.emoticon"
    column = ["id","content","url","thumburl","tags","replays","checked"]

    def __init__(self):
        super(EmoticonModel,self).__init__(self.name)


    def create(self, vals, *args, **kwargs):
        content = vals.get("content")
        url = vals.get("url")
        thumburl = vals.get("thumburl","")
        tags = vals.get("tags",[])
        replays = vals.get("replays",[])
        checked = vals.get("checked",False)
        id = md5(url)
        try:
            self.find_one(query_params={id:id})
            pass
        except:
            super(EmoticonModel,self).create(dict(id=id,content=content,url=url,thumburl=thumburl,tags=tags,replays=replays,checked=checked))

