# coding:utf-8
"""
归并法
O(nlogn)
"""
import random
import time


def time_decorator(func, **kwargs):
    def run_time(*args, **kwargs):
        start = time.time()
        # print 'start:', start
        func(*args, **kwargs)
        stop = time.time()
        print 'run_time:', (stop - start)

    return run_time


# @time_decorator

def merge(left, right):
    result = []
    # raw_input()
    # print "merge list:",left,right
    while 0 < len(left) and 0 < len(right):
        if left[0] <= right[0]:
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])
            del right[0]

    # print left,right
    result.extend(left)
    result.extend(right)

    # print 'result is:', result
    return result

def merge_sort(lists):

    if len(lists) <= 1:
        return lists
    middle = len(lists) / 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


l = []
for i in range(1, 100000):
    l.append(random.randint(1, 100))
# print 'origin List :', l

@time_decorator
def call_merge_sort(l):
    return merge_sort(l)
# print l
call_merge_sort(l)