#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 0014 13:44
# @Author  : jiaojianglong

class Msg():
    type_ = ""

    def __init__(self,msg):
        self.client = msg.client
        self.sendmassage = self.client.sendmassage
        self.msg = msg
    #处理函数
    def handle(self):
        raise Exception("子类需复写此方法")

    #回复text类型消息
    def reply_text(self,text):
        print("发送消息",text)
        self.sendmassage.sendmsg("3|%s|%s|%s|0"%(self.msg.botid,self.msg.from_wxid,text))



