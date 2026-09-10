class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        l = 0

        maxF = 0

        # fill up the hash map
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

        # shrink while invalid
            while ( r - l  + 1 ) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            maxF = max(r - l + 1, maxF)
        return maxF

            

