#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 0014 14:31
# @Author  : jiaojianglong

import json
import requests

from weixin_bot.massage.msg import Msg
from tools.md5lib import md5


class TextMassage(Msg):
    type_ = "text"

    def handle(self):




        body = {
            "reqType":0,
            "perception": {
                "inputText": {
                    "text": self.msg.text
                },
            },
            "userInfo": {
                "apiKey": "476fba18fe1d41a7bf652ff37a9c5295",
                "userId": md5(self.msg.from_wxid)
            }
        }
        res = requests.post("http://openapi.tuling123.com/openapi/api/v2",json=body).text
        res = json.loads(res)
        results = res["results"]
        for result in results:
            if result["resultType"] == "text":
                self.reply_text(result["values"]['text'])
            elif result['resultType'] == "url":
                self.reply_text(result["values"]['url'])
            elif result['resultType'] == "voice":
                pass
            elif result['resultType'] == "video":
                pass
            elif result['resultType'] == "image":
                pass
            elif result['resultType'] == "news":
                pass




