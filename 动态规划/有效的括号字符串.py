"""
给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

任何左括号 ( 必须有相应的右括号 )。
任何右括号 ) 必须有相应的左括号 ( 。
左括号 ( 必须在对应的右括号之前 )。
* 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
一个空字符串也被视为有效字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parenthesis-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cur = {0}
        for c in s:
            nxt = set()
            if not cur:
                return False
            if c == '(':
                for val in cur:
                    nxt.add(val + 1)
            elif c == ')':
                for val in cur:
                    if val - 1 >= 0:
                        nxt.add(val - 1)
            else:
                for val in cur:
                    nxt.add(val + 1)
                    nxt.add(val)
                    if val - 1 >= 0:
                        nxt.add(val - 1)
            cur = nxt
        return 0 in cur

if __name__ == '__main__':
    s = "(*))"
    print(Solution().checkValidString(s))