#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 0016 19:57
# @Author  : jiaojianglong
from models.connect.mongodb import MongoDB
from tools.md5lib import md5


class EmoticonModel(MongoDB):
    name = "j_qa.emoticon"
    column = ["id","content","url","thumburl","tags","replays","checked","file_name"]

    def __init__(self):
        super(EmoticonModel,self).__init__(self.name)


    def create(self, vals, *args, **kwargs):
        content = vals.get("content","")
        url = vals.get("url")
        thumburl = vals.get("thumburl","")
        tags = vals.get("tags",[])
        file_name = vals.get("file_name","")
        replays = vals.get("replays",[])
        checked = vals.get("checked",False)
        id = md5(url)
        if not self.get_count({"id":id}):
            super(EmoticonModel,self).create(dict(id=id,content=content,url=url,
                                                  thumburl=thumburl,tags=tags,
                                                  replays=replays,checked=checked,
                                                  file_name=file_name))

