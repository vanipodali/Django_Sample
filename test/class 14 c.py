import datetime
import logging
logging.basicConfig(filename='class.log', level=logging.INFO)
class calculate_time:
    def __init__(self,original_func):
        self.original_func=original_func

    def __call__(self, *args, **kwargs):
        t1=datetime.datetime.now()
        res=self.original_func(*args,**kwargs)
        t2=datetime.datetime.now()
        print('It took {} to run {}'.format((t2-t1).total_seconds(),self.original_func.__name__))
        return res

@calculate_time
def print_nums():
    # t1=datetime.datetime.now()
    for i in range(1,100000):
        pass
    # t2=datetime.datetime.now()
    # print((t1-t2).total_seconds())

@calculate_time
def print_nums_dup():
    for i in range(1,2000000):
        pass

logging.INFO(print_nums())
logging.INFO(print_nums_dup())

