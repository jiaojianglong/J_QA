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
        for client in CONNS:
            if not client.sendmassage.sending:
                client.sendmassage.send()
                client.sendmassage.sending = True
        time.sleep(1)

threading.Thread(target=send_thread).start()

