"""
191. Number of 1 Bits
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.


Add Two Numbers Without The "+" Sign (Bit Shifting Basics) -> https://www.youtube.com/watch?v=qq64FrA2UXQ

Runtime: 8 ms, faster than 98.74% of Python online submissions for Number of 1 Bits.
Memory Usage: 11.7 MB, less than 70.00% of Python online submissions for Number of 1 Bits.
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 0000001011 -> 3
        count = 0
        for _ in range(32):
        #while n: #Runtime: 24 ms
            if n & 1:
                count += 1                
            n = n >> 1

        return count
