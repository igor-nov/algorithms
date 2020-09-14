"""
1371. Find the Longest Substring Containing Vowels in Even Counts


Solution 1
Time Limit Exceeded

Solution 2 -  modified solution 1
Runtime: 6960 ms, faster than 5.01% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
Memory Usage: 18.6 MB, less than 100.00% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.


Solution 3 - modified 3 - use internal method count to count vowels
Runtime: 240 ms, faster than 96.09% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
Memory Usage: 18.5 MB, less than 100.00% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.

Solution 4 - simplified 3
Runtime: 236 ms, faster than 96.56% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
Memory Usage: 18.7 MB, less than 100.00% of Python3 online submissions for Find the Longest Substring Containing
Runtime: 244 ms, faster than 95.00% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
Memory Usage: 18.5 MB, less than 100.00% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.


Solutions
[Python] Easy Sliding Window - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/531870/Python-Easy-Sliding-Window
"""


class Solution1:
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


class Solution2:
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


class Solution3:
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


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # move using sliding window
        # 0:n;
        # 0: n-1; 1:n
        # 0: n-2; 1: n-1; 2:n:
        # ....
        for window_size in range(len(s), -1, -1):
            for i in range(len(s) - window_size + 1):
                substring = s[i: i + window_size]
                print(f'start index: {i}, end index{i+window_size}, substring len: {window_size}, substring: {substring}')
                is_all_even = True
                for ch in 'aeiou':
                    if substring.count(ch) % 2:
                        is_all_even = False
                        break
                if is_all_even:
                    return window_size
        return 0



#####################
import unittest


class TestSolution(unittest.TestCase):

    # def test_1(self):
    #     inp = 'eleetminicoworoep'
    #     out = 13
    #     res = Solution().findTheLongestSubstring(inp)
    #     self.assertEqual(res, out)

    def test_2(self):
        inp = 'leetcodeisgreat'
        out = 5
        res = Solution().findTheLongestSubstring(inp)
        self.assertEqual(res, out)

    # def test_3(self):
    #     inp = 'bcbcbc'
    #     out = 6
    #     res = Solution().findTheLongestSubstring(inp)
    #     self.assertEqual(res, out)
    #
    #
    # def test_4(self):
    #     inp = 'id'
    #     out = 1
    #     res = Solution().findTheLongestSubstring(inp)
    #     self.assertEqual(res, out)
    #
    # def test_5(self):
    #     from testcases.find_the_longest__ import s_inp as test_inp
    #     inp = test_inp
    #     out = 499995
    #     res = Solution().findTheLongestSubstring(inp)
    #     self.assertEqual(res, out)
    #
    # def test_6(self):
    #     inp = 'a'
    #     out = 0
    #     res = Solution().findTheLongestSubstring(inp)
    #     self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
