class Solution(object):
    def trap1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if len(height) == 0:
            return 0
        maxLen = 0
        for i in range(len(height)):
            if height[i] > maxLen:
                maxLen = height[i]
        if maxLen == 0:
            return 0
        sum = 0
        for i in range(1, maxLen+1):
            index = 0
            maxLen = 0
            first = 0
            for j in range(n):
                if height[j] != 0:
                    if first == 0:
                        index = j
                        first = 1
                    if j >= index:
                        maxLen = j
                    height[j] -= 1
                    sum -= 1
            sum += maxLen-index + 1

        return sum

    def trap(self, height):
        n = len(height)
        if len(height) == 0:
            return 0
        left_max = [0 for _ in range(n)]
        right_max = [0 for _ in range(n)]
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i-1])
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
        ans = 0
        for i in range(1, n):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    print(solution.trap(height))