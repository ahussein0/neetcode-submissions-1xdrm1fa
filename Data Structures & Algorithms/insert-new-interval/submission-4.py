class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0
        n = len(intervals)


        # phase 1 copies intervals that are before newInterval and cannot overlap it
        #  For [1,2], [4,6] with newInterval = [5,8], it does not copy [4,6] because 6 < 5 is false. That leaves [4,6] for Phase 2, where it can be merged with [5,8].
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # overlaps happen here .. check if 
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