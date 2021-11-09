class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        if n<=2:
            if n==1:
                return False
            if n==2:
                return True
        # 从前往后走， 每个数字记录能除以他的最大数字。
        #
        # 2 1  T
        # 3 1 1 F
        # 4 2 1 T
        # 5 4 F
        # 6 5 4 3 2 1  T
        # 7 6 F
        # 8 7 4 6 T
        # 9 8 6 F
        # 10 9 8 5 T
        div = [[0],[1]]
        for i in range(2, n+1):
            tmp = set()
            for j in range(i-1, 0,-1):
                if j == 1:
                    tmp.add(1)
                    break
                if i % j == 0 and j != 1:
                    tmp.add(j)
                    tmp.add(int(i/j))
                    for k in div[j]:
                        tmp.add(k)
                    for k in div[int(i/j)]:
                        tmp.add(k)
                    break
            div.append(list(tmp))

        dp = [False for _ in range(n+1)]
        dp[0] = False
        dp[1] = False
        dp[2] = True

        for i in range(3, n+1):
            for j in div[i]:
                if dp[i-j] == False:
                    dp[i] = True
        return dp[n]

        #dp[i] |= d[i - div[j]]

if __name__ == '__main__':
    print(Solution().divisorGame(4))