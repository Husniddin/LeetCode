class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals

        intervals.sort(key=lambda x: x[0])

        # [[1, 3], [2, 8], [4, 6], [15, 18]]

        non_o_intervals = []
        tmp = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= tmp[0] and intervals[i][0] <= tmp[1]:
                tmp[1] = max(tmp[1], intervals[i][1])
            else:
                non_o_intervals.append(tmp)
                tmp = intervals[i]

        non_o_intervals.append(tmp)
        
        return non_o_intervals

# Test Cases

s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
print(s.merge([[1,4],[4,5]]))