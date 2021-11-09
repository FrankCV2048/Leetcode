class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n == 0:
            return 0
        dp = [0 for _ in range(n)]
        dp[0] = cost[0]
        dp[1] = min(cost[0], cost[1])
        for i in range(0, n):
            if i+2>=n and (i==0 or i==1):
                dp[i] = cost[i]
            else:
                dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[n-2], dp[n-1])

if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(Solution().minCostClimbingStairs(cost))