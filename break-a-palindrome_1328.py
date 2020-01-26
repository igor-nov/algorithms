"""
1328. Break a Palindrome

Solution 1
Runtime: 20 ms, faster than 100.00% of Python3 online submissions for Break a Palindrome.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Break a Palindrome.

Solution 2
Runtime: 28 ms, faster than 100.00% of Python3 online submissions for Break a Palindrome.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Break a Palindrome.

Solutions
[Java/C++/Python] Easy and Concise
https://leetcode.com/problems/break-a-palindrome/discuss/489774/JavaC%2B%2BPython-Easy-and-Concise

Python brute force
https://leetcode.com/problems/break-a-palindrome/discuss/489891/Python-brute-force

[C++] Greedy
https://leetcode.com/problems/break-a-palindrome/discuss/489722/C%2B%2B-Greedy

Clean Python 3 three lines
https://leetcode.com/problems/break-a-palindrome/discuss/489748/Clean-Python-3-three-lines

"""


class Solution:

    def is_palindrome(self, string):
        st = 0
        while st < len(string) // 2:
            if string[st] != string[len(string) - st - 1]:
                return False
            st += 1
        return True

    def breakPalindrome(self, palindrome: str) -> str:
        if not palindrome or len(palindrome) == 1:
            return ''

        # 1 check before
        # b -> a , c -> a b
        for i, ch in enumerate(palindrome):
            replace_ch = 'a'
            while replace_ch < ch:
                next_replacement = palindrome[0:i] + replace_ch + palindrome[i + 1:]
                # print(next_replacement, replace_ch)
                if not self.is_palindrome(next_replacement):
                    return next_replacement
                replace_ch = chr(ord(replace_ch) + 1)
                # print(replace_ch)

        # check after
        # b -> c,d,e...z
        for i in range(len(palindrome) - 1, -1, -1):
            replace_ch = chr(ord(palindrome[i]) + 1)
            while replace_ch <= 'z':
                next_replacement = palindrome[0:i] + replace_ch + palindrome[i + 1:]
                # print(next_replacement, replace_ch)
                if not self.is_palindrome(next_replacement):
                    return next_replacement
                replace_ch = chr(ord(replace_ch) + 1)
        return ''


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]

        return palindrome[:-1] + 'b' if len(palindrome) > 1 else ''


#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = 'abccba'
        out = 'aaccba'
        res = Solution().breakPalindrome(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = 'a'
        out = ''
        res = Solution().breakPalindrome(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = 'aba'
        out = 'abb'
        res = Solution().breakPalindrome(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
