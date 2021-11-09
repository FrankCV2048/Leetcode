'''
#########会员题目###########：

假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。

当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x 3 的矩阵来表示的。

例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1 号房子粉刷成绿色的花费，以此类推。请你计算出粉刷完所有房子最少的花费成本。

注意：

所有花费均为正整数。

示例：

输入: [[17,2,17],
      [16,16,5],
      [14,3,19]]
输出: 10
解释: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色。
最少花费: 2 + 5 + 3 = 10。

思路：dp[n][m] 为 第n个房子刷某个颜色的费用
状态转移： dp[n][m] = min(dp[n-1][!m]) + matrix[n][m]的费用
遍历dp[n]
时间复杂度：O(n^2)
空间复杂度：O(n^2)
'''


class Solution(object):
    def minCost(self, matrix):
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0

        dp = [[0]*m for _ in range(n)]
        for i in range(m):
            dp[0][i] = matrix[0][i]
        for i in range(1, n):
            for j in range(m):
                tmp = dp[i-1][:j] + dp[i-1][j+1:]
                dp[i][j] = min(tmp) + matrix[i][j]
        return min(dp[n-1])


if __name__ == '__main__':
    matrix = [[]]
    print(Solution().minCost(matrix))
