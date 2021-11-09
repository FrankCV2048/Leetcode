class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==0 or n==0:
            return 0
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for j in range(m):
            dp[j][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

if __name__ == '__main__':
    #也可以优化，因为i,j 只和前两个状态有关所以可以将O(n)改为O(1)，其中前两次遍历也可以放到第三个遍历中加限制即可
    m = 3
    n = 3
    print(Solution().uniquePaths(m, n))