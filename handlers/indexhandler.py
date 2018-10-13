
import time
from handlers.basehandler import BaseHandler
from handlers.decorator import thread_pool_executor

class IndexHandler(BaseHandler):
    @thread_pool_executor
    def get(self, *args, **kwargs):
        time.sleep(3)
        return "睡了三秒，哈哈哈哈哈"
