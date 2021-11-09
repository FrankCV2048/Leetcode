class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                f[i] += f[i - 2]
        return f[n]



if __name__ == '__main__':
    s = "1201234"
    # 1 1 2
    # 1 12 1 + 1
    # 11 2

    # 1 1 2 3
    # 11 23   2 + 2
    # 1 1 23
    # 11 2 3
    # 1 12 3




    print(Solution().numDecodings(s))
