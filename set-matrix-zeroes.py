class Solution(object):
    
	
	"""
	solution 1
	O(n+m) space
	Runtime: 88 ms, faster than 95.25% of Python online submissions for Set Matrix Zeroes.
	"""
    def findPos(self, matrix): 
        res = []
        rows = [None] * len(matrix)
        cols = [None] * len(matrix[0])
        
        for i, row in enumerate(matrix):
            for j, item in enumerate(row):                
                if item == 0:
                    rows[i] = 1
                    cols[j] = 1
        return rows, cols
    
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """        

        if not matrix:
            return

        rows, cols = self.findPos(matrix)        
        
        for rowIdx, val in enumerate(rows):
            if val:
                for col in xrange(len(matrix[rowIdx])):            
                    matrix[rowIdx][col] = 0                
        
        for colIdx, val in enumerate(cols):
            if val:
                for row in matrix:
                    row[colIdx] = 0
					
	
	"""
	Solution 2
	O(1) space
	Runtime: 104 ms, faster than 44.20% of Python online submissions for Set Matrix Zeroes.
	"""
	
	    def setZeroesHelper(self, matrix):

        for rowIdx in xrange(len(matrix)):
            #print rowIdx, matrix[rowIdx]
            
            for colIdx in xrange(len(matrix[rowIdx])):
                
                if matrix[rowIdx][colIdx] == 0:
                    
                    if colIdx == 0 and rowIdx == 0:
                        matrix[0][0] = ('Set', 'Set')
                    
                    elif colIdx == 0 and type(matrix[0][0]) is int:
                        matrix[0][0] = (matrix[0][0], 'Set')
                        matrix[rowIdx][0] = 'Set'
                        
                    elif colIdx == 0 and type(matrix[0][0]) is not int:
                        matrix[0][0] = (matrix[0][0][0], 'Set')
                        matrix[rowIdx][0] = 'Set'
                        
                    elif rowIdx == 0:
                        matrix[0][colIdx] = 'Set'
                        if type(matrix[0][0]) is not int:
                            matrix[0][0] = ('Set', matrix[0][0][1])
                        else:
                            matrix[0][0] = ('Set', None)
                        
                    else:
                        matrix[0][colIdx] = 'Set'
                        matrix[rowIdx][0] = 'Set'
        
        
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """        
        if not matrix:
            return
        
        
        self.setZeroesHelper(matrix)
        
        for colIdx in xrange(len(matrix[0])-1, 0, -1):
            if matrix[0][colIdx] == 'Set':
                for row in matrix:
                    row[colIdx] = 0
                    
        for rowIdx in xrange(len(matrix)-1, 0, -1):
            if matrix[rowIdx][0] == 'Set':
                for col in xrange(len(matrix[rowIdx])):
                    matrix[rowIdx][col] = 0
                    
        if type(matrix[0][0]) is not int:
            rowIdx, colIdx = matrix[0][0]            
            if rowIdx and rowIdx == 'Set':
                matrix[0] = [0] * len(matrix[0])
            if colIdx and colIdx == 'Set':                
                for row in xrange(len(matrix)):
                    matrix[row][0] = 0
					
					
	"""
	Solution 2 / simplified
	O(1) space
	Runtime: 148 ms, faster than 20.74% of Python online submissions for Set Matrix Zeroes.
	"""
	
	    def setZeroesHelper(self, matrix):

        is1stColZeroes = False
        
        for rowIdx in xrange(len(matrix)):            
            for colIdx in xrange(len(matrix[rowIdx])):                
                if matrix[rowIdx][colIdx] == 0:
                    if colIdx == 0:
                        is1stColZeroes = True
                    else:
                        matrix[0][colIdx] = 0
                        matrix[rowIdx][0] = 0

        return is1stColZeroes
                    
        
        
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """        
        if not matrix:
            return
        
        
        is1stColZeroes = self.setZeroesHelper(matrix)
                    
        for rowIdx in xrange(1, len(matrix)):
            for colIdx in xrange(1, len(matrix[0])):
                if matrix[rowIdx][0] == 0 or matrix[0][colIdx] == 0:
                    matrix[rowIdx][colIdx] = 0
        
        if matrix[0][0] == 0:
            for colIdx in xrange(len(matrix[0])):
                matrix[0][colIdx] = 0
        
        if is1stColZeroes:
            for rowIdx in xrange(len(matrix)):
                matrix[rowIdx][0] = 0
				
				
				
				
################################
# TESTs

import unittest

class TestSolution(unittest.TestCase):
    
    def test_1(self):
        x =  [[1,0,1]]        
        out = [[0, 0, 0]]
        res = Solution().setZeroes(x)        
        self.assertEqual(x, out)
        
    def test_2(self):
        x =  [[1,1,1],[1,0,1],[1,1,1]]        
        out = [[1,0,1], [0,0,0], [1,0,1]]
        res = Solution().setZeroes(x)
        self.assertEqual(x, out)
        
    def test_3(self):
        x =  [[0,1,2,0],[3,4,5,2],[1,3,1,5]]        
        out = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        res = Solution().setZeroes(x)
        self.assertEqual(x, out)     
    
    

    def test_4(self):
        x =  [[1]]        
        out = [[1]]
        res = Solution().setZeroes(x)
        self.assertEqual(x, out)
        
    def test_5(self):
        x =  [[1,1,1],[0,1,2]]
        out = [[0,1,1],[0,0,0]]
        res = Solution().setZeroes(x)
        self.assertEqual(x, out)
        
    def test_6(self):
        x =  [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
        out = [[0,0,0,0],[0,0,0,4],[0,0,0,0],[0,0,0,3],[0,0,0,0]]
        res = Solution().setZeroes(x)
        self.assertEqual(x, out)
        
    def test_7(self):
        x =  [[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]
        out = [[0,0,0,0,0],[0,0,0,0,0],[2147483647,2,-9,-6,0]]
        res = Solution().setZeroes(x)
        self.assertEqual(x, out)
        
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
	
	