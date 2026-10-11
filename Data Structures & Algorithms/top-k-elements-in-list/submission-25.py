class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        arr = []
        for num, freq in count.items():
            arr.append([freq, num])
        arr.sort() # <-- puts most frequent numbers in the back

        # arr = [1:4, 2:3, 3:2] k = 2

        res = []

        while len(res) < k:
            res.append(arr.pop()[1]) # pops from the back where the most frequent entries live and takes the 2nd index
        return res



        