#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/18
# @Author  : JiaoJianglong
from models.mongodb.emoticon import EmoticonModel
class EmoticonCache():
    emoticonmodel = EmoticonModel()
    emoticons = []
    emoticons_name = []
    def create(self):
        emoticon_list = self.emoticonmodel.coll.find()
        for emoticon in emoticon_list:
            self.emoticons.append(emoticon)
            self.emoticons_name.append(emoticon['content'])


    def get(self,id):
        for emoticon in self.emoticons:
            if emoticon['id'] == id:
                return emoticon


EmoticonCache().create()