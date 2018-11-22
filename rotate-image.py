"""
Rotate Image (https://leetcode.com/problems/rotate-image/)

You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Examples:
https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image !!!
https://leetcode.com/problems/rotate-image/discuss/19123/6-lines-of-code-and-with-O(1)-space-in-c%2B%2B

https://www.youtube.com/watch?v=Jtu6dJ0Cb94 !!!
https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)

"""


class Solution(object):
    
    def reverseM(self, m):
        mH = len(m) - 1        
        for row in xrange(mH):
            if mH - row > row:
                m[row], m[mH - row] = m[mH - row], m[row]
                
    def swap(self, m):        
        for i in xrange(len(m)):            
            for j in xrange(i+1,len(m)):                                
                m[i][j], m[j][i] = m[j][i], m[i][j]
            
    def rotate(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """        
        self.reverseM(m)
        self.swap(m)        
                

matrix =[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

matrix = [[0,1], [2,3]]
matrix = [[0,1,2], [3,4,5], [6,7,8]]

for row in matrix:
    print row
    
print '------'

Solution().rotate(matrix)

for row in matrix:
    print row

