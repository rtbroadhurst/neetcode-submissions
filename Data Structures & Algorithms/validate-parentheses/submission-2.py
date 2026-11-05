class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c =  {')' : '(',
                 ']' : '[', 
                 '}' : '{',}
        
        for char in s:
            if char in c.values():
                stack.append(char)
            else:
                if stack and c[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0