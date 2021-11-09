class Solution(object):
    def waysToStep(self, n):
        if n < 2:
            return 1
        a = 1
        b = 1
        c = 2
        for _ in range(3, n + 1):
            a, b, c = b, c, (a + b + c) % 1000000007
        return c

if __name__ == '__main__':
    num = 1
    print(num>>1)

