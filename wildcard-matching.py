"""
44. Wildcard Matching

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.

-------------

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

-------------

Example 2:
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

-------------

Example 3:
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Solutions:

1.
https://www.youtube.com/watch?v=3ZDZ-N0EPV0
@todo - decrease space complexity //We can improve space complexity by making use of the fact that we only uses the result from last row.https://www.geeksforgeeks.org/wildcard-pattern-matching/

2.
https://leetcode.com/problems/wildcard-matching/discuss/17810/Linear-runtime-and-constant-space-solution
http://yucoding.blogspot.com/2013/02/leetcode-question-123-wildcard-matching.html
https://leetcode.com/problems/wildcard-matching/discuss/17811/My-three-C%2B%2B-solutions-(iterative-(16ms)-and-DP-(180ms)-and-modified-recursion-(88ms))
https://leetcode.com/problems/wildcard-matching/discuss/17950/Fastest-non-DP-solution-with-O(1)-space

3 @todo  - Finite-state machine - https://leetcode.com/problems/wildcard-matching/discuss/138878/Finite-state-machine-with-Python-and-dictionary.-13-lines-O(p%2Bs)-time





"""

class Solution(object):
    
	"""
    merge sequences of * in to single * as they mean the same thing
    """
    def simplifyPattern(self, p):
        
        if not p:
            return p
        
        newPat = p[0]
        for i in xrange(1, len(p)):
            if not (p[i] == '*' and p[i] == p[i-1]):                
                newPat += p[i]
                
        return newPat
                   
        
    
	# O(n*m)
    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        p = self.simplifyPattern(p)
        
        dMtx = [[False for i in xrange(len(p)+1)] for i in xrange(len(s)+1)]
        
        for i in xrange( len(p) + 1):            
            if i == 0 or ( p[i-1] == '*' and dMtx[0][i-1] == True):
                dMtx[0][i] = True
                
       
                
        for i in xrange(1, len(s) + 1):
            for j in xrange(1, len(p) + 1):
                
                #print 'i %s j %s s=%s p=%s' % (i, j, s[i-1], p[j-1])
                #1 ? or j == i 
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dMtx[i][j] = dMtx[i-1][j-1]
                    #print '=i %s j %s s=%s p=%s' % (i, j, s[i-1], p[j-1])                                
                
                #2 *
                elif p[j-1] == '*':
                    dMtx[i][j] = dMtx[i-1][j] or dMtx[i][j-1]
                    #print '*i %s j %s s=%s p=%s' % (i, j, s[i-1], p[j-1])                                
                    
                #3 False
                else:
                    pass
        
        for row in dMtx:
            print row
            
        return dMtx[-1][-1]
		
		
	def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        #p = self.simplifyPattern(p)
        pPt = 0
        sPt = 0
        match = 0
        star = -1
        
        while sPt < len(s):            
            
            #print sPt, pPt
            
            if pPt < len(p) and (s[sPt] == p[pPt] or p[pPt] == '?'):
                sPt += 1
                pPt += 1
                
            elif  pPt < len(p) and  p[pPt] == '*':
                match = sPt                
                star = pPt
                pPt += 1
                
            elif star != -1:
                pPt = star + 1                                
                match += 1                
                sPt = match 
				
            else:
                return False
            
                
        while pPt < len(p) and p[pPt] == '*':
            pPt += 1
        
        if pPt !=  len(p):
            return False
        
        return True
		
	
        
s = "adceb"
p = "*a*b"
#true

s = "acdcb"
p = "a*c?b"
#Output: false

s = "acdb"
p = "a*c?b"
#Output: false

s = "aab"
p = "c*a*b"
#Output: false

# s = "aa"
# p = "*"
#Output: True

# s = "aa"
# p = "***b**" #false

# s = ""
# p = "" # false

res = Solution().isMatch(s, p)
print res


import unittest

class TestSolution(unittest.TestCase):
    
    def test_1(self):
        s =  ""
        p = ""
        out = True
        res = Solution().isMatch(s, p)
        self.assertEqual(res, out)
        
    def test_2(self):
        s =  "aa"
        p = "***b**"
        out = False
        res = Solution().isMatch(s, p)
        self.assertEqual(res, out)
        
    def test_3(self):
        s =  "aa"
        p = "*"
        out = True
        res = Solution().isMatch(s, p)
        self.assertEqual(res, out)
        
    def test_4(self):
        s = "aab"
        p = "c*a*b"
        out = False
        res = Solution().isMatch(s, p)
        self.assertEqual(res, out)
        
    def test_5(self):
        s = "adceb"
        p = "*a*b"
        out = True
        res = Solution().isMatch(s, p)
        self.assertEqual(res, out)
        
    def test_6(self):
        s = "acdcb"
        p = "a*c?b"
        out = False
        res = Solution().isMatch(s, p)
        self.assertEqual(res, out)
        
    def test_7(self):
        s = "acdb"
        p = "a*c?b"
        out = True
        res = Solution().isMatch(s, p)
        self.assertEqual(res, out)

    def test_8(self):
        s =  "a"
        p = "aa"
        out = False
        res = Solution().isMatch(s, p)
        self.assertEqual(res, out)
        
    def test_9(self):
        s =  "abefcdgiescdfimde"
        p = "ab*cd?i*de"
        out = True
        res = Solution().isMatch(s, p)
        self.assertEqual(res, out)
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)