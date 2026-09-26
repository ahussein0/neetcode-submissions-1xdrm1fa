class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        arr = []
        for num, freq in count.items():
            arr.append([freq,num])
        arr.sort()

        res = [num for freq, num in arr[-k:]]

        return res