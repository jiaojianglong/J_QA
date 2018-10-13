#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 22:11
# @Author  : jiaojianglong

from handlers.indexhandler import IndexHandler
handler = [
    (r"/", IndexHandler),
]
