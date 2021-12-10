"""
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
         最长公共子序列
        :param word1:
        :param word2:
        :return:
        """
        # sieya
        # iesait
        #

        n = len(word1)
        m = len(word2)
        dp = [[0]*m for _ in range(n)]
        if n == 0 or m == 0:
            return 0
        if word1[0] == word2[0]:
            dp[0][0] = 1
        if n > 1 and m > 1:
            if word1[0] == word2[1]:
                dp[0][1] = 1
            if word1[1] == word2[0]:
                dp[1][0] = 1

        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp

if __name__ == '__main__':
    word1 = "sea"
    word2 = "eat"
    print(Solution().minDistance(word1, word2))



