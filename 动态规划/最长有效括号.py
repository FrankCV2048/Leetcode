class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if len(s) < 2:
            return 0

        dp = [0 for _ in range(n)]
        for i in range(1,n):
            if s[i] == '(':
                dp[i] = 0
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2]+2
                if s[i-1] == ')' and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2
                    if i-dp[i-1]-2 >= 0:
                        dp[i] = dp[i] + dp[i-dp[i-1]-2]
        return max(dp)

if __name__ == '__main__':
    s = "(()))())("
    So = Solution()
    print(So.longestValidParentheses(s))