#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 0014 20:17
# @Author  : jiaojianglong
from weixin_bot.client.msg import Msg


class NoticeMassage(Msg):
    type_ = "notice"

    def handle(self):
        print("通知消息")