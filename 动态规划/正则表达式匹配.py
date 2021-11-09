class Solution(
        object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def match(index_s, index_p):
            if index_s == 0:
                return False
            if p[index_p-1] == '.':
                return True
            return s[index_s-1] == p[index_p-1]

        m = len(s)
        n = len(p)

        f = [[False]*(n+1) for _ in range(m+1)]
        f[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    f[i][j] |= f[i][j-2]
                    if match(i, j-1):
                        f[i][j] |= f[i-1][j]
                else:
                    if match(i, j):
                        f[i][j] |= f[i-1][j-1]
        return f[m][n]

if __name__ == '__main__':
    s = '###b'
    p = '###b*'
    o = Solution()
    print(o.isMatch(s, p))