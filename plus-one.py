"""
66. Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

---

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

---

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.


Solutions:

https://leetcode.com/problems/plus-one/discuss/24082/My-Simple-Java-Solution
https://leetcode.com/problems/plus-one/discuss/24085/Simple-Python-solution-with-explanation-(Plus-One)
https://leetcode.com/problems/plus-one/discuss/24090/Python-simple-solution-using-recursion

"""

class Solution(object):
    
	#48 ms
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        if not digits:
            return [1]
        else:
            print digits
            res =  int(''.join(str(i) for i in digits))
            res += 1
            
            res = [int(i) for i in str(res)]
            
            #print type(res)
            return res
			
	#20 ms - 100% - https://leetcode.com/problems/plus-one/discuss/24085/Simple-Python-solution-with-explanation-(Plus-One)
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        str_digits = ''.join(str(i) for i in digits)
        int_digits = int(str_digits) + 1
        str_digits = str(int_digits)
        for i in str_digits:
            result.append(int(i))
        return result
        
        
	#24 ms
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        else:
            
            overflow = 1
            i = len(digits)-1
            while i >= 0:
                #print i
                overflow, res = divmod(digits[i] + overflow, 10)                
                #print overflow, res
                digits[i] = res                
                i -= 1
                
            if overflow:
                #digits = [overflow] + digits
                digits.insert(0, overflow)
                
            return digits
        
	#24 ms
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        else:      
            num = 0
            for i in xrange(len(digits)-1, -1, -1):            
                num += digits[i] * 10**(len(digits)- i -1)
            num += 1
            
            res = []
            while num:
                num, rem = divmod(num, 10)
                res.insert(0, rem)

            return res
			
	#28 ms
	def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        else:
            
            i = len(digits)-1
            while i >= 0:                
                if digits[i] < 9:
                    digits[i] +=1
                    return digits                    
                else:
                    digits[i] = 0
                    i -= 1
                
            return [1] + digits
			
        
        
    
inp = [1,2,3]
#inp = None
#inp = [9,9,9]

res = Solution().plusOne(inp)
print res
