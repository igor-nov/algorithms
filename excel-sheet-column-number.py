"""
171. Excel Sheet Column Number
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28

Example 3:

Input: "ZY"
Output: 701


Solutions:

Explanation in Python - https://leetcode.com/problems/excel-sheet-column-number/discuss/52289/Explanation-in-Python
Python concise solution. - https://leetcode.com/problems/excel-sheet-column-number/discuss/52304/Python-concise-solution.
Python solution - https://leetcode.com/problems/excel-sheet-column-number/discuss/143309/Python-solution
Recursive My solutions in 3 languages, does any one have one line solution in Java or C++? - https://leetcode.com/problems/excel-sheet-column-number/discuss/52107/My-solutions-in-3-languages-does-any-one-have-one-line-solution-in-Java-or-C%2B%2B



"""


"""
Runtime: 32 ms, faster than 37.38% of Python online submissions for Excel Sheet Column Number.
Memory Usage: 10.6 MB, less than 87.40% of Python online submissions for Excel Sheet Column Number.
"""
class Solution(object):
    
    def __init__(self):
        self.chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.charsDict = { self.chars[i]: i+1 for i in xrange(len(self.chars))}
        self.charsLen = len(self.chars)
        
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        power = 0
        
        for i in xrange(len(s)-1, -1, -1):
            val = self.charsDict[s[i]]
            #print s[i], val, res
            res += self.charsLen ** power * val
            power += 1
        return res
		
################################################################################################

"""
Runtime: 28 ms, faster than 78.04% of Python online submissions for Excel Sheet Column Number.
Memory Usage: 10.7 MB, less than 62.99% of Python online submissions for Excel Sheet Column Number
"""
class Solution(object):
    
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        power = 0
        
        for i in xrange(len(s)-1, -1, -1):
            val = ord(s[i]) - ord('A') + 1
            res += 26 ** power * val
            power += 1
        return res
		
		
###################################################################################################

"""
Runtime: 28 ms, faster than 78.04% of Python online submissions for Excel Sheet Column Number.
Memory Usage: 10.9 MB, less than 11.81% of Python online submissions for Excel Sheet Column Number.
"""

class Solution(object):
    
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x, y: 26*x + y, [ord(ch) - ord('A') + 1 for ch in list(s)])
		
		
#####################################################################################################

"""
Runtime: 28 ms, faster than 78.04% of Python online submissions for Excel Sheet Column Number.
Memory Usage: 10.8 MB, less than 22.83% of Python online submissions for Excel Sheet Column Numbe
"""

class Solution(object):
    
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = 0
        for ch in s:
            res = res * 26 + ord(ch) - 64
        return res
		
