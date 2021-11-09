class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 二维数组
        # [10, 9, 2, 4, 5, 3, 7, 101, 18, 4, 13415, 20]
        n = len(nums)
        if n==0:
            return 0
        dp = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1

            else:
                for j in range(i-1, -1,-1):
                    if nums[j] < nums[i]:
                        dp[i] = max(dp[j]+1, dp[i])
        return max(dp)
if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]
    print(Solution().lengthOfLIS(nums))