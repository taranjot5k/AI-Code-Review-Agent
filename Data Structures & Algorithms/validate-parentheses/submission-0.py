class Solution:
    def isValid(self, s: str) -> bool:
        stack= [ ] #remember the opening brackets that we've encountered and haven't closed yet.
        brackets = { 
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s: 
            if c not in brackets: #If c is NOT one of ), }, ]
                stack.append(c)
            if c in brackets: 
                if not stack: 
                    return False 
                if stack.pop() != brackets[c]:
                    return False 

        if not stack: 
            return True 
        else:
            return False  
            




            
                 
        