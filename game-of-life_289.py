"""
289. Game of Life

Solution 1 - O(n*m) time, O(n*m) space using additional matrix
Runtime: 32 ms, faster than 56.22% of Python3 online submissions for Game of Life.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Game of Life.

Solution 2 - O(n*m) time, O(1) space ????? - I wouldn't agree with the solution for followup 1, that the space complexity is O(1).
Runtime: 32 ms, faster than 56.22% of Python3 online submissions for Game of Life.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Game of Life.


Solution
https://leetcode.com/problems/game-of-life/solution/

I wouldn't agree with the solution for followup 1, that the space complexity is O(1).
Why? It assumes that the cells are capable of holding integers, and not just True or False bits.
That is a really strong assumption, since why on earth would somebody implement these cells with two state

Infinite board solution - https://leetcode.com/problems/game-of-life/discuss/73217/Infinite-board-solution/201780
AC Python 40 ms solution O(mn) time O(1) extra space - https://leetcode.com/problems/game-of-life/discuss/73334/AC-Python-40-ms-solution-O(mn)-time-O(1)-extra-space
python 100% with explanation - https://leetcode.com/problems/game-of-life/discuss/174179/python-100-with-explanation

"""

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        board_tmp = [board[row][:] for row in range(len(board))]

        for row in range(len(board)):
            for col in range(len(board[0])):
                lives_around = self.get_lives(board_tmp, row, col)

                if board_tmp[row][col] and (lives_around < 2 or lives_around > 3):
                    board[row][col] = 0
                elif board[row][col] == 0 and lives_around == 3:
                    board[row][col] = 1

        #return board_new

    def get_lives(self, board, row, col):
        tmp = board[row][col]
        board[row][col] = 0

        top_r, bot_r = max(0, row - 1), min(len(board) - 1, row + 1)
        left_c, right_c = max(0, col - 1), min(len(board[0]) - 1, col + 1)

        res = 0
        for row_ in range(top_r, bot_r + 1):
            res += sum(board[row_][left_c:right_c + 1])

        board[row][col] = tmp
        return res


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:

        # -1 - was 1 previously - replace to 0
        # 2 - was 0 previously -> replace to 1
        for row in range(len(board)):
            for col in range(len(board[0])):
                lives_around = self.get_lives(board, row, col)
                if board[row][col] and (lives_around < 2 or lives_around > 3):
                    board[row][col] = -1
                elif board[row][col] == 0 and lives_around == 3:
                    board[row][col] = 2

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1

    def get_lives(self, board, row, col):
        tmp = board[row][col]
        board[row][col] = 0

        top_r, bot_r = max(0, row - 1), min(len(board) - 1, row + 1)
        left_c, right_c = max(0, col - 1), min(len(board[0]) - 1, col + 1)

        res = 0
        for row_ in range(top_r, bot_r + 1):
            res += sum([abs(val) for _, val in enumerate(board[row_][left_c:right_c + 1]) if val in (1, -1)])

        board[row][col] = tmp
        return res

"""
[
[0, -1, 0], 
[2, 0, 1], 
[-1, 1, 1], 
[0, 0, 0]
]

"""

#############
import unittest


class TestCase(unittest.TestCase):

    # def test1(self):
    #     inp = [
    #         [0, 1, 0],
    #         [0, 0, 1],
    #         [1, 1, 1],
    #         [0, 0, 0]
    #     ]
    #     out = [
    #         [0, 0, 0],
    #         [1, 0, 1],
    #         [0, 1, 1],
    #         [0, 1, 0]
    #     ]
    #     res = Solution().gameOfLife(inp)
    #     self.assertEqual(res, out)

    def test1(self):
        inp = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        out = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
        res = Solution().gameOfLife(inp)
        self.assertEqual(inp, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
