class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1 = len(s1)
        n2 = len(s2)
        n = len(s3)
        if n1+n2 != n:
            return False
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        dp[0][0] = True
        for i in range(n1+1):
            for j in range(n2+1):
                p = i+j-1
                if i>0:
                    dp[i][j] |= dp[i-1][j] and s1[i-1]==s3[p]
                if j>0:
                    dp[i][j] |= dp[i][j-1] and s2[j-1]==s3[p]
        if dp[n1][n2] == 0:
            return False
        return True

if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(Solution().isInterleave(s1,s2,s3))