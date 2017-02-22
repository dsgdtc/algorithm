# coding:utf-8
"""
归并法
mytest里的代码要稍微简洁一些
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
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    # print 'result is:', result
    return result

def merge_sort(lists):

    if len(lists) <= 1:
        return lists
    middle = len(lists) / 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)

# if __name__ == '__main__':
#     a = [4, 7, 8, 3, 5, 9]
#     print merge_sort(a)


l = []
for i in range(1, 100000):
    l.append(random.randint(1, 100))
# print 'origin List :', l

merge_sort(l)
# print l