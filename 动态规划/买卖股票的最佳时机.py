class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if  n == 0:
            return 0
        minPr = prices[0]
        maxPr = 0
        temp = 0
        for i in range(1, n):
            if minPr<=prices[i]:
                temp = prices[i] - minPr
            else:
                minPr = prices[i]
            maxPr = max(maxPr, temp)
        return maxPr

if __name__ == '__main__':
    print(Solution().maxProfit([7,6,4,3,1]))