"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""

import queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #self.que1 = queue.Queue()
        #self.que2 = queue.Queue()
        self.que = queue.Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        #self.que1.put(x)
        tmp = queue.Queue()
        while not self.que.empty():
            tmp.put(self.que.get())
        self.que.put(x)
        while not tmp.empty():
            self.que.put(tmp.get())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        """
        while self.que1.qsize() > 1:
            self.que2.put(self.que1.get())
        res = self.que1.get()
        self.que1, self.que2 = self.que2, self.que1
        return res
        """
        return self.que.get()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        """
        while self.que1.qsize() > 1:
            self.que2.put(self.que1.get())
        res = self.que1.get()
        self.que1, self.que2 = self.que2, self.que1
        self.que1.put(res)
        return res
        """
        res = self.que.get()
        tmp = queue.Queue()
        tmp.put(res)
        while not self.que.empty():
            tmp.put(self.que.get())
        self.que, tmp = tmp, self.que
        return res

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        #return self.que1.empty()
        return self.que.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()