"""
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ones-and-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findMaxForm(self, strs, m, n):
        Len = len(strs)
        # 记录下三维数组的写法，外层遍历必须用for _ in range()的方式申请内存，不能用[]*n浅拷贝的方式申请
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(Len + 1)]
        for k in range(1, Len + 1):
            cnt0 = strs[k - 1].count('0')
            cnt1 = strs[k - 1].count('1')
            for i in range(m + 1):
                for j in range(n + 1):
                    dp[k][i][j] = dp[k - 1][i][j]
                    if i - cnt0 >= 0 and j - cnt1 >= 0:
                        dp[k][i][j] = max(dp[k][i][j], dp[k - 1][i - cnt0][j - cnt1] + 1)

        return dp[Len][m][n]

if __name__ == '__main__':
    strs = ["001", "110","0000","0000"]
    m = 9
    n = 2
    print(Solution().findMaxForm(strs, m, n))



