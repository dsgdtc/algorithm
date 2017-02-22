#coding:utf-8
"""
冒泡排序
时间复杂度O（n^2）
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
def bubbleSort(L):
    assert(type(L)==type(['']))
    length = len(L)
    if length==0 or length==1:
        return L
    for i in xrange(length):
        for j in xrange(length-1-i):
            if L[j] < L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
    return L


l=[]
for i in range(1,100000):
    l.append(random.randint(1,100))
# print 'origin List:', l

bubbleSort(l)