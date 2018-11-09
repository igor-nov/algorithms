"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if not needle:
            return 0
        
        if not haystack:
            return -1
        
        if len(needle) >  len(haystack):
            return -1
        
        search = "" 
        for i in xrange(len(needle)):
            search += haystack[i]
         
        if search == needle:
            return 0
        else:
            for i in xrange(len(needle), len(haystack)):
                search = search[1:] + haystack[i]
                if search == needle:
                    return i-len(needle) + 1
            return -1
        
        
haystack = "hellot"
needle = "llott"


haystack = ""
needle = "a"

haystack = "aaa"
needle = "aaaa"

res  = Solution().strStr(haystack, needle)
print res