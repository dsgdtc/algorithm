# coding:utf-8
"""
快速排序
O(nlogn)
"""
import random
import time
import sys
sys.setrecursionlimit(1000000)


def time_decorator(func, **kwargs):
    def run_time(*args, **kwargs):
        start = time.time()
        # print 'start:', start
        func(*args, **kwargs)
        stop = time.time()
        print 'run_time:', (stop - start)

    return run_time


#@time_decorator
def quickSortPython(l):

#l[0]作为随机选择的数
    # assert (type(l) == type(['']))
    length = len(l)
    if length <= 1:
        return l
    left = [i for i in l[1:] if i > l[0]]
    right = [i for i in l[1:] if i <= l[0]]
    return quickSortPython(left) + [l[0], ] + quickSortPython(right)


l = []
for i in range(1, 100000):
    l.append(random.randint(1, 100))
# print 'origin List :', l

@time_decorator
def call_quicksort(l):
    return quickSortPython(l)
# print quickSortPython(l)
# print l

call_quicksort(l)