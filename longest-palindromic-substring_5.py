"""
Longest Palindromic Substring

@todo - O(N) Manacher's Algorithm
Manacher's Algorithm | Code Tutorial and Explanation - https://www.youtube.com/watch?v=kbUiR5YWUpQ
https://www.youtube.com/watch?v=V-sEwsca1ak
https://www.youtube.com/watch?v=nbTSfrEfo6M

Solution - just redu
Runtime: 2924 ms, faster than 39.58% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 20.5 MB, less than 14.29% of Python3 online submissions for Longest Palindromic Substring.

Solution1 - time limit exceeded

Solution2 - Runtime: 4236 ms, faster than 30.43% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 22.6 MB, less than 5.04% of Python3 online submissions for Longest Palindromic Substring.

solution3 - Runtime: 3748 ms, faster than 34.97% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 22.6 MB, less than 5.04% of Python3 online submissions for Longest Palindromic Substring.

solution4 same but without zip - Runtime: 3540 ms, faster than 36.72% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 22.7 MB, less than 5.04% of Python3 online submissions for Longest Palindromic Substring.


Solutions:
LONGEST PALINDROME SUB STRING WITH DYNAMIC PROGRAMMING - https://www.youtube.com/watch?v=Fi5INvcmDos

https://www.youtube.com/watch?v=obBdxeCx_Qs
https://www.youtube.com/watch?v=0xeBqanD5GQ
https://www.youtube.com/watch?v=HBtiDHIOK9A
https://www.youtube.com/watch?v=V-sEwsca1ak

https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

O(N) Manacher's Algorithm
https://www.youtube.com/watch?v=V-sEwsca1ak
https://www.youtube.com/watch?v=nbTSfrEfo6M

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        dp = [[0] * len(s) for _ in range(len(s))]
        max_pal = ""

        for i in range(len(s)):
            dp[i][i] = 1
            max_pal = s[i]

        # len2
        # for i in range(1, len(s)):
        #     if s[i] == s[i-1]:
        #         dp[i-1][i] = 1
        #         max_pal = s[i-1:i+1]

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                max_pal = s[i:i + 2]

        # for row in dp:
        #     print(row)

        # len 3...n
        for sub_len in range(2, len(s)):
            for start in range(len(s) - sub_len):
                end = sub_len + start
                if s[start] == s[end] and dp[start + 1][end - 1]:
                    dp[start][end] = 1
                    if len(max_pal) < end - start + 1:
                        max_pal = s[start:end + 1]

        return max_pal

class Solution1:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ''

        max_palindrome = ''

        for i in range(len(s)):
            for j in range(len(s) + 1, i, -1):
                if self.getPalindrome(s, i, j) and len(max_palindrome) < len(s[i:j]):
                    max_palindrome = s[i:j]

        return max_palindrome

    def getPalindrome(self, s, lo, hi):
        # print(s[lo:hi])
        if s[lo:hi] == s[lo:hi][::-1]:
            return True
        return False


class Solution2:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ''

        len_s = len(s)
        # dp = [False for _ in range(len_s)] * for _ in range(len_s)
        dp = [[False for _ in range(len_s)] for _ in range(len_s)]
        pal = s[0]

        # set diagonal
        for i in range(len_s):
            dp[i][i] = True

        # find palindrome for length 2
        for i in range(0, len_s - 1):
            print(i, i + 2, s[i:i + 2])
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                if len(pal) < len(s[i:i + 2]):
                    pal = s[i:i + 2]

        # find palindrome strin > 2
        for len_ in range(2, len_s):
            for i in range(0, len(s) - len_):
                j = i + len_
                print(i, j, s[i:j + 1])
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if len(pal) < len(s[i:j + 1]):
                        pal = s[i:j + 1]

        return pal


class Solution3:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ''

        start = 0
        max_len = 1
        len_s = len(s)
        dp = [[None for _ in range(len_s)] for _ in range(len_s)]

        # set True to diagonal
        for i, j in zip(range(len_s), range(len_s)):
            dp[i][j] = True

        # loop through len 2
        for i in range(len_s - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2
                # print(start, max_len)

        # loop through len > 2
        for len_ in range(3, len_s + 1):

            for i in range(0, len_s - len_ + 1):
                j = i + len_ - 1
                # print(i,j, len_, s[i:j+1])
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True

                    if max_len <= len_:
                        max_len = len_
                        start = i
                        # print(start, max_len)
        # print(start, max_len)
        return s[start:start + max_len]


class Solution3:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ''

        start = 0
        max_len = 1
        len_s = len(s)
        dp = [[None for _ in range(len_s)] for _ in range(len_s)]

        # set True to diagonal
        for i in range(len_s):
            dp[i][i] = True

        # loop through len 2
        for i in range(len_s - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2
                # print(start, max_len)

        # loop through len > 2
        for len_ in range(2, len_s):

            for i in range(0, len_s - len_):
                j = i + len_
                # print(i,j, len_, s[i:j+1])
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True

                    if max_len <= len_:
                        max_len = len_ + 1
                        start = i
                        # print(start, max_len)
        # print(start, max_len)
        return s[start:start + max_len]



#
# class Solution(object):
#
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#
#         isPalM = [[None for i in xrange(len(s))] for i in xrange(len(s))]
#
#         lt = gt = 0
#         for j in xrange(1, len(s)):
#             for i in xrange(0, j):
#                 isPal = isPalM[i+1][j-1] or j-i <= 2
#                 if isPal and s[i] == s[j]:
#                     isPalM[i][j] = True
#                     if gt - lt < j - i:
#                         lt, gt = i, j
#
#         return s[lt:gt+1]
#
#     def longestPalindrome2(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#
#         palMtrx = [[None for i in xrange(len(s))] for i in xrange(len(s))]
#
#
#         lt = gt = 0
#
#         for i in xrange(0, len(s)):
#             palMtrx[i][i] = True
#
#         for i in xrange(1, len(s)):
#             if s[i-1] == s[i]:
#                 palMtrx[i-1][i] = True
#                 lt, gt = i-1, i
#
#         for w in xrange(2, len(s)):
#             for i in xrange(0, len(s)-w):
#                 j = i + w
#                 isPal = palMtrx[i+1][j-1] and s[i] == s[j]
#                 if isPal:
#                     palMtrx[i][j] = True
#
#                     if gt - lt < j - i:
#                         lt, gt = i, j
#
#         return s[lt:gt+1]

#############
import unittest


# @unittest.skip
class TestCase(unittest.TestCase):

    # @unittest.skip
    def test1(self):
        inp = 'babad'
        out = 'aba'
        out = 'bab'
        res = Solution().longestPalindrome(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = 'babadweqw'
        out = 'aba'
        out = 'bab'
        res = Solution().longestPalindrome(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = 'bba'
        out = 'bb'
        res = Solution().longestPalindrome(inp)
        self.assertEqual(res, out)

    def test4(self):
        inp = 'cbbd'
        out = 'bb'
        res = Solution().longestPalindrome(inp)
        self.assertEqual(res, out)

    def test5(self):
        inp = 'ccc'
        out = 'ccc'
        res = Solution().longestPalindrome(inp)
        self.assertEqual(res, out)

    def test6(self):
        inp = 'bb'
        out = 'bb'
        res = Solution().longestPalindrome(inp)
        self.assertEqual(res, out)

    def test7(self):
        inp = 'b'
        out = 'b'
        res = Solution().longestPalindrome(inp)
        self.assertEqual(res, out)

    def test8(self):
        inp = "abcba"
        out = "abcba"
        res = Solution().longestPalindrome(inp)
        self.assertEqual(res, out)

    def test9(self):
        inp = "caba"
        out = "aba"
        res = Solution().longestPalindrome(inp)
        self.assertEqual(res, out)

    def test91(self):
        inp = "eabcb"
        out = "bcb"
        res = Solution().longestPalindrome(inp)
        self.assertEqual(res, out)

    def test91(self):
        inp = ""
        out = ""
        res = Solution().longestPalindrome(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
