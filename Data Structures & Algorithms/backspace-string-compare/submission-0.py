class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []


        for c in s:
            if c == '#' and stack1:
                stack1.pop()

            elif c == '#' and not stack1:
                continue

            else:
                stack1.append(c)
        
        for c in t:
            if c == '#' and stack2:
                stack2.pop()
            elif c == '#' and not stack2:
                continue
            else:
                stack2.append(c)           
        
        return stack1 == stack2