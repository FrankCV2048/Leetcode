class Solution:
    # 看到了 dp[i] 和 dp[i-1] 与 dp[n-i]的关系
    # 没想到累加求和 转换为 dp[n] 与 dp[n-1]的关系
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]





