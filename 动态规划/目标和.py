"""
给你一个整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def findTargetSumWays(self, nums, target) -> int:
        m, s = len(nums), sum(nums)
        if abs(target) > abs(s): return 0

        dp = [[0] * (2 * s + 1) for _ in range(m)]
        dp[0][s + nums[0]] += 1
        dp[0][s - nums[0]] += 1

        for i in range(1, m):
            for j in range(2 * s + 1):
                l = j - nums[i] if j - nums[i] >= 0 else 0
                r = j + nums[i] if j + nums[i] < 2 * s + 1 else 0
                dp[i][j] = dp[i - 1][l] + dp[i - 1][r]
        return dp[-1][s + target]

