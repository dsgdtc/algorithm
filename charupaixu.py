#coding:utf-8
"""
插入排序
时间复杂度O（n^2）
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
def insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j = j - 1
    # print 'after_sorted:', lists
    # return lists



l=[]
for i in range(1,1000):
    l.append(random.randint(1,100))
# print 'origin List:', l

insert_sort(l)