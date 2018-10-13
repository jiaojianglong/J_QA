#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 22:05
# @Author  : jiaojianglong


import time
import os
import tornado.web
import concurrent.futures



class BaseHandler(tornado.web.RequestHandler):
    ProcessThreadExecutor = {}
    process_executor = concurrent.futures.ProcessPoolExecutor()

    def future_process(self,func, fun):
        self.process_executor.submit(func, fun)

    def future_thread(self,func):
        def done_callback(result):
            print(result.result(), "线程")
            return result.result()

        print("分配进程：", os.getpid())
        if os.getpid() in self.ProcessThreadExecutor.keys():
            print("使用创建好的线程")
            thread_executor = self.ProcessThreadExecutor[os.getpid()]
        else:
            print("使用新创建线程")
            thread_executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
            self.ProcessThreadExecutor[os.getpid()] = thread_executor
        future = thread_executor.submit(func)
        future.add_done_callback(done_callback)
        time.sleep(0.01)

