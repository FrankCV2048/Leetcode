class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0
        dp = [[0] * m for _ in range(n)]
        if matrix[n - 1][m - 1] == '0':
            dp[n - 1][m - 1] = 0
        else:
            dp[n - 1][m - 1] = 1

        for i in range(0, m):
            if matrix[n - 1][i] == '0':
                dp[n - 1][i] = 0
            else:
                dp[n - 1][i] = 1

        for i in range(0, n):
            if matrix[i][m - 1] == '0':
                dp[i][m - 1] = 0
            else:
                dp[i][m - 1] = 1

        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                if matrix[i][j] == '1':
                        dp[i][j] = min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])+1
                else:
                    if matrix[i][j] == '0':
                        dp[i][j] = 0

        maxL = 0
        for i in range(n):
            for j in range(m):
                if dp[i][j] > maxL:
                    maxL = dp[i][j]
        return maxL

# 因为只和前三个元素有关所以可以使用滚动数组，求一个最大边长即可
if __name__ == '__main__':
    matrix = [["1", "1", "1", "1", "0"],
              ["1", "1", "1", "1", "0"],
              ["1", "1", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["0", "0", "1", "1", "1"]]
    print(Solution().maximalSquare(matrix))
