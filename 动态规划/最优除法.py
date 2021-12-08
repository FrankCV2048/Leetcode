"""
给定一组正整数，相邻的整数之间将会进行浮点除法操作。例如， [2,3,4] -> 2 / 3 / 4 。

但是，你可以在任意位置添加任意数目的括号，来改变算数的优先级。你需要找出怎么添加括号，才能得到最大的结果，并且返回相应的字符串格式的表达式。你的表达式不应该含有冗余的括号。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/optimal-division
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n = len(nums)
        if n == 0: return ""
        if n == 1: return str(nums[0])
        if n == 2: return str(nums[0]) + "/" + str(nums[1])
        res = str(nums[0])
        res += "/(" + str(nums[1])
        for i in range(2, n):
            res += "/" + str(nums[i])
        res += ")"
        return res
