"""
Time: O(1)
Space: O(1), except data itself.

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
"""


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# two stacks, O(n) extra space
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.minstk = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stk.append(x)
        if not self.minstk or x <= self.minstk[-1]:
            self.minstk.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.minstk[-1] == self.stk.pop():
            self.minstk.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstk[-1]


# one stack, but same O(n) extra space.
class MinStack2(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.minval = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.minval:
            self.stk.append(self.minval)  # Everytime updating minval, push last minval.
            self.minval = x
        self.stk.append(x)

    def pop(self):
        """
        :rtype: void
        """
        # Everytime poping minval, updating minval back to last minval,
        # and remove last minval from stack.
        if self.stk.pop() == self.minval:
            self.minval = self.stk[-1]
            self.stk.pop()  # remove last minval

    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minval


# 1 stack and O(1) extra space!
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.minval = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stk:
            self.stk.append(0)
            self.minval = x
        else:
            self.stk.append(x-self.minval)
            if x < self.minval:  # pushed new_min - last_min
                self.minval = x

    def pop(self):
        """
        :rtype: void
        """
        p = self.stk.pop()
        if p < 0:  # top is new_min
            self.minval -= p  # restore last_min = new_min - (new_min - last_min)

    def top(self):
        """
        :rtype: int
        """
        top = self.stk[-1]
        if top > 0:
            return top + self.minval
        else:  # top is new_min
            return self.minval

    def getMin(self):
        """
        :rtype: int
        """
        return self.minval
