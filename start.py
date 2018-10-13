#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 21:56
# @Author  : jiaojianglong


import tornado.ioloop
import tornado.web
from urls import handler
import tornado.httpserver

application = tornado.web.Application(handler,debug = False)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.bind(8888)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()