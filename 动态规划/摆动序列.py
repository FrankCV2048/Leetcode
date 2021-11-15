"""
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 摆动序列 。第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也视作摆动序列。

例如， [1, 7, 4, 9, 2, 5] 是一个 摆动序列 ，因为差值 (6, -3, 5, -7, 3) 是正负交替出现的。

相反，[1, 4, 7, 2, 5] 和 [1, 7, 4, 5, 5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
子序列 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。

给你一个整数数组 nums ，返回 nums 中作为 摆动序列 的 最长子序列的长度

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wiggle-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            if n == 2:
                if nums[0] == nums[1]:
                    return 1
                else:
                    return 2
            return n
        dp = [0] * n
        dp[0] = 1
        if nums[1] > nums[0]:
            dp[1] = 2
        elif nums[1] < nums[0]:
            dp[1] = -2
        else:
            dp[1] = 1

        for i in range(2, n):
            for j in range(0, i):
                if dp[j] == 1:
                    dp[i] = max(dp[i], 2)
                    if nums[i] > nums[j]:
                        dp[i] = 2
                    elif nums[i] < nums[j]:
                        dp[i] = -2
                    else:
                        dp[i] = 1
                if dp[j] < 0 and nums[i] > nums[j]:
                    dp[i] = max(dp[i], abs(dp[j]) + 1)
                elif dp[j] > 0 and nums[i] < nums[j]:
                    dp[i] = max(abs(dp[i]), dp[j] + 1)
                    dp[i] = -dp[i]
        dp = [abs(i) for i in dp]
        return max(dp)


if __name__ == '__main__':
    nums = [1,1,7,4,9,2,5]
    print(Solution().wiggleMaxLength(nums))
