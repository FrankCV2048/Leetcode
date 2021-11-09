class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxF = [0]*(n)
        minF= [0]*(n)
        maxF[0]=nums[0]
        minF[0]=nums[0]
        for i in range(1,n):
            maxF[i] = max(maxF[i - 1] * nums[i], max(nums[i], minF[i - 1] * nums[i]))
            minF[i] = min(minF[i - 1] * nums[i], min(nums[i], maxF[i - 1] * nums[i]))

        return max(maxF)

if __name__ == '__main__':
    pass