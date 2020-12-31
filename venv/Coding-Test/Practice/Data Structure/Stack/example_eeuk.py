class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        good = 0

        for i in S:
            if i == '(':
                stack.append(i)
            else:
                if stack != []:
                    stack.remove('(')
                    good += 2
        return len(S) - good