class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2
        dp[4] = 4
        for i in range(5, n + 1):
            for j in range(0, i+1):
                if i - j >= 0:
                    dp[i] = max(dp[i], dp[i - j] * dp[j], (i - j) * j)
        return dp[n]

if __name__ == '__main__':
    n = 10
    print(Solution().integerBreak(n))