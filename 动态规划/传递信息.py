class Solution(object):
    def numWays(self, n, relation, k):
        """
        :type n: int
        :type relation: List[List[int]]
        :type k: int
        :rtype: int
        """
        # dp[2] = 0 - 2, 1 - 2
        # dp[3] = 0 - 3, dp[2]
        # dp[4][k] = dp[3][k - 1] + dp[2][k - 1] + dp[1][k - 1]
        # dp[3][k - 1] = dp[2][k - 1]
        if n <= 0 or len(relation) <= 0 or k <= 0:
            return 0
        dp = [[0]*(k+1) for _ in range(n+1)]
        for i in range(len(relation)):
            if relation[0] == 0:
                dp[relation[1]][1] = 1
        dp[0][0] = 1
        for i in range(k):
            for m in range(len(relation)):
                dp[relation[m][1]][i+1] += dp[relation[m][0]][i]
        return dp[n-1][k]

if __name__ == '__main__':
    n = 5
    relation = [[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]]
    k = 3
    print(Solution().numWays(n, relation, k))