"""
题目改过
如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

子数组 是数组中的一个按原顺序序列。
"""


class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #1 2 4 5 6 8
        n = len(nums)
        if n < 3:
            return 0
        dp = [[0]*(int(n/2)+1) for _ in range(n)]
        dp[1][nums[1]-nums[0]] = -1

        if (nums[0] - nums[1] == nums[1] -nums[2]):
            dp[2][nums[1] - nums[0]] = 1

        for i in range(2, n):
            for j in range(i-1, -1, -1):
                if (nums[i] - nums[j])>int(n/2):continue
                if dp[j][nums[i] - nums[j]] != 0 and dp[j][nums[i] - nums[j]] != -1:
                    dp[i][nums[i]-nums[j]] += (dp[j][nums[i]-nums[j]]+1)
                if dp[j][nums[i] - nums[j]] == -1:
                    dp[i][nums[i] - nums[j]] = 1
                if dp[j][nums[i] - nums[j]] == 0:
                    dp[i][nums[i] - nums[j]] = -1
        sum = 0
        for i in range(n):
            for j in range(len(dp[0])):
                if dp[i][j] != -1:
                    sum += dp[i][j]
        return sum

if __name__ == '__main__':
    nums = [1,2,3,4,5,6]
    print(Solution().numberOfArithmeticSlices(nums))

