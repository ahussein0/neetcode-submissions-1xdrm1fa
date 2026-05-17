class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {} # characters were looking for 
        window = {} # window were building

        # build out countT {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have = 0
        need = len(countT)

        res = [-1,-1]
        resLen = float("infinity")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # check if 'c' is a character in countT  & if the char amount is the same
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need: # shrink while window is valid
                if r - l + 1 < resLen: # is this window the new best?
                    res = [l , r] # save bounds
                    resLen = r - l + 1  # save the new best length
                
                window[s[l]] -= 1 # done with this window now lets remove

                if s[l] in countT and window[s[l]] < countT[s[l]]: # check if we unsatisfied some conditions
                    have -= 1 
                
                l += 1 # move forward
        l ,r = res # tuple unpacking

        return s[l : r + 1] if resLen != float("infinity") else ""
