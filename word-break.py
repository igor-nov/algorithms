"""
139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
			 
Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

Solutions:
ideserve - https://www.ideserve.co.in/learn/word-break-problem
Word Break Problem | DP-32 geeksforgeeks - https://www.geeksforgeeks.org/word-break-problem-dp-32/
Word Break Problem using Backtracking - https://www.geeksforgeeks.org/word-break-problem-using-backtracking/


Grapth:
A solution using BFS - https://leetcode.com/problems/word-break/discuss/43797/A-solution-using-BFS

Set:
DFS with Path Memorizing Java Solution - https://leetcode.com/problems/word-break/discuss/43819/DFS-with-Path-Memorizing-Java-Solution

Java implementation using DP in two ways - https://leetcode.com/problems/word-break/discuss/43790/Java-implementation-using-DP-in-two-ways
A Simple Python DP solution (check comment for improvement) - https://leetcode.com/problems/word-break/discuss/43995/A-Simple-Python-DP-solution
4 different ways to solve this with detailed explanation. - https://leetcode.com/problems/word-break/discuss/43908/4-different-ways-to-solve-this-with-detailed-explanation.
My Java DP solution beats 93.83% - https://leetcode.com/problems/word-break/discuss/43852/My-Java-DP-solution-beats-93.83
C++ Dynamic Programming simple and fast solution (4ms) with optimization - https://leetcode.com/problems/word-break/discuss/43814/C%2B%2B-Dynamic-Programming-simple-and-fast-solution-(4ms)-with-optimization
Simple DP solution in Python with description - https://leetcode.com/problems/word-break/discuss/43808/Simple-DP-solution-in-Python-with-description
The Time Complexity of The Brute Force Method Should Be O(2^n) and Prove It Below - https://leetcode.com/problems/word-break/discuss/169383/The-Time-Complexity-of-The-Brute-Force-Method-Should-Be-O(2n)-and-Prove-It-Below
Evolve from brute force to optimal, a review of all solutions - https://leetcode.com/problems/word-break/discuss/43886/Evolve-from-brute-force-to-optimal-a-review-of-all-solutions


http://www.zrzahid.com/word-break-problem/

Videos:
LeetCode Tutorial 139. Word Break - https://www.youtube.com/watch?v=YxtQUbKbdUs (http://www.goodtecher.com/leetcode-139-word-break/)
LeetCode 139. Word Break - https://www.youtube.com/watch?v=RPeTFTKwjps
Java coding interview questiion - Word break using Memoization - https://www.youtube.com/watch?v=3ejFHdqJg-E


Companies: https://youtu.be/YxtQUbKbdUs?t=816 (Google, Facebook, Amazon...)

@todo - check how to do it with max
implement next way - Java implementation using DP in two ways - https://leetcode.com/problems/word-break/discuss/43790/Java-implementation-using-DP-in-two-ways
4 lines in Python - https://leetcode.com/problems/word-break/discuss/43788/4-lines-in-Python
? DFS with Path Memorizing Java Solution - https://leetcode.com/problems/word-break/discuss/43819/DFS-with-Path-Memorizing-Java-Solution
dfs + prune + memoize+ explanation, beats 94% 44ms python ? https://leetcode.com/problems/word-break/discuss/128102/dfs-%2B-prune-%2B-memoize%2B-explanation-beats-94-44ms-python
"""


"""
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

29 / 36 test cases passed.
Time Limit Exceeded !!!!!!!!!!!!
"""
class Solution(object):
    def wordBreakHelper(self, s, wordDict, startFrom=0):
        
        if s in wordDict:
            return True
        
        for i in xrange(len(s)):        
            if s[:i] in wordDict and self.wordBreakHelper(s[i:], wordDict):
                return True
            
        return False
                    
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.wordBreakHelper(s, wordDict, 0)
		
		
"""
Runtime: 28 ms, faster than 79.22% of Python online submissions for Word Break.
Memory Usage: 10.8 MB, less than 77.62% of Python online submissions for Word Break
"""
class Solution(object):
    def wordBreakHelper(self, s, wordDict, wordBreak):
        
		lenS = len(s)
        
        for i in xrange(0, lenS):
            
            if wordBreak[i] == False and s[:i+1] in wordDict:
                wordBreak[i] = True
                
            if wordBreak[i] and i == lenS-1:
                return True
            
            if wordBreak[i]:
                for j in xrange(i, lenS):
                    if wordBreak[j] == False and s[i+1:j+1] in wordDict:
                        wordBreak[j] = True
                        
                    if wordBreak[j] and j == lenS-1:
                        return True
        
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
		
        wordDict = set(wordDict)   #set is faster    
        wordBreak = [False] * len(s)        
        self.wordBreakHelper(s, wordDict, wordBreak)
        
        return wordBreak[-1]
