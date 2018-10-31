class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        dict = {')':'(', ']':'[', '}':'{'}
        stack = []
        
        for ch in s:            
            if ch not in dict.values():
                
                if not len(stack):
                    return False
                
                prevCh = stack.pop()
                
                if(prevCh != dict[ch]):
                    return False 
                
            else:
                stack.append(ch)
        
        if len(stack) != 0:
            return False        
        
        return True