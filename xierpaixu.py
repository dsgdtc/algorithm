#coding:utf-8
"""
希尔排序

"""
import random
import time

def time_decorator(func,**kwargs):
    def run_time(*args,**kwargs):
        start=time.time()
        # print 'start:', start
        func(*args,**kwargs)
        stop=time.time()
        print 'run_time:',(stop-start)
    return run_time

@time_decorator
def shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    group = count / step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k = k - group
                j = j + group
        group = group // step
    # print 'after_sorted:', lists
    return lists


l=[]
for i in range(1,1000):
    l.append(random.randint(1,100))
# print 'origin List :', l

shell_sort(l)