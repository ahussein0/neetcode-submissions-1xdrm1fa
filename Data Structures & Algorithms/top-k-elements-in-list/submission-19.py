class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #1. create hash
        count = {}


        # 2. fill up the hash frequencies
        for num in nums:
            count[num] = count.get(num, 0) + 1

        #3. put the hash into an array and sort()

        arr = []
        for num, freq in count.items():
            arr.append([freq, num])

        # arr = [[3,1], [2,2], [1,3]]

        arr.sort() # ascending by frequency (index[0])

        # arr = [[1,3], [2,2], [3,1]]   ← ascending by freq

        # pull the freq and output

        res = []
        while len(res) < k:
            res.append(arr.pop()[1]) # pops and grabs the highest freq at the end places in res
            # [1] grabs the num which is the 2nd value in the pair
        return res





        
        