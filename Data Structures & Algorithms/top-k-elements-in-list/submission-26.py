class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        arr = []

        for num, freq in count.items():
            arr.append([freq, num])
        arr.sort() # highest freq at the end 


        res = []

        while len(res) < k:
            res.append(arr.pop()[1]) # grabs the num value
        return res