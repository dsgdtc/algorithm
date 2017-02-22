#coding:utf-8
"""
用内建函数sort排序
"""
import random
import time

def time_decorator(func,**kwargs):
    def run_time(*args,**kwargs):
        start=time.time()
        # print 'start:', start
        func(*args,**kwargs)
        # return res
        stop=time.time()
        print 'run_time:',(stop-start)
    return run_time

@time_decorator
def buildin_sort(lists):
    # 插入排序
    sorted(lists)



l=[]
for i in range(1,100000):
    l.append(random.randint(1,100))
# print 'origin List:', l

buildin_sort(l)