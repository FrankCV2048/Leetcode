class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for x in range(n + 1)]
        for i in range(1, n + 1):
            minnum, k = i, 1
            while i - k * k >= 0:
                minnum = min(dp[i - k * k], minnum)
                k += 1
            dp[i] = minnum + 1
        return dp[n]
