class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        par = list(S)
        stack = []
        num = 0
        while len(par) != 0:
        # for i in range(len(par)):
            if par[-1] == ')':
                stack.append(par.pop())
                # print("stack: ", stack)
            else:
                if len(stack) == 0:
                    par.pop()
                    num += 1
                else:
                    par.pop()
                    stack.pop()
                    # print("stack: ", stack)
            # print("par: ", par)
        final = len(stack) + num
        return final


p = Solution()
print(p.minAddToMakeValid("())"))