'''
Design a stack that supports increment operations on its elements.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum 
number of elements in the stack.
void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
int pop() Pops and returns the top of the stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. 
If there are less than k elements in the stack, increment all the elements in the stack.

'''

class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = [-1]*maxSize
        self.top = -1

    def isFull(self):
        if self.top == self.size -1:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False


    def push(self, x: int) -> None:
        if self.isFull():
            return
        else:
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            res = self.stack[self.top]
            self.top -= 1
            return res

    def increment(self, k: int, val: int) -> None:
        if self.isEmpty():
            return
        endIndex = min(k, self.top + 1)
        for i in range(0, endIndex):
            self.stack[i] += val




# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)