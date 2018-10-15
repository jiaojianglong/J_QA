#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 0015 20:56
# @Author  : jiaojianglong

from weixin_bot.client.msg import Msg


class ConnectSuccessMassage(Msg):
    type_ = "connect_success"

    def handle(self):
        print("连接成功")