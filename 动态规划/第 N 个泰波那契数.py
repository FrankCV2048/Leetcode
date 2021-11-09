class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        dp = [0, 1, 1]
        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2] + dp[i-3])
        return dp[n]

if __name__ == '__main__':
    print(Solution().tribonacci(25))