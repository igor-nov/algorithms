"""
929. Unique Email Addresses

Solution 3
Runtime: 64 ms, faster than 25.85% of Python3 online submissions for Unique Email Addresses.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Unique Email Addresses.

Solution 4
Runtime: 40 ms, faster than 98.33% of Python3 online submissions for Unique Email Addresses.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Unique Email Addresses.
"""

from typing import List
class Solution1:
    def numUniqueEmails(self, emails: List[str]) -> int:

        unique_emails = set()
        for email in emails:
            unique_emails.add(self.format_email(email))
        return len(unique_emails)

    def format_email(self, email):
        prefix, domain = email.split('@')
        final_email = []
        for ch in prefix:
            if ch == '+':
                break
            if ch == '.':
                continue
            final_email.append(ch)

        final_email = final_email + ['@'] + [domain]
        return ''.join(final_email)


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        unique_emails = set()
        for email in emails:
            unique_emails.add(self.format_email(email))
        return len(unique_emails)


    def format_email(self, email):
        final_email = []
        isDone = False
        for i, ch in enumerate(email):
            if ch == '@':
                final_email.append(email[i:])
                break
            elif ch == '.' or isDone:
                continue
            elif ch == '+':
                isDone = True
                continue
            else:
                final_email.append(ch)

        return ''.join(final_email)


class Solution3:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            prefix_raw, domain = email.split('@')
            prefix = []
            for ch in prefix_raw:
                if ch == '+':
                    break
                if ch == '.':
                    continue
                else:
                    prefix.append(ch)
            unique_emails.add(''.join(prefix) + '@' + domain)
        return len(unique_emails)



class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            prefix, domain = email.split('@')
            unique_emails.add(''.join(prefix.split('+')[0].split('.')) + '@' + domain)
        return len(unique_emails)

import unittest


class TestCase(unittest.TestCase):
    # @unittest.skip
    def test1(self):
        inp = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
        out = 2
        res = Solution().numUniqueEmails(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com",
               ".t.est.email+david@lee.tcode.com"]
        out = 2
        res = Solution().numUniqueEmails(inp)
        self.assertEqual(res, out)



    def test3(self):
        inp = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
        out = 2
        res = Solution().numUniqueEmails(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
