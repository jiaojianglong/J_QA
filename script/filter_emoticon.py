#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/19
# @Author  : JiaoJianglong

import time
from cache.emoticon import EmoticonCache
from login import SendMessage
from setting import clients
emoticons = EmoticonCache().emoticons
emoticon_name = EmoticonCache().emoticons_name
send_client = SendMessage(clients[0]['host'],clients[0]['send_port'])
bot_id = "2708"
user_id = "wxid_lkjy3t6spc4u22"
def filter_emoticon():
    for emoticon in emoticons:
        url = emoticon['url']
        id = emoticon['id']
        print(id,url)
        filename = url.split("/")[-1]
        print("发送图片：",filename)
        send_client.sendmsg("12|%s|%s|1|%s|%s" % (bot_id, user_id, filename, url))
        time.sleep(1)


if __name__ =="__main__":
    filter_emoticon()
