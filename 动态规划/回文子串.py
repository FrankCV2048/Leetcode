"""
给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。

回文字符串 是正着读和倒过来读一样的字符串。

子字符串 是字符串中的由连续字符组成的一个序列。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindromic-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sasdfa
        n = len(s)
        if n == 1:
            return 1
        dp = [[False] * n for _ in range(n)]
        if s[0] == s[1]:
            dp[0][1] = True

        for i in range(n):
            dp[i][i] = True
        for i in range(2, n):
            for j in range(i-1, -1, -1):
                if j == i-1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                    continue
                if s[i] == s[j]:
                    dp[i][j] = dp[i-1][j+1]
                else:
                    dp[i][j] = False
        sum = 0
        for i in range(n):
            for j in range(n):
               if dp[i][j]:
                    sum+=1
        return sum

if __name__ == '__main__':
    s = "hello"
    print(Solution().countSubstrings(s))