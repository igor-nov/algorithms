"""
49. Group Anagrams - https://leetcode.com/problems/group-anagrams/

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.

Solutions:
https://leetcode.com/problems/group-anagrams/solution/

"""

class Solution(object):
    
    def checkIsAnagram2(self, baseSt, toCheck):
        
        if len(baseSt) != len(toCheck):
            return False
        
        dct = {}
        
        for ch in baseSt:
            if ch not in dct:
                dct[ch] = 0                
            dct[ch] += 1
            
        for ch in toCheck:
            if not ch in dct:
                return False
            else:
                if dct[ch] == 1:
                    del dct[ch]
                else:
                    dct[ch] -= 1
                    
        return False if len(dct) else True
        
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = []
        
        while len(strs):
            baseSt = strs.pop()
            res = [baseSt]
            
            i = 0
            while i < len(strs):
                if self.checkIsAnagram(baseSt, strs[i]):                
                    res.append(strs[i])
                    strs = strs[0:i]+strs[i+1:]                    
                    i -= 1
                i += 1
                
            groups.append(res)
            
        return groups
        
    
    def groupAnagrams1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        res = []
        specCase = 0
        groups = {}        
        for st in strs:
            
            lKey = len(st)
            
            if not lKey:            
                key = 32 #ord(' ')
                #specCase += 1
            else:
                key = ''.join(sorted(st))
                
            if not key in groups:
                groups[key] = []

            groups[key].append(st)
            
        for sKey in groups:            
            res.append(groups[sKey])
            
        return res
    
    
	# O = N*K
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ordA = ord('a')
        
        groups = {}
        
        for st in strs:
            key = [0] * 26
            for ch in st:
                pos = ord(ch) - ordA
                key[pos] += 1                
            
            dKey = tuple(key)
            if not dKey in groups:
                groups[dKey] = []
            
            groups[dKey].append(st)
            
        
        return [groups[gKey] for gKey in groups]
        
        

inp = ["eat", "tea", "tan", "ate", "nat", "bat"]
inp = ["eat", "tea", "tan", "ate", "nat", "bat", "st", "ts"]
inp = ["",""] # ["",""]

res = Solution().groupAnagrams(inp)

print res
