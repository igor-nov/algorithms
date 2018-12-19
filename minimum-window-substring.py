"""
76. Minimum Window Substring


Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.


Solutions
https://leetcode.com/problems/minimum-window-substring/
https://leetcode.com/problems/minimum-window-substring/discuss/26835/Java-4ms-bit-97.6

@todo - use counter 

"""

class Solution(object):
    
    def checkIsDone(self, tD):
        
        #for key, val in tD.items():           
        for key in tD:
            if tD[key] > 0:
                return False
            
        return True
    
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        if not t:
            return ""
        elif s == t:
            return t
               
        
        lo = hi = 0
        fSt, fEnd = None, None
        tDict = {}
        
        for ch in t:
            if not ch in tDict: 
                tDict[ch] = 1
            else: 
                tDict[ch] += 1
        
        appQueue = []
        
        for i in xrange(len(s)):            
		
            if s[i] in tDict:
                appQueue.append(i)
                tDict[s[i]] -= 1
                isDone = self.checkIsDone(tDict)
                
                if self.checkIsDone(tDict):
                    hi = i
                    lo = appQueue[0]
					
                    while self.checkIsDone(tDict): 
            
                        if fEnd is None and fSt is None or (fEnd - fSt) > (hi - lo):                            
                            fEnd, fSt = hi, lo

                        chIdx = appQueue.pop(0)
                        ch = s[chIdx]
                        tDict[ch] += 1                    
                        if appQueue:
                            lo = appQueue[0]
                    
					
        if fEnd is not None and fSt is not None:
            return s[fSt:fEnd+1]
        else:
            return ""
        
             
s = "ADOBECODEBANC"
t = "ABC"
#Output: "BANC"

s = "ABACDOBECODEBAN"
t = "ABC" #BAC

s = "ABACDOBECODEBANABC"
t = "ABC" # ""

# s = "aaaa" 
# t = "aaa"
    
res = Solution().minWindow(s, t)
print 'res %s' % res


############## unit
import unittest

class TestSolution(unittest.TestCase):
    
    def test_1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        o = "BANC"
        res = Solution().minWindow(s,t)
        self.assertEqual(res, o)
        
    def test_2(self):
        s = "ABACDOBECODEBAN"
        t = "ABC"
        o = "BAC"
        res = Solution().minWindow(s,t)
        self.assertEqual(res, o)
        
    def test_3(self):
        s = "AAA"
        t = "AA"
        o = "AA"
        res = Solution().minWindow(s,t)
        self.assertEqual(res, o)
        
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

        