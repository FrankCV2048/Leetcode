class Solution(object):
    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[n-1]
        pass
#可以变为空间为O(1)
if __name__ == '__main__':
    nums = [2,1,4,5,3,1,1,3]
    print(Solution().massage(nums))