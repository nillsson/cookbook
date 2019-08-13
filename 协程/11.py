import time, re
import os, datetime
from concurrent import futures

data = ['MIMI', 'YIYI', 'lloyd']

def wait_on(argument):
    print(argument)
    time.sleep(2)
    return "OK!"

ex = futures.ThreadPoolExecutor(max_workers = 2)
for i in ex.map(wait_on, data):
    print(i)