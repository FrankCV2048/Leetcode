"""
最初记事本上只有一个字符 'A' 。你每次可以对这个记事本进行两种操作：

Copy All（复制全部）：复制这个记事本中的所有字符（不允许仅复制部分字符）。
Paste（粘贴）：粘贴 上一次 复制的字符。
给你一个数字 n ，你需要使用最少的操作次数，在记事本上输出 恰好 n 个 'A' 。返回能够打印出 n 个 'A' 的最少操作次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/2-keys-keyboard
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def minSteps(self, n: int) -> int:
        f = [0] * (n + 1)
        for i in range(2, n + 1):
            f[i] = float("inf")
            j = 1
            while j * j <= i:
                if i % j == 0:
                    f[i] = min(f[i], f[j] + i // j)
                    f[i] = min(f[i], f[i // j] + j)
                j += 1

        return f[n]


if __name__ == '__main__':
    n = 65
    print(Solution().minSteps(n))