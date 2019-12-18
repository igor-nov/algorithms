"""
First Missing Positive

Runtime: 24 ms, faster than 61.46% of Python online submissions for First Missing Positive. (for solution 2)


Examples 
http://n00tc0d3r.blogspot.com/2013/03/find-first-missing-positive.html
https://www.cnblogs.com/EdwardLiu/p/3811206.html




"""


class Solution(object):

    # Solution 1
    # O(n) time, O(n) space
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = set()
        lo = 1

        for k, v in enumerate(nums):
            if v == lo:
                while True:
                    lo += 1
                    if lo not in tmp:
                        break
            elif lo < v:
                tmp.add(v)

        return lo


class Solution(object):
    # Solution 2
    # O(n) time, O(1) space
    def firstMissingPositive(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        numsLen = len(nums)

        if not numsLen:
            return 1

        i = 0
        while i < numsLen:
            # nums[i] = x ==>> put=>> nums[x-1] = x

            # original=>	[3, 4, -1, 1]
            # step 1	=>	[-1, 4, 3, 1]
            #			[-1, 4, 3, 1]
            # step 2	=>	[-1, 1, 3, 4]
            #           [1, -1, 3, 4]
            #
            # all in place - nothing to change
            # step 3	=>	[1, -1, 3, 4]
            #			[1, -1, 3, 4]
            #
            # step 4 =>	[1, -1, 3, 4] - final res

            if nums[i] > 0 and nums[i] <= numsLen and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        # print nums
        i = 0
        while i < numsLen and nums[i] == i + 1:
            i += 1

        return i + 1
