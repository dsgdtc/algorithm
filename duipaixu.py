# coding:utf-8
"""
堆排序
时间复杂度O（nlogn）
"""
import random
import time
import heapq


def time_decorator(func, **kwargs):
    def run_time(*args, **kwargs):
        start = time.time()
        # print 'start:', start
        func(*args, **kwargs)
        # return res
        stop = time.time()
        print 'run_time:', (stop - start)

    return run_time


@time_decorator
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)  #[0, 1, 2, 6, 3, 5, 4, 7, 8, 9]  #向堆中插入数据
    return [heapq.heappop(h) for i in range(len(h))]               #输出最大的数据


l = []
for i in range(1, 100000):
    l.append(random.randint(1, 100))
# print 'origin List:', l

heapsort(l)