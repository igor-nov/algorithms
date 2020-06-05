"""
1400. Construct K Palindrome Strings

Solution 1
Runtime: 116 ms, faster than 16.67% of Python3 online submissions for Construct K Palindrome Strings.
Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Construct K Palindrome Strings.


Solutions
[Java/C++/Python] Straight Forward - https://leetcode.com/problems/construct-k-palindrome-strings/discuss/563379/JavaC%2B%2BPython-Straight-Forward
Python one liner, O(n), explanation -https://leetcode.com/problems/construct-k-palindrome-strings/discuss/563433/Python-one-liner-O(n)-explanation
2 Conditions Only - https://leetcode.com/problems/construct-k-palindrome-strings/discuss/563393/2-Conditions-Only

"""

from itertools import combinations, permutations

from functools import lru_cache
import numpy

class Solution:

    def canConstruct(self, s: str, k: int) -> bool:

        if len(s) == k:
            return True
        if len(s) < k:
            return False

        counts = {}
        for ch in s:
            counts[ch] = 1 if ch not in counts else counts[ch] + 1

        odd_counts = 0
        for ch, ch_count in counts.items():
            if ch_count % 2:
                odd_counts += 1

        return False if odd_counts > k else True



#############
import unittest


class TestCase(unittest.TestCase):
    #
    def test1(self):
        s = "annabelle"
        k = 2
        out = True
        res = Solution().canConstruct(s, k)
        self.assertEqual(res, out)

    def test2(self):
        s = "leetcode"
        k = 3
        out = False
        res = Solution().canConstruct(s, k)
        self.assertEqual(res, out)

    def test3(self):
        s = "true"
        k = 4
        out = True
        res = Solution().canConstruct(s, k)
        self.assertEqual(res, out)

    def test4(self):
        s = "yzyzyzyzyzyzyzy"
        k = 2
        out = True
        res = Solution().canConstruct(s, k)
        self.assertEqual(res, out)

    def test5(self):
        s = "cr"
        k = 7
        out = False
        res = Solution().canConstruct(s, k)
        self.assertEqual(res, out)

    def test6(self):
        s = "messi"
        k = 3
        out = True
        res = Solution().canConstruct(s, k)
        self.assertEqual(res, out)



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
