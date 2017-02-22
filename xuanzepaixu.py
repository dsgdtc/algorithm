#coding:utf-8
"""
选择排序
复杂度O(n^2)
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

def selection_sort(list2):
    for i in range(0, len (list2)):
        min = i
        for j in range(i + 1, len(list2)):
            if list2[j] < list2[min]:
                min = j
        list2[i], list2[min] = list2[min], list2[i]

l=[]
for i in range(1,100000):
    l.append(random.randint(1,100))
# print 'origin List :', l

selection_sort(l)
# print l