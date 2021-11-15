"""
给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。

题目数据保证答案符合 32 位整数范围
"""


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            for j in range(n):
                if i - nums[j] >= 0:
                    dp[i] += dp[i - nums[j]]  #做重复了 干尼玛
        return dp[target]


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    print(Solution().combinationSum4(nums, target))
