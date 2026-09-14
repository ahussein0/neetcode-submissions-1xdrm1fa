class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg = 0
        end = len(nums) - 1

        # find midpoint

        while beg <= end:
            midpoint = (beg + end) // 2

            mid_val = nums[midpoint]

            if mid_val == target:
                return midpoint

            elif mid_val <= target:
                beg = beg + 1
            
            else:
                end = end - 1
        return -1
        