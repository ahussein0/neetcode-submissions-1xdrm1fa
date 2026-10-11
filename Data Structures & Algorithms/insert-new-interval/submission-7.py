class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        merged = []

        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        
        # overlap check
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        merged.append(newInterval)

        # right side of the insert

        for j in range(i,n):
            merged.append(intervals[j])
        return merged

        