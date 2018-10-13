
from concurrent.futures import ThreadPoolExecutor


def thread_pool_executor(func):
    def wrapper(self,*args,**kwargs):
        def done_callback(obj):
            print(obj.result)
            self.write(obj.result)
        try:
            executor = ThreadPoolExecutor(max_workers=50)
            future = executor.submit(func,*args,**kwargs)
            future.add_done_callback(done_callback)
        except Exception as e:
            self.write({"code":500,"data":e.args})
    return wrapper
