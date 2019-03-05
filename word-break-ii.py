"""
140. Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]



Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]


Solutions:

https://leetcode.com/problems/word-break-ii/discuss/44368/Python-easy-to-understand-solution-(DP%2BDFS%2BBacktracking).
https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution
https://leetcode.com/problems/word-break-ii/discuss/44345/Python-DP-solution-in-11-lines
https://leetcode.com/problems/word-break-ii/discuss/44298/DP-%2B-DFS-in-Python
"""

"""
Runtime: 28 ms, faster than 96.20% of Python online submissions for Word Break II.
Memory Usage: 10.9 MB, less than 92.39% of Python online submissions for Word Break II.
"""
class Solution(object):
    
	def isBreakable(self, s, wordDict):
        
		if not s:
            return True
        
        wb = [False] * len(s)
        
        for i in xrange(len(s)):
            
            if not wb[i] and s[:i+1] in wordDict:
                wb[i] = True
                
            if wb[i]:
                for j in xrange(i+1, len(s)):
                    if s[i+1:j+1] in wordDict:
                        wb[j] = True
            
        return wb[-1]
		
    def wordBreakHelper(self, s, wordDict, res, tmp):
            
        if self.isBreakable(s, wordDict):

            if not s:
                res.append(' '.join(tmp))

            for i in xrange(len(s)):
                if s[:i+1] in wordDict:
                    self.wordBreakHelper(s[i+1:], wordDict, res, tmp + [s[:i+1]])
            
        return res
    
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        wb = [False] * len(s)
        wordDict = set(wordDict)
        self.wordBreakHelper(s, wordDict, res, [])
        
        return res
		