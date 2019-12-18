
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
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        res = [""]
        for i in digits:
            tmp = []            
            for ch in self.d2l[int(i)]:                
                #if len(res) > 0: # we can skip this if we set res = [""] as empty string
                    for lt in res:                    
                        tmp.append(lt+ch)
                #else:
                #    tmp.append(ch)
            res = tmp
            
        return res
                    
            
        
        
#inp = "23456"
inp = "23" #["ad","ae","af","bd","be","bf","cd","ce","cf"]

res = Solution().letterCombinations(inp)
print res
