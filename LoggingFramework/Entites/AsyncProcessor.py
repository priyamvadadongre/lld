from concurrent.futures import ThreadPoolExecutor

class AsyncProcessor():

    def __init__(self):
        self.executer = ThreadPoolExecutor(max_workers=5)
    def process_async(self, func, *args, **kwargs):
        return self.executer.submit(func, *args, **kwargs)
    
    def shutdown(self):
        self.executer.shutdown(wait=True)
