#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 0014 14:31
# @Author  : jiaojianglong

from weixin_bot.client.msg import Msg
from weixin_bot.tuling.tuling_replay import tuling_replay
from cache.emoticon import EmoticonCache
from models.mongodb.emoticon import EmoticonModel
class TextMassage(Msg):
    type_ = "text"
    emoticon = EmoticonCache()
    emoticonmodel = EmoticonModel()
    def handle(self):
        if self.text in self.emoticon.emoticons_name:
            emoticon_url = self.emoticonmodel.find_one(query_params={"content":self.text})["url"]
            file_name = emoticon_url.split("/")[-1]
            print(file_name)
            self.sendImage(file_name,emoticon_url)
        else:
            tuling_replay(dict(msg_type=0,
                            text=self.text,
                            user_id=self.msg.user_id,
                            group_id=self.msg.group_id,),self)





