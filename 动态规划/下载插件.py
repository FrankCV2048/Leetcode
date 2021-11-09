from math import log


class Solution(object):
    def leastMinutes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        if n & (n-1) != 0:
            return int(log(n, 2)) + 2
        else:
            return int(log(n, 2)) + 1


if __name__ == '__main__':
    pass