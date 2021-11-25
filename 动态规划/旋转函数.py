"""
给定一个长度为 n 的整数数组。

假设Bk数组顺时针旋转 k 个位置后的数组，我们定义的“旋转函数”为：

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]。

计算F(0), F(1), ..., F(n-1)中的最大值。

注意:
可以认为 n 的值小于 105。
"""

class Solution:
    def maxRotateFunction(self, nums):
        f = 0
        length = len(nums)
        for i in range(length):
            f += i*nums[i]
        maxf = f
        ss = sum(nums)
        for i in range(length-1,-1,-1):
            f = f - (length-1)*nums[i] + ss - nums[i]
            maxf = max(f,maxf)
        return maxf
