"""
Runtime: 44 ms, faster than 91.20% of Python online submissions for Valid Sudoku.

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

-Each row must contain the digits 1-9 without repetition.
-Each column must contain the digits 1-9 without repetition.
-Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Examples
https://www.youtube.com/watch?v=i2YKwM9oCcY
https://leetcode.com/problems/valid-sudoku/discuss/15472/Short%2BSimple-Java-using-Strings
https://leetcode.com/problems/valid-sudoku/discuss/15715/AC-concise-Python-code
https://leetcode.com/problems/valid-sudoku/discuss/15509/Clean-and-Easy82ms-Python
https://leetcode.com/problems/valid-sudoku/discuss/15460/1-7-lines-Python-4-solutions
"""
class Solution(object):
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #appearances = {}
        apRow = {}
        apCol = {}
        apCeil = {}
        
        for row in xrange(9):
            if row not in apRow:
                apRow[row] = {}
            
            for col in xrange(9):
                ceil = 3*(row/3) + col/3
                
                if ceil not in apCeil:
                    apCeil[ceil] = {}
                
                if col not in apCol:
                    apCol[col] = {}
                
                if board[row][col] != '.':
                    
                    if board[row][col] in apRow[row] or (
                        board[row][col] in apCol[col]) or (
                        board[row][col] in apCeil[ceil]):
                        return False
                    
                    apRow[row][board[row][col]] = [row, col]
                    apCol[col][board[row][col]] = [row, col]
                    apCeil[ceil][board[row][col]] = [ceil]
                    
        return True 
    
    #using set
    def isValidSudokuSet(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #appearances        
        app = set()
        
        for row in xrange(9):            
            for col in xrange(9):
                
                ceil = 3*(row/3) + col/3
                
                if board[row][col] != '.':
                    
                    
                    if  'r%s-%s' % (row, board[row][col]) in app or (
                        'c%s-%s' % (col, board[row][col]) in app) or (
                        '%s-%s' % (ceil, board[row][col]) in app ): #!!!!
                        #print app , 'r%s-%s' % (row, board[row][col]), '%s-%s' % (board[row][col], col), '%s-%s' % (ceil, board[row][col])
                        return False                        
                    
                    app.add('r%s-%s' % (row, board[row][col]))                    
                    app.add('c%s-%s' % (col,board[row][col]))                    
                    app.add('%s-%s' % (ceil, board[row][col]))
                                        
        return True 
    
    #using bit manipulations
    def isValidSudokuBit(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        #appearances
        aRow = [0 for i in xrange(9)]
        aCol = [0 for i in xrange(9)]
        aCeil = [0 for i in xrange(9)]
        
        for row in xrange(9):            
            for col in xrange(9): 
                if board[row][col] != '.':                    
                    val = 1 << int(board[row][col]) - 1
                    print bin(val)
                    
                    ceil = row/3 * 3 + col/3
                    
                    if val & aRow[row] or val & aCol[col] or val & aCeil[ceil]:
                        return False
                    
                    
                    aRow[row] = aRow[row] | val
                    aCol[col] = aCol[col] | val
                    aCeil[ceil] = aCeil[ceil] | val
                    
                    print aCeil[ceil]
                
        return True
                    
                
                    
                
        
board = [
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".","9","."],
    [".",".",".","5","6",".",".",".","."],
    ["4",".","3",".",".",".",".",".","1"],
    [".",".",".","7",".",".",".",".","."],
    [".",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]

board = [
  ["8","8","8",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
] #false

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
] #true

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".","3","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
] #true

board = [
	[".",".","4",".",".",".","6","3","."],
	[".",".",".",".",".",".",".",".","."],
	["5",".",".",".",".",".",".","9","."],
	[".",".",".","5","6",".",".",".","."],
	["4",".","3",".",".",".",".",".","1"],
	[".",".",".","7",".",".",".",".","."],
	[".",".",".","5",".",".",".",".","."],
	[".",".",".",".",".",".",".",".","."],
	[".",".",".",".",".",".",".",".","."]
]
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
res = Solution().isValidSudoku(board)
print 'res = %s' % res