class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #因为首尾相连接了，那么就分为[1:n-1] , [2:n]
        n = len(nums)
        if n<=2:
            return max(nums)
        dp1 = [0] * (n - 1)
        dp2 = [0] * (n - 1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[:2])
        dp2[0] = nums[1]
        dp2[1] = max(nums[1:3])
        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
        for i in range(3, n):
            dp2[i-1] = max(dp2[i-2], dp2[i-3]+nums[i])
        return max(dp1[n-2], dp2[n-2])

if __name__ == '__main__':
    nums = [1,2,3,1]
    print(Solution().rob(nums))


