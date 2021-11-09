class Solution(object):
    def reverseBits(self, num):
        """
        :type num: int
        :rtype: int
        """

        s = [0]*32
        nums = bin(num & 0xffffffff).replace('0b', '')
        for i in range(len(nums)):
            s[len(s)-i-1] = int(nums[i])

        left = [0 for _ in range(len(s))]
        right = [0 for _ in range(len(s))]
        left[0] = s[0]
        right[0] = s[-1]
        for i in range(1,len(s)):
            if s[i] == 1:
                left[i] = left[i-1] + 1
            if s[i] == 0:
                left[i] = 0
            if s[len(s)- i- 1] == 1:
                right[i] = right[i-1] + 1
            if s[len(s) - i - 1] == 0:
                right[i] = 0
        right = right[::-1]
        max1 = max(right[1]+1, left[len(s)-2]+1)
        for i in range(1, len(s)-1):
            if max1 <= (left[i-1]+right[i+1]):
                max1 = left[i-1]+right[i+1] + 1
        return max1
        # 对每一个数字都找出他的最左边零，和最右边零 记录 然后每个点计算差值即可

if __name__ == '__main__':
    print(Solution().reverseBits(-1))

