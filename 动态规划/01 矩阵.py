"""
给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/01-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(mat)
        m = len(mat[0])
        maxlen = n
        if m > n:
            maxlen = m
        dp = [[maxlen]*m for _ in range(n)]
        if mat[0][0] == 0:
            dp[0][0] = 0
        else:
            dp[0][0] = 1
        if mat[n-1][n-1] == 0:
            dp[n-1][n-1] = 0
        else:
            dp[n-1][n-1] = 1


        for i in range(1,m):
            if mat[0][i] == 0:
                dp[0][i] = 0
            else:
                dp[0][i] = dp[0][i-1]+1
        for i in range(1,n):
            for j in range(1,m):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(mat[i][j], dp[i-1][j], dp[i][j-1])
        for k in range(n-2, -1, -1):
            for s in range(m-2,-1,-1):
                dp[k][s] = min(dp[k+1][s], mat[k][s], dp[k][s+1])

        return dp

if __name__ == '__main__':
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    print(Solution().updateMatrix(mat))
