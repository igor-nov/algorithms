"""
166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:

Input: numerator = 2, denominator = 1
Output: "2"

Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"

Solutions:

Idea is to put every remainder into the hash table as a key, and the current length of the result string as the value. When the same remainder shows again, it's circulating from the index of the value in the table.

Python solution - https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/137886/Python-solution
Python easy to understand solution with comments. - https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/51187/Python-easy-to-understand-solution-with-comments.
Fast and concise python solution using dictionary - https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/51186/Fast-and-concise-python-solution-using-dictionary.
Simple Python Solution - https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/157398/Simple-Python-Solution
Python 4 lines (32ms, beats 100%) with explanation - https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/180004/Python-4-lines-(32ms-beats-100)-with-explanation

"""

"""
Runtime: 16 ms, faster than 100.00% of Python online submissions for Fraction to Recurring Decimal.
Memory Usage: 10.6 MB, less than 100.00% of Python online submissions for Fraction to Recurring Decimal.
"""
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        
        sign = ''
        if numerator *  denominator < 0:
            sign = '-'
            
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        
        ceil, rem = divmod(numerator, denominator)
        res = [sign + str(ceil)]
        
        #print ceil, rem, res
        if rem == 0:
            return ''.join(res)
        
        res.append('.')
        
        prev = {}
        while rem:
                
            if rem in prev:
                pos = prev[rem]
                res.insert(pos, '(')
                res.append(')')
                break
            else:
                prev[rem] = len(res)
                ceil, rem = divmod(rem*10, denominator)
                res.append(str(ceil))
                
        return ''.join(res)
		

##########################

import unittest


class TestSolution(unittest.TestCase):
          
    def test_1(self):
        numerator = 1
        denominator = 2
        out = '0.5'
        res = Solution().fractionToDecimal(numerator, denominator)
        self.assertEqual(res, out)
    
    def test_2(self):
        numerator = 1
        denominator = -2
        out = '-0.5'
        res = Solution().fractionToDecimal(numerator, denominator)
        self.assertEqual(res, out)
        
    def test_3(self):
        numerator = 4
        denominator = 333
        out = '0.(012)'
        res = Solution().fractionToDecimal(numerator, denominator)
        self.assertEqual(res, out)
        
    
    def test_4(self):
        numerator = 0
        denominator = -5
        out = '0'
        res = Solution().fractionToDecimal(numerator, denominator)
        self.assertEqual(res, out)
        
        
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)