"""
Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"

Solutions:
https://www.youtube.com/watch?v=Fi5INvcmDos
https://www.youtube.com/watch?v=obBdxeCx_Qs
https://www.youtube.com/watch?v=0xeBqanD5GQ
https://www.youtube.com/watch?v=HBtiDHIOK9A

https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

O(N) Manacher's Algorithm
https://www.youtube.com/watch?v=V-sEwsca1ak
https://www.youtube.com/watch?v=nbTSfrEfo6M


"""


class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        isPalM = [[None for i in xrange(len(s))] for i in xrange(len(s))]
        
        lt = gt = 0
        for j in xrange(1, len(s)):
            for i in xrange(0, j):
                isPal = isPalM[i+1][j-1] or j-i <= 2
                if isPal and s[i] == s[j]:
                    isPalM[i][j] = True
                    if gt - lt < j - i:
                        lt, gt = i, j
                    
        return s[lt:gt+1]

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        palMtrx = [[None for i in xrange(len(s))] for i in xrange(len(s))]
        
        
        lt = gt = 0        
        
        for i in xrange(0, len(s)):
            palMtrx[i][i] = True            
                    
        for i in xrange(1, len(s)):            
            if s[i-1] == s[i]:
                palMtrx[i-1][i] = True                
                lt, gt = i-1, i
                             
        for w in xrange(2, len(s)):            
            for i in xrange(0, len(s)-w):                
                j = i + w                
                isPal = palMtrx[i+1][j-1] and s[i] == s[j]
                if isPal:
                    palMtrx[i][j] = True
                    
                    if gt - lt < j - i:
                        lt, gt = i, j

        return s[lt:gt+1]
		

inp = 'babad'
inp = 'babadweqw'
inp = 'bba'
inp = 'cbbd'
inp = 'ccc'
res = Solution().longestPalindrome(inp)

print res