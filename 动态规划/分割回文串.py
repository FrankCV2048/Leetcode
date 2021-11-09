class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)

        ret = list()
        ans = list()

        def isPalindrome(i, j):
            if i >= j:
                return 1
            return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1

        def dfs(i):
            if i == n:
                ret.append(ans[:])
                return

            for j in range(i, n):
                if isPalindrome(i, j) == 1:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret

    def partition1(self, s):
        n = len(s)
        f = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        ret = list()
        ans = list()

        def dfs(i):
            if i == n:
                ret.append(ans[:])
                return

            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret

# 由于需要求出字符串 ss 的所有分割方案，因此我们考虑使用搜索 + 回溯的方法枚举所有可能的分割方法并进行判断。
#
# 假设我们当前搜索到字符串的第 ii 个字符，且 s[0..i-1]s[0..i−1] 位置的所有字符已经被分割成若干个回文串，并且分割结果被放入了答案数组 \textit{ans}ans 中，那么我们就需要枚举下一个回文串的右边界 jj，使得 s[i..j]s[i..j] 是一个回文串。
#
# 因此，我们可以从 ii 开始，从小到大依次枚举 jj。对于当前枚举的 jj 值，我们使用双指针的方法判断 s[i..j]s[i..j] 是否为回文串：如果 s[i..j]s[i..j] 是回文串，那么就将其加入答案数组 \textit{ans}ans 中，并以 j+1j+1 作为新的 ii 进行下一层搜索，并在未来的回溯时将 s[i..j]s[i..j] 从 \textit{ans}ans 中移除。
#
# 如果我们已经搜索完了字符串的最后一个字符，那么就找到了一种满足要求的分割方法。
#
# 细节
#
# 当我们在判断 s[i..j]s[i..j] 是否为回文串时，常规的方法是使用双指针分别指向 ii 和 jj，每次判断两个指针指向的字符是否相同，直到两个指针相遇。然而这种方法会产生重复计算，例如下面这个例子：
#
# 当 s=aaba 时，对于前 22 个字符 aa，我们有 2 种分割方法[aa] 和 [a, a][a,a]，当我们每一次搜索到字符串的第 i=2 个字符 b 时，都需要对于每个 s[i..j]s[i..j] 使用双指针判断其是否为回文串，这就产生了重复计算。
#
# 因此，我们可以将字符串 ss 的每个子串 s[i..j]s[i..j] 是否为回文串预处理出来，使用动态规划即可。设 f(i, j)f(i,j) 表示 s[i..j]s[i..j] 是否为回文串，那么有状态转移方程：
if __name__ == '__main__':
    s = 'abababab'
    print(Solution().partition1(s))