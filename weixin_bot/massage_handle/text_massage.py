#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 0014 14:31
# @Author  : jiaojianglong

from weixin_bot.client.msg import Msg
from weixin_bot.tuling.tuling_replay import tuling_replay

class TextMassage(Msg):
    type_ = "text"

    def handle(self):
        tuling_replay(dict(msg_type=0,
                           text=self.text,
                           user_id=self.msg.user_id,
                           group_id=self.msg.group_id,),self)





