class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        non_overlap = []

        for i in range(len(intervals)):
            if not non_overlap or non_overlap[-1][1] <= intervals[i][0]:
                non_overlap.append(intervals[i])
            else:
                pass
        return len(intervals) - len(non_overlap)
        
        # o n log n 
        # sorting costs n log n 

        # looping happens once o(n)

        #indexing comparision is o(1)