class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[0])  # 按每个元素的左边界排序
        N = len(intervals)
        if N == 0: return 0
        dp = [1 for _ in range(N)]  # 初始化
        # 求 去掉某1个或n个元素后 最大non-overlapping intervals的长
        for i in range(N):
            for j in range(i - 1, -1, -1):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    break
        return N - max(dp)


if __name__ == '__main__':
    intervals = [[1,2],[1,3],[2,3],[3,4]]
    print(Solution().eraseOverlapIntervals(intervals))