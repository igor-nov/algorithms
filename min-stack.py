"""
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

Solutions:
Implement A Max Stack - A Stack With A .max() API (Similar To "Min Stack" on LeetCode) - https://www.youtube.com/watch?v=nGwn8_-6e7w
Java / Python Utility Stack with Thinking Process - https://leetcode.com/problems/min-stack/discuss/209587/Java-Python-Utility-Stack-with-Thinking-Process
My Python solution - https://leetcode.com/problems/min-stack/discuss/49022/My-Python-solution
"""


"""
Runtime: 48 ms, faster than 86.06% of Python online submissions for Min Stack.
Memory Usage: 14.9 MB, less than 8.67% of Python online submissions for Min Stack.
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack):
            current_min = min(self.stack[-1][1], x)
        else:
            current_min = x    
            
        self.stack.append((x, current_min))
        

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack):
            #last_element = self.stack.pop()
            #return last_element[0]
            return self.stack.pop()[0]
        else:
            return None

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack):
            return self.stack[-1][0]
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack):
            return self.stack[-1][1]
        else:
            return None
			
			
#### Solution 2 - implement LIFO
class Node(object):    
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LIFO(object):
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def append(self, val):
        new_node = Node(val)
        
        if not self.is_empty():
            new_node.next = self.head
            
        self.head = new_node
        
    def top(self):
        return self.head.val
    
    def pop(self):
        element = self.head
        self.head = element.next
        return element.val

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = LIFO()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack.is_empty():
            current_min = min(self.stack.top()[1], x)
        else:
            current_min = x    
            
        self.stack.append((x, current_min))
        
    def pop(self):
        """
        :rtype: None
        """
        if not self.stack.is_empty():
            return self.stack.pop()[0]
        else:
            return None

    def top(self):
        """
        :rtype: int
        """
        if not self.stack.is_empty():
            return self.stack.top()[0]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack.is_empty():
            return self.stack.top()[1]
        else:
            return None
        
		
### Solution 3 - optimized space - uses separate stack for min values
"""
Runtime: 48 ms, faster than 86.06% of Python online submissions for Min Stack.
Memory Usage: 14.5 MB, less than 81.63% of Python online submissions for Min Stack.
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.minStack):
            if self.minStack[-1][0] == x:
                self.minStack[-1][1] += 1
            elif self.minStack[-1][0] > x:
                self.minStack.append([x, 1])
        else:
            self.minStack.append([x, 1])
            
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack):
            val = self.stack.pop()
            
            if val == self.minStack[-1][0]:
                self.minStack[-1][1] -= 1
                if self.minStack[-1][1] == 0:
                    self.minStack.pop()
                    
            return val
        
        else:
            return None

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack):
            return self.stack[-1]
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minStack):
            return self.minStack[-1][0]
        else:
            return None

##################################################
minStack = MinStack()
minStack.push(-2)
print '{} top -2'.format(minStack.top())

minStack.push(0)
print '{} top 0'.format(minStack.top())

minStack.push(-3)
print '{} top -3'.format(minStack.top())

print minStack.getMin()#   --> Returns -3.

minStack.pop()
print '{}  0'.format(minStack.top())#      --> Returns 0.
minStack.pop()
print minStack.top()# 
print 'min' , minStack.getMin()#   --> Returns -2.