'''
给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。

示例:

输入: 2
输出: 91
解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。
'''

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n+1):
            dp[i] = dp[i-1]*10 + \
                    (9*pow(10,i-2) - dp[i-1])*(i-1);

        return pow(10, n) - sum(dp)

    def countNumbersWithUniqueDigits1(self, n):
        if n == 0:
            return 1

        def pending_num(num):
            result = 1
            i = 1
            while i < num:
                result *= 10 - i
                i += 1
            return result

        l = [0] * 10
        l[1] = 10
        for i in range(2, n + 1):
            l[i] = l[i - 1] + 9 * pending_num(i)
        return l[n]



if __name__ == '__main__':
    n = 4
    print(Solution().countNumbersWithUniqueDigits(n))





