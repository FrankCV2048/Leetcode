class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m != 0:
            n = len(obstacleGrid[0])
        else:
            return 0
        if n == 0:
            return 0
        dp = [[0]*n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(1, n):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i-1]
            else:
                dp[0][i] = 0
        for i in range(1, m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0

        return dp[m-1][n-1]
if __name__ == '__main__':
    obstacleGrid = obstacleGrid = [[0,1],[0,0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))


