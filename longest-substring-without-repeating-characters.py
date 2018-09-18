class Solution(object):

    """ it's possible to return string in case if necessary"""
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_substring = []
        current_str = []
        start_idx = 0
        end_idx = 0

        for idx, ch in enumerate(s):

            end_idx = end_idx + 1

            if ch not in current_str:
                current_str.append(ch)

            else:
                if len(current_str) >= len(longest_substring):
                    longest_substring = current_str

                for start_idx_for_next_substring in range(start_idx, end_idx):
                    start_idx += 1
                    if s[start_idx_for_next_substring] == ch:
                        current_str = list(s[start_idx_for_next_substring+1:end_idx])
                        break

        return max(len(longest_substring), len(current_str))

    # solution 2
    # @todo optimize max_len = max(len(substring), max_len)
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = 0
        substring = set()
        max_len = 0

        for key, ch in enumerate(s):
            end += 1

            if ch not in substring:
                substring.add(ch)
            else:
                max_len = max(len(substring), max_len)
                for idx in range(start, end - 1):
                    start += 1
                    if s[idx] != ch:
                        substring.remove(s[idx])
                    else:
                        break

        max_len = max(len(substring), max_len)
        return max_len




### test cases - @todo - refactor it


#3
#input = 'abcabcbb'
#input = ' '
# 3
#input = 'pwwkew'
#input = 'bbbbb'
# 6
#input = 'bbtablud'
#input = 'aab'
# 3
#input = 'aabaab!bb'
#6
input = 'bpfbhmipx'
solution = Solution()
res = solution.lengthOfLongestSubstring(input)
print('res %s' % res)
