class Solution:
    def generate(self, numRows):
        if numRows <= 0:
            return []
        ret = [[1]]
        for i in range(numRows+1):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[j] + ret[j - 1])
            ret = row
        return ret

if __name__ == '__main__':
    print(Solution().generate(3))