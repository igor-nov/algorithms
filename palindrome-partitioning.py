"""
131. Palindrome Partitioning


Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]



Solutions:
https://leetcode.com/problems/palindrome-partitioning/discuss/41973/Python-recursiveiterative-backtracking-solution
https://leetcode.com/problems/palindrome-partitioning/discuss/41963/Java%3A-Backtracking-solution.
My Java DP only solution without recursion - https://leetcode.com/problems/palindrome-partitioning/discuss/41974/My-Java-DP-only-solution-without-recursion.-O(n2)
https://leetcode.com/problems/palindrome-partitioning/discuss/41982/Java-DP-%2B-DFS-solution
https://leetcode.com/problems/palindrome-partitioning/discuss/41964/Clean-C%2B%2B-backtracking-solution
https://leetcode.com/problems/palindrome-partitioning/discuss/182307/Java%3A-Backtracking-Template-General-Approach
https://leetcode.com/problems/palindrome-partitioning/discuss/42101/C%2B%2B-backtracking

WTF - https://leetcode.com/problems/palindrome-partitioning/discuss/42025/1-liner-Python-Ruby


@todo - check not reqursive solution
+ add memoizations
"""


"""
Runtime: 96 ms, faster than 79.58% of Python online submissions for Palindrome Partitioning.
Memory Usage: 11 MB, less than 100.00% of Python online submissions for Palindrome Partitioning.
"""
class Solution(object):
    
    def is_palindrome(self, s):
        return s == s[::-1]
    
    def partition_helper(self, s, path, res):
        
         
        if not s:
            res.append(path[:])
            return
            
        for i in xrange(1, len(s)+1):
            if self.is_palindrome(s[:i]):
                self.partition_helper(s[i:], path + [s[:i]], res)
        
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        res = []
        self.partition_helper(s, [], res)
        return res
		

"""
2nd variant
don't mutate string
Runtime: 96 ms, faster than 79.58% of Python online submissions for Palindrome Partitioning.
Memory Usage: 11.3 MB, less than 100.00% of Python online submissions for Palindrome Partitioning.
"""
"""
Runtime: 96 ms, faster than 79.58% of Python online submissions for Palindrome Partitioning.
Memory Usage: 11 MB, less than 100.00% of Python online submissions for Palindrome Partitioning.
"""
class Solution(object):
    def is_palindrome(self, s):
        return s == s[::-1]
    
    def partition_helper(self, s, lo, hi, path, res):
         
        if lo > hi:
            res.append(path[:])
            return
            
        for i in xrange(lo, hi+1):
            if self.is_palindrome(s[lo:i+1]):
                self.partition_helper(s, i+1, hi, path + [s[lo:i+1]], res)
        
    
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.partition_helper(s, 0, len(s)-1,  [], res)
        return res


		
        
        
		
####################################################

import unittest


class TestSolution(unittest.TestCase):
       
    def test_1(self):        
        inp = "aab"
        out = [
                ["a","a","b"],
                ["aa","b"]
            ]
        res = Solution().partition(inp)
        self.assertEqual(res, out)
     
   
    def test_2(self):        
        inp = ""
        out = [
                []
            ]
        res = Solution().partition(inp)
        self.assertEqual(res, out)
     
   
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)