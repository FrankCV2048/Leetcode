class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            if i % 2 == 0:
                dp[i] = dp[int(i/2)]
            else:
                dp[i] = dp[int((i-1)/2)] + 1
        return dp

if __name__ == '__main__':
    print(Solution().countBits(8))
