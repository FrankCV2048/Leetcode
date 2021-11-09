class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #剩余步长 到这位置的最大剩余步长+2
        n = len(nums)
        if n<=0:
            return 0
        dp = [0]*n
        dp[0] = nums[0]
        for i in range(1, n):
            if dp[i-1] == 0:
                dp[i] = 0
            else:
                dp[i] = max(dp[i-1]-1, nums[i])
        if dp[n-2] == 0:
            return False
        else:
            return True
if __name__ == '__main__':
    nums = [3,2,1,0,4,1,3]
    print(Solution().canJump(nums))