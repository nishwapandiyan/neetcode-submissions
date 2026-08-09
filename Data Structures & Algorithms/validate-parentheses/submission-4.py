class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            if stack:    
                if ch == ')' and stack.pop() != '(':
                    return False
                    
                elif ch == ']' and stack.pop() != '[':
                    return False
                    
                elif ch == '}' and stack.pop() != '{':
                    return False        
            else:
                return False
        else:
          if len(stack) == 0:
            return True
          else:
            return False