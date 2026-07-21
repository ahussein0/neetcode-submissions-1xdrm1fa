class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pars = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in pars:
                if stack and stack[-1] == pars[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        