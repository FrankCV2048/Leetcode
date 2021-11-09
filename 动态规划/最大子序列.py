class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        pre = nums[0]
        maxSum = nums[0]
        for i in range(1, n):
            pre = max(pre+nums[i], nums[i])
            maxSum = max(pre, maxSum)
        return maxSum

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    so = Solution()
    print(so.maxSubArray(nums))