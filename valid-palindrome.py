"""
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false

https://leetcode.com/problems/valid-palindrome/discuss/40094/Challenge-me-Shortest-possible-answer-in-python-for-Valid-Palindrome-(Life-is-short-we-need-python)

"""
class Solution(object):
    
	"""
	Runtime: 32 ms, faster than 99.91% of Python online submissions for Valid Palindrome.
	Memory Usage: 12.7 MB, less than 0.95% of Python online submissions for Valid Palindrome.
	"""
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        s = [ch for ch in s.lower() if ch.isalnum()]
        return s == s[::-1]
        


class Solution2(object):    
	"""
	Runtime: 36 ms, faster than 95.47% of Python online submissions for Valid Palindrome.
    Memory Usage: 12.7 MB, less than 0.95% of Python online submissions for Valid Palindrome.
    #s = self.toAlphaArr(s)
	"""
	def toAlphaArr(self, s):        
        alphaNum = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '0','1','2','3','4','5','6','7','8','9')
        s = list(s.lower())        
        s = [ch for ch in s if ch in alphaNum]
        return s
		
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        s = self.toAlphaArr(s)
        sOrig = ''.join( str(ch) for ch in s )
		
        s.reverse()
        sRev = ''.join( str(ch) for ch in s )
        
        return sOrig == sRev
        
class Solution3(object):
	"""
	Runtime: 32 ms, faster than 99.91% of Python online submissions for Valid Palindrome.
    Memory Usage: 12.7 MB, less than 0.95% of Python online submissions for Valid Palindrome.
	"""
    
    def toAlphaArr(self, s):
        s = list(s.lower())
        s = [ch for ch in s if ch.isalnum()]
        return s
        
    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        s = self.toAlphaArr(s)
        
        sOrig = ''.join( str(ch) for ch in s )
        s.reverse()
        sRev = ''.join( str(ch) for ch in s )
        
        return sOrig == sRev
	
	
###############################################################

import unittest


class TestSolution(unittest.TestCase):

                
    def test_1(self):        
        inp = "A man, a plan, a canal: Panama"
        out = True
        res = Solution().isPalindrome(inp)
        self.assertEqual(res, out)
        
    def test_2(self):        
        inp = "race a car"
        out = False
        res = Solution().isPalindrome(inp)
        self.assertEqual(res, out)
        
    def test_3(self):        
        inp = "0P"
        out = False
        res = Solution().isPalindrome(inp)
        self.assertEqual(res, out)
        
    def test_4(self):        
        inp = ".G?j!:;;:Gj?!."
        out = False
        res = Solution().isPalindrome(inp)
        self.assertEqual(res, out)
        
        
    def test_5(self):        
        inp = ".jG?!:;;:Gj?!."
        out = True
        res = Solution().isPalindrome(inp)
        self.assertEqual(res, out)
        
   
        
   
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
	
