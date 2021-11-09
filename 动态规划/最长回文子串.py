class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        maxLen = 1
        begin = 0
        if n < 2:
            return s
        dp = [[False] * n for _ in range(len(s))]
        for i in range(n):
            dp[i][i] = True
        for L in range(2, n + 1):
            for i in range(n):
                j = L + i - 1
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > maxLen:
                    begin = i
                    maxLen = j - i + 1
        return s[begin:begin + maxLen]

if __name__ == '__main__':
    s = 'baaabababab'
    l = Solution()
    print(l.longestPalindrome(s))
