import operator
import random
import time
from functools import wraps, lru_cache


def calc(op_func,*args,**kwargs):
    items = list(args) + list(kwargs.values())
    result = 0
    for item in items:
        if type(item) in (int, float):
            result = op_func(result,item)
    return result


def add(x, y):
    return x + y

def sub(x, y):
    return x - y


def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'花费时间: {end_time - start_time:.2f}秒')
        return result
    return wrapper



@record_time
def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')

@record_time
def upload(filename):
    """上传文件"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')



@lru_cache
def fib1(n):
    if n in (1,2):
        return 1
    return fib1(n-1) + fib1(n-2)






if __name__ == '__main__':
    start_time = time.time()
    print(fib1(350))
    end_time = time.time()
    print(f'花费时间: {end_time - start_time:.2f}秒')
    # download('MySQL从删库到跑路.avi')
    # upload('Python从入门到住院.pdf')
    # download.__wrapped__('MySQL必知必会.pdf')
    # upload.__wrapped__('Python从新手到大师.pdf')
