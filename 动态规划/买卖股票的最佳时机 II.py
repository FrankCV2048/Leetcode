class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        if n == 1:
            return 0
        sp = [0]*n
        sp[0] = 0
        dp = [0]*n
        dp[0] = 0
        for i in range(1,n):
            if prices[i] >= prices[i-1]:
                sp[i] = sp[i-1]
            else:
                sp[i] = i
        for i in range(1, n):
            if sp[i] == sp[i-1]:
                dp[i] = dp[i-1] + prices[i]-prices[i-1]
            else:
                dp[i] = dp[sp[i]-1] + prices[i] - prices[sp[i]]
        return dp[n-1]
#累加所有上坡就可以了
if __name__ == '__main__':
    prices = prices =  [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))
