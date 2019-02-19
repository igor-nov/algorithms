"""
134. Gas Station

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.

------------
Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

-------------
Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.


Solutions:
https://leetcode.com/problems/gas-station/discuss/42578/Easy-and-simple-proof-with-Python-solution.
https://leetcode.com/problems/gas-station/discuss/206911/Python-beats-100-with-explanation-and-plots
https://leetcode.com/problems/gas-station/discuss/42568/Share-some-of-my-ideas.,
https://leetcode.com/problems/gas-station/discuss/42572/Proof-of-%22if-total-gas-is-greater-than-total-cost-there-is-a-solution%22.-C%2B%2B
comment from - https://leetcode.com/problems/gas-station/discuss/42648/My-one-pass-solution.
https://leetcode.com/problems/gas-station/discuss/42661/Possibly-the-MOST-easiest-approach-O(N)-one-variable-Python

"""


"""
Runtime: 20 ms, faster than 100.00% of Python online submissions for Gas Station.
Memory Usage: 11.2 MB, less than 100.00% of Python online submissions for Gas Station.
"""
class Solution(object):
    
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        totalGas = 0
        currentGas = 0
        position = 0
        
        for pointIdx, pointGas in enumerate(gas):
            
            if pointGas + currentGas < cost[pointIdx]:
                position = pointIdx + 1
                currentGas = 0
            else:
                currentGas += pointGas - cost[pointIdx]
                
            totalGas += pointGas - cost[pointIdx]
            
        if totalGas >= 0:
            return position
        else:
            return -1
			
"""
Runtime: 2512 ms, faster than 3.84% of Python online submissions for Gas Station.
Memory Usage: 11.1 MB, less than 100.00% of Python online submissions for Gas Station.
"""
class Solution2(object):
    
    def canMoveNext(self, gas, cost):
        return gas >= cost
    
    def canCompleteHelper(self, gas, cost, startFromIdx):
        
        currentIdx = startFromIdx
        currentGas = gas[currentIdx]
        
        steps = len(gas)
        maxIdx = steps - 1
        
        while steps > 1:
            
            if currentIdx < maxIdx:
                nextStepIdx = currentIdx + 1
            else:
                nextStepIdx = 0
            
            if currentGas >= cost[currentIdx]:
                currentGas = currentGas + gas[nextStepIdx] - cost[currentIdx]
            else:
                return False
                
            currentIdx = nextStepIdx            
            steps -= 1
            
        return currentGas - cost[currentIdx] >= 0
    
    
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """        
        for pointIdx, pointGas in enumerate(gas):            
            if self.canMoveNext(pointGas, cost[pointIdx]) and self.canCompleteHelper(gas, cost, pointIdx):
                return pointIdx
            
        return -1
		
#############################################################	
import unittest


class TestSolution(unittest.TestCase):

                
    def test_1(self):
        out = 3
        gas  = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        res = Solution().canCompleteCircuit(gas, cost)
        self.assertEqual(res, out)
        
    def test_2(self):
        out = -1
        gas  = [2,3,4]
        cost = [3,4,3]
        res = Solution().canCompleteCircuit(gas, cost)
        self.assertEqual(res, out)
        
    def test_3(self):
        out = 4
        gas  = [5,1,2,3,4]
        cost = [4,4,1,5,1]
        res = Solution().canCompleteCircuit(gas, cost)
        self.assertEqual(res, out)
        
    def test_4(self):
        out = 6
        gas  = [1,2,3,4,5,5,70]
        cost = [2,3,4,3,9,6,2]
        res = Solution().canCompleteCircuit(gas, cost)
        self.assertEqual(res, out)
   
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
