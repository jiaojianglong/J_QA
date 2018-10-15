#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 0015 19:12
# @Author  : jiaojianglong

from weixin_bot.client.wxbot import WXBot
class WxFriend():

    def __init__(self,wxbot,friend_id):
        if isinstance(wxbot,WXBot):
            self.wxbot = wxbot
        else:
            raise Exception("参数错误")
        self.friend_id = friend_id