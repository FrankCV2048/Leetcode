class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 回溯 剪枝 动态
        n = len(s)

        f = [False] * (n+1)
        f[0] = True
        for i in range(1,n+1):
            # 回溯 剪枝 动态  [a a a a a]
            for j in range(0, i):
                f[i] |= f[j] and (s[j:i] in wordDict)
                if f[i]:
                    break
        return f[n]

if __name__ == '__main__':
    s = "leetcode"

    wordDict = ["leet","code"]
    print(Solution().wordBreak(s, wordDict))
