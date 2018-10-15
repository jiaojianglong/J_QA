#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 0014 13:44
# @Author  : jiaojianglong
from weixin_bot.client.wxbot import WXBot
from weixin_bot.client.wxgroup import WXGroup
from weixin_bot.client.wxfrinend import WxFriend
from weixin_bot.client.wxmember import WXMember
class Msg():
    type_ = ""

    def __init__(self,msg):
        self.msg = msg
        self.wxclient = msg.client.client
        if self.type_ == "connect_success":
            return
        self.text = msg.text
        self.wxbot = WXBot(self.wxclient,msg.botid)
        if msg.is_group:
            self.wxgroup = WXGroup(self.wxbot,msg.group_id)
            self.wxmember = WXMember(self.wxgroup,msg.member)
        else:
            self.wxfriend = WxFriend(self.wxbot,msg.from_wxid)

    #处理函数
    def handle(self):
        raise Exception("子类需复写此方法")

    #回复text类型消息
    def reply_text(self,text):
        print("发送消息",text)
        self.wxclient.sendmassage.sendmsg("3|%s|%s|%s|0"%(self.msg.botid,self.msg.from_wxid,text))

    def sendImage(self,filename, fileurl):
        self.wxclient.sendmassage.sendmsg("12|%s|%s|1|%s|%s" % (self.msg.botid, self.msg.from_wxid, filename, fileurl))

    def sendFile(self,filename, fileurl):
        self.wxclient.sendmassage.sendmsg("12|%s|%s|2|%s|%s" % (self.msg.botid, self.msg.from_wxid, filename, fileurl))

