#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 0015 19:11
# @Author  : jiaojianglong

class WXClient():

    def __init__(self,host,send_port,accept_port,sendmassage):
        self.host = host
        self.send_port = send_port
        self.accept_port = accept_port
        self.sendmassage = sendmassage

    def start_up(self):
        """
        启动微信客户端
        :return:
        """
        self.sendmassage.sendmsg("start up")

    def get_weixin_num(self):
        """
        获取微信号
        :return:
        """
        recData = self.sendmassage.sendmsg_getreturn("WeChat list")
        if recData.startswith("YXLB"):
            rec = recData.replace("YXLB‘", "")
            if len(rec) > 3:
                weixin_num_list = rec.split("—")
                weixin_list = []
                for weixin_num_str in weixin_num_list:
                    if weixin_num_str:
                        try:
                            weixin_dict = {}
                            weixin_message = weixin_num_str.split("‘")
                            weixin_dict['weixin_num'] = weixin_message[0]
                            weixin_dict['weixin_nickname'] = weixin_message[1]
                            weixin_dict['weixin_phone'] = weixin_message[2]
                            weixin_dict['weixin_wxid'] = weixin_message[3]
                            weixin_dict['weixin_id'] = weixin_message[4]
                            weixin_list.append(weixin_dict)
                        except:
                            pass
                return weixin_list
        return []