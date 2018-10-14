#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/26
# @Author  : JiaoJianglong


import os
import re
import time
import datetime
import socket
import threading

import tornado.ioloop
import tornado.iostream

from tools.trans_byte_to_string import transformCodec
from weixin_bot.massage.accept_massage import AcceptMassage
from weixin_bot.massage.send_massage import SendMessage

#TCP连接客户端实例
#需每隔100秒发送一条消息，避免连接断开
class TCPClient(object):

    def __init__(self, client, io_loop=None):
        self.client = client
        self.host = self.client['host']
        self.accept_port = self.client['accept_port']
        self.send_port = self.client['send_port']
        if io_loop is None:
            self.io_loop = tornado.ioloop.IOLoop.current()
        else:
            self.io_loop = io_loop
        self.shutdown = False
        self.stream = None
        self.sock_fd = None
        self.EOF = b"\xcd\xea\xb3\xc9"
        self.re_connect_num = 0
        self.sendmassage = SendMessage(self.host,self.send_port)
    def get_stream(self):
        self.sock_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.stream = tornado.iostream.IOStream(self.sock_fd)
    #创建连接
    def connect(self):
        self.get_stream()
        self.stream.connect((self.host, self.accept_port), self.start)
        self.stream.set_close_callback(self.on_close)
        return self

    def reconnect(self):
        pass
        # if self.re_connect_num % 1000 == 0:
        #     if self.re_connect_num == 0:
        #         if not ClientConnectModel().get_count({"id": self.id}):
        #             send_email_lib.send_email_content(EMAILL_ACCEPT_ACCOUNT, "客户端连接断开,正在尝试重连",
        #                                               "客户端：%s\n客户端地址：%s\nsend_port:%s" % (
        #                                                 self.client['name'], self.host, self.send_port))
        #             obj = {
        #                 "id": self.id,
        #                 "host": self.host,
        #                 "accept_port": self.accept_port,
        #                 "send_port": self.send_port,
        #                 "name": self.client["name"]
        #             }
        #             ClientConnectModel().create(obj)
        # self.re_connect_num += 1
        # self.get_stream()
        # self.stream.connect((self.host, self.accept_port), self.restart)
        # self.stream.set_close_callback(self.on_close)

    def restart(self):
        pass
        # self.re_connect_num = 0
        # send_email_lib.send_email_content(
        #     EMAILL_ACCEPT_ACCOUNT, "重新连接成功", "客户端：%s\n客户端地址：%s\nsend_port:%s" %
        #                                      (self.client['name'], self.host, self.send_port))
        # ClientConnectModel().delete(query_params={"id": self.id})
        # self.accept_message()

    def start(self):
        self.accept_message()

    def accept_message(self):
        self.stream.read_until(self.EOF, self.on_receive)

    def on_receive(self, data):
        self.sendmassage.accept_time = time.time()
        t1 = threading.Thread(target=self.data_reply, kwargs={"data": data})
        t1.start()
        self.accept_message()

    def on_close(self):
        time.sleep(1)
        self.reconnect()

    def close(self):
        self.io_loop.close_fd(self.sock_fd)
        print("断开连接")
    #接收消息时调用
    def data_reply(self, **kwargs):
        data = kwargs.get("data")
        msg = transformCodec(data)
        msg = msg[:msg.find("完成")]
        print("%s--接收消息：" % datetime.datetime.now(), msg)
        AcceptMassage(msg,self).reply_massage()
