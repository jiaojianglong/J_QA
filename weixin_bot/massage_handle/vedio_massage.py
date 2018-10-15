#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 0014 20:17
# @Author  : jiaojianglong
import re
from weixin_bot.massage.msg import Msg
from weixin_bot.tuling.tuling_replay import tuling_replay
class EmoticonMassage(Msg):
    type_ = "vedio"

    def handle(self):
        print("视屏消息")