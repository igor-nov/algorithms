"""
1371. Find the Longest Substring Containing Vowels in Even Counts

#####################
Optimized brute force

Solutions
[Python] Easy Sliding Window - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/531870/Python-Easy-Sliding-Window

[Python] Solution Sliding Window (Easy to Read)
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/578071/Python-Solution-Sliding-Window-(Easy-to-Read)

#####################
O(n)

C++/Java with picture
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/534135/C%2B%2BJava-with-picture

Dew It | Simple illustration for THE trick
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/534210/Dew-It-or-Simple-illustration-for-THE-trick

[Python] solution in O(n) time and O(1) space explained
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/531850/Python-solution-in-O(n)-time-and-O(1)-space-explained

[Java] o(n) one pass solution. Easy to understand.
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/532101/Java-o(n)-one-pass-solution.-Easy-to-understand.

"""


"""
Runtime: 7996 ms, faster than 5.04% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
Memory Usage: 19.5 MB, less than 45.87% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
"""
class Solution1:

    def is_even(self, needed:dict) -> bool:
        for val in needed.values():
            if val:
                return False
        return True

    def findTheLongestSubstring(self, s: str) -> int:
        needed = {'a': 0 , 'e': 0, 'i': 0, 'o': 0, 'u':0 }
        max_len = 0
        for end in range(len(s)):

            if s[end] in needed:
                needed[s[end]] = not needed[s[end]]

            if self.is_even(needed):
                max_len = max(max_len, end+1)


            st = 0
            needed_tmp = needed.copy()
            while st < end:
                if end-st < max_len:
                    break
                if s[st] in needed:
                    needed[s[st]] = not needed[s[st]]
                if self.is_even(needed):
                    max_len = max(max_len, end-st)
                st += 1

            needed = needed_tmp.copy()

        return max_len


"""
Time Limit Exceeded
"""
from functools import lru_cache
class Solution2:

    @lru_cache(None)
    def is_even_str(self, str):
        needed = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        for ch in str:
            if ch in needed:
                needed[ch] = not needed[ch]
        for val in needed.values():
            if val:
                return False
        return True


    def findTheLongestSubstring(self, s: str) -> int:

        max_len = 0
        for end in range(len(s)):

            if self.is_even_str(s[:end+1]):
                max_len = max(max_len, end+1)

            st = 0
            while st < end:
                if end-st < max_len:
                    break
                if self.is_even_str(s[st+1:end+1]):
                    max_len = max(max_len, end-st)
                st += 1

        return max_len



"""
Time Limit Exceeded
"""
class Solution3:
    def findTheLongestSubstring(self, s: str) -> int:
        substrings = self.generate_subst(s)
        res = 0
        for substring in substrings:
            if self.is_appropr_substring(substring):
                res = max(res, len(substring))
        return res

    def is_appropr_substring(self, s: str):
        vowels = {
            'a': 0,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0
        }
        for ch in s:
            if ch in vowels:
                vowels[ch] += 1

        for ch, count in vowels.items():
            if count % 2:
                return False
        return True

    def generate_subst(self, s: str):
        res = set()
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                res.add(s[i:j])
        return res

"""
Solution 4 -  modified solution 3
Runtime: 6960 ms, faster than 5.01% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
Memory Usage: 18.6 MB, less than 100.00% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
"""

class Solution4:
    def findTheLongestSubstring(self, s: str) -> int:
        substrings = self.generate_subst(s)
        res = 0
        for substring in substrings:
            if self.is_appropr_substring(substring):
                return len(substring)
        return res

    def is_appropr_substring(self, s: str):
        vowels = {
            'a': 0,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0
        }
        for ch in s:
            if ch in vowels:
                vowels[ch] += 1

        for ch, count in vowels.items():
            if count % 2:
                return False
        return True

    def generate_subst(self, s: str):
        for window_size in range(len(s), -1, -1):
            for i in range(len(s) - window_size + 1):
                yield s[i: i+window_size]

"""
Solution 5 - modified 3 - use internal method count to count vowels
Runtime: 240 ms, faster than 96.09% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
Memory Usage: 18.5 MB, less than 100.00% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
"""

class Solution5:
    def findTheLongestSubstring(self, s: str) -> int:
        substrings = self.generate_subst(s)
        res = 0
        for substring in substrings:
            is_all_even = True
            for ch in 'aeiou':
                if substring.count(ch) % 2:
                    is_all_even = False
                    break
            if is_all_even:
                return len(substring)

        return res

    def generate_subst(self, s: str):
        for window_size in range(len(s), -1, -1):
            for i in range(len(s) - window_size + 1):
                yield s[i: i+window_size]

"""
Solution 6 - simplified 5
Runtime: 236 ms, faster than 96.56% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
Memory Usage: 18.7 MB, less than 100.00% of Python3 online submissions for Find the Longest Substring Containing
Runtime: 244 ms, faster than 95.00% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
Memory Usage: 18.5 MB, less than 100.00% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.

"""
class Solution6:
    def findTheLongestSubstring(self, s: str) -> int:
        # move using sliding window
        # 0:n;
        # 0: n-1; 1:n
        # 0: n-2; 1: n-1; 2:n:
        # ....
        for window_size in range(len(s), -1, -1):
            for i in range(len(s) - window_size + 1):
                substring = s[i: i + window_size]
                #print(f'start index: {i}, end index{i+window_size}, substring len: {window_size}, substring: {substring}')
                is_all_even = True
                for ch in 'aeiou':
                    if substring.count(ch) % 2:
                        is_all_even = False
                        break
                if is_all_even:
                    return window_size
        return 0


class Solution7:
    def findTheLongestSubstring(self, s: str) -> int:

        for window_size in range(len(s), -1, -1):
            end_pos = len(s) - window_size + 1
            for i in range(end_pos):
                substring = s[i: i+ window_size]
                is_all_even = True
                for ch in 'aeiou':
                    if substring.count(ch) % 2:
                        is_all_even = False
                        break
                if is_all_even:
                    return window_size
        return 0

"""
Runtime: 500 ms, faster than 61.94% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
Memory Usage: 19.5 MB, less than 43.47% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
"""
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        masks = {0: -1}
        mask = 0
        match = {
            'a' : 1,
            'e' : 2,
            'i' : 4,
            'o' : 8,
            'u': 16
        }
        max_len = 0
        for i, ch in enumerate(s):
            if ch in match:
                mask = mask ^ (1 << match[ch])
            if mask in masks:
                max_len = max(max_len, i - masks[mask])
            else:
                masks[mask] = i
        return max_len

#####################
import unittest


class TestSolution(unittest.TestCase):

    def test_1(self):
        inp = 'eleetminicoworoep'
        out = 13
        res = Solution().findTheLongestSubstring(inp)
        self.assertEqual(out, res)

    def test_2(self):
        inp = 'leetcodeisgreat'
        out = 5
        res = Solution().findTheLongestSubstring(inp)
        self.assertEqual(res, out)

    def test_3(self):
        inp = 'bcbcbc'
        out = 6
        res = Solution().findTheLongestSubstring(inp)
        self.assertEqual(res, out)


    def test_4(self):
        inp = 'id'
        out = 1
        res = Solution().findTheLongestSubstring(inp)
        self.assertEqual(res, out)

    def test_6(self):
        inp = 'a'
        out = 0
        res = Solution().findTheLongestSubstring(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
