

import concurrent.futures
import time
import os

ProcessThreadExecutor = {}

process_executor = concurrent.futures.ProcessPoolExecutor()

def future_process(func,fun):
    process_executor.submit(func,fun)


def future_thread(self):
    def done_callback(result):
        print(result.result(),"线程")
        return result.result()
    print("分配进程：",os.getpid())
    if os.getpid() in ProcessThreadExecutor.keys():
        print("使用创建好的线程")
        thread_executor = ProcessThreadExecutor[os.getpid()]
    else:
        print("使用新创建线程")
        thread_executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
        ProcessThreadExecutor[os.getpid()] = thread_executor
    future = thread_executor.submit(self.index)
    future.add_done_callback(done_callback)
    time.sleep(0.01)
