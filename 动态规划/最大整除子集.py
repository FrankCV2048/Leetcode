"""
给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
answer[i] % answer[j] == 0 ，或
answer[j] % answer[i] == 0
如果存在多个有效解子集，返回其中任何一个均可。
"""


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums = sorted(nums)
        if n == 0:
            return 0
        dp = [1] * n
        dp[0] = 1
        max_size = 1
        max_value = 1
        for i in range(1, n):
            for j in range(1, i + 1):
                if nums[i] % nums[i - j] == 0:
                    dp[i] = max(dp[i], dp[i - j] + 1)
                if dp[i] > max_size:
                    max_size = dp[i]
                    max_value = nums[i]
        if max_size == 1:
            return [nums[0]]
        ns = []
        i = max_size
        j = n - 1
        while i != 0:
            if max_value % nums[j] == 0 and dp[j] == i:
                max_value = nums[j]
                i -= 1
                ns.append(nums[j])
            j -= 1
        return ns

if __name__ == '__main__':
    nums = [1, 2, 4, 8]
    print(Solution().largestDivisibleSubset(nums))