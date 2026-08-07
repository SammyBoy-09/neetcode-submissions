class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        op = ['(', '[', '{']
        cl = {')':'(', ']' : '[', '}':'{'} 

        if len(s) % 2 != 0:
            return False

        for i in s:
            if i in op:
                stack.append(i)
            elif stack != [] and cl[i] == stack[-1]:
                stack.pop()
            else:
                return False
        
        if stack == []:
            return True
        else:
            return False
                
        