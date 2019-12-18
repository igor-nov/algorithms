"""
1160. Find Words That Can Be Formed by Characters

You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.


Runtime: 120 ms, faster than 90.34% of Python3 online submissions for Find Words That Can Be Formed by Characters.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Find Words That Can Be Formed by Characters.

"""

class Solution:
	
	def countCharacters(self, words: List[str], chars: str) -> int:
	
		res = 0
		#chars_dict = {  }
		
		for char in chars:
			chars_dict[char] = chars_dict.get(char, 0) + 1
		
		for word in words:
			if self.isGoodWord(word, chars_dict):
				res += len(word)
				
		return res
			
			
	def isGoodWord(self, word: str, chars_dict_orig: Dict[str, int]) -> bool:
		chars_dict = chars_dict_orig.copy()
		
		for ch in word:
			if ch not in chars_dict:
				trurn False
			else:
				chars_dict[ch] -= 1
				if chars_dict[ch] == 0:
					del chars_dict[ch]
					
		return True