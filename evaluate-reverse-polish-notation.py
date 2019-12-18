"""
150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

Example 1:
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

"""
Runtime: 32 ms, faster than 99.73% of Python online submissions for Evaluate Reverse Polish Notation.
Memory Usage: 12.1 MB, less than 22.41% of Python online submissions for Evaluate Reverse Polish Notation.
"""
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        operators = {
            '+': lambda x, y: int(x) + int(y),
            '-': lambda x, y: int(x) - int(y), 
            '*': lambda x, y: int(x) * int(y),
            '/': lambda x, y: int(x)*1.0 / int(y)
        }
        
        stack = [0]
        
        for item in tokens:
            if item in operators:
                #rOperand = stack.pop()
                #lOperand = stack.pop()
				rOperand, lOperand = stack.pop(), stack.pop()
                res = operators[item](lOperand, rOperand)
                stack.append(res)
            else:
                stack.append(item)
            
        return int(stack.pop())
		
		
############################
import unittest


class TestSolution(unittest.TestCase):

              
    def test_1(self):
        out = 9
        tokens = ["2", "1", "+", "3", "*"]
        res = Solution().evalRPN(tokens)
        self.assertEqual(res, out)
        
                
    def test_2(self):
        out = 6
        tokens = ["4", "13", "5", "/", "+"]
        res = Solution().evalRPN(tokens)
        self.assertEqual(res, out)
        
                
    def test_3(self):
        out = 22
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        res = Solution().evalRPN(tokens)
        self.assertEqual(res, out)
   
    def test_4(self):
        out = -7
        tokens = ["4","-2","/","2","-3","-","-"]
        res = Solution().evalRPN(tokens)
        self.assertEqual(res, out)
   
   
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

    
		