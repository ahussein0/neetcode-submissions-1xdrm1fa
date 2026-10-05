class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0
        n = len(intervals)


        # phase 1 skipped every interval whose end was before newInterval starts 
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # overlaps happen here .. current interval starts before the newInterval ends
        while i < n and intervals[i][0] <= newInterval[1]:
            # merging happens here
            # grab the minimum between the two intervals
            newInterval[0] = min(intervals[i][0], newInterval[0])

            #grab the max
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        merged.append(newInterval)
        
        # right side of the intervals which dont overlap add to merged
        for j in range(i,n):
            merged.append(intervals[j])
        return merged