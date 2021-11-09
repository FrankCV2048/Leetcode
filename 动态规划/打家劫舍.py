class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * n
        dp[0] = nums[0]
        if n<=2:
            return max(nums)
        dp[1] = max(nums[:2])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[n-1]

#一样 因为i只和i-1 和 i-2有关，可以做成流动数组，减少空间复杂度
if __name__ == '__main__':
    nums = [1,1,1,2]
    print(Solution().rob(nums))
