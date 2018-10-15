#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 0015 20:28
# @Author  : jiaojianglong

from weixin_bot.client.wxgroup import WXGroup

class WXMember():

    def __init__(self,wxgroup,member_id):
        if isinstance(wxgroup,WXGroup):
            self.wxgroup = wxgroup
        else:
            raise Exception("参数错误")
        self.member_id = member_id