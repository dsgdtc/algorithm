#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'guyu'

'''
输入一个整型数组,数组里有整数也有负数。
数组中一二或连续的多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)
'''

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if array == None or len(array) <= 0:
            return 0

        nCurSum = 0
        nGreatestSum = array[0]
        for i in range(len(array)):
            if nCurSum <= 0:
                nCurSum = array[i]
            else:
                nCurSum += array[i]

            if nCurSum > nGreatestSum:
                nGreatestSum = nCurSum

        return nGreatestSum
    # 动态规划解决问题
    def FindGreatestSumOfSubArray2(self, array):
        if array == None or len(array) <= 0:
            return 0
        aList = [0]*len(array)
        for i in range(len(array)):
            if i == 0 or aList[i-1] <= 0:
                aList[i] = array[i]
            else:
                aList[i] = aList[i-1] + array[i]
        return max(aList)

    def FindGreatestSumOfSubArray3(self,array):
        maxsofar = max_end_here = array[0]
        for x in array[1:]:
            max_end_here = max(x, max_end_here + x)
            maxsofar = max(maxsofar, max_end_here)
            raw_input()
            print x, max_end_here, maxsofar
        return maxsofar

alist = [1, -2, 3, -10, -4, 7, 2, -5]
s = Solution()
print alist
print(s.FindGreatestSumOfSubArray3(alist))