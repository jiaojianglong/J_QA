#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 0014 11:49
# @Author  : jiaojianglong
import time
import threading
from setting import clients
from weixin_bot.connect_bot.tcp_client import TCPClient

CONNS = [TCPClient(clinet).connect() for clinet in clients]


def send_thread():
    while True:
        for i in range(60):
            for client in CONNS:
                if not client.sendmassage.sending:
                    client.sendmassage.send()
                    client.sendmassage.sending = True
            time.sleep(1)
            if i == 20:
                for client in CONNS:
                    try:
                        print("心跳")
                        client.sendmassage.sendmsg("lalala")
                        client.re_connect_num = 0
                    except:
                        if client.re_connect_num == 0:
                            client.reconnect()




threading.Thread(target=send_thread).start()

