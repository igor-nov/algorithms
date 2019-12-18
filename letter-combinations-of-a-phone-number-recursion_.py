#Runtime: 20 ms, faster than 100.00% of Python online submissions for Letter Combinations of a Phone Number.

"""
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

examples : https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8070/One-line-python-solution

"""

class Solution(object):
    
    def __init__(self):        
        #mapping digit to character set
        self.d2l = {
            1: '',
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        
    """
    parse string of numbers and return list of possible characters to combine    
    """
    def num2list(self, number):        
        digList = [ self.d2l[int(item)] for item in number]                
        return digList
    
    """
    add items from new charset to previous combinations
    """
    def addItemsToCombinations(self, set1, set2):
        combinations = []        
        for ch1 in set1:
            for ch2 in set2:                
                combinations.append("%s%s" % (ch1, ch2))                
        return combinations
                
                
    """
    get combinations
    """
    def getComb(self, listForCombinations):
        combinations = []
        
        #reqursivle go through all combinations combining only 2 at once
        while len(listForCombinations) > 0:
            
            #if it's 1st run we have to fill empty part (combinations)
            if len(combinations) == 0:
                combinations = listForCombinations.pop(0)
                
            newPart = listForCombinations.pop(0)                            
            combinations = self.addItemsToCombinations(combinations, newPart)
        
        return combinations
        
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        digComb = self.num2list(digits)
        
        if len(digComb) == 0:
            return []
        elif len(digComb) == 1:            
            return [ch for ch in digComb[0]]
        
        res = self.getComb(digComb)
        
        return res
               
        
        
        
inp = "43"
inp = ""
inp = "2"
#inp = "2345"
#inp = "2345"
inp = "234"
#inp = "23" #["ad","ae","af","bd","be","bf","cd","ce","cf"]

res = Solution().letterCombinations(inp)
print res
print len(res)

tmp = ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]
print len(tmp)
    