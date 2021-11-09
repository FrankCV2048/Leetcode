class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n <= 0:
            return 0

        dp = [0]*(n+1)
        dp[0] = cost[0]
        dp[1] = min(cost[0], cost[1])
        if n==3:
            return min(cost[0]+cost[2], cost[1])
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[n-1], dp[n-2])

if __name__ == '__main__':
    cost = [0,1,1,0]
    print(Solution().minCostClimbingStairs(cost))