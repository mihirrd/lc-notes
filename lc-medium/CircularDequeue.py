class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.queue = [-1]*k
        self.front = -1
        self.rear = -1


    def isEmpty(self) -> bool:
        if self.front == self.rear == -1:
            return True
        else:
            return False


    def isFull(self) -> bool:
        if (self.rear + 1)%self.size == self.front:
            return True
        return False
                

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front +=1
            self.rear += 1
            self.queue[self.front] = value
            return True
        else:
            self.front = (self.front - 1)%self.size
            self.queue[self.front] = value
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front +=1
            self.rear += 1
            self.queue[self.front] = value
            return True
        else:
            self.rear = (self.rear + 1)%self.size
            self.queue[self.rear] = value
        return True


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
            return True
        else:
            self.front = (self.front+1)%self.size
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
            return True
        else:
            self.rear = (self.rear-1)%self.size
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]


    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear]