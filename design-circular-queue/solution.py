class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.length = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isEmpty():
            self.queue[self.front] = value
            self.rear = self.front
            return True
        else:
            tempRear = (self.read + 1) % self.length
            if tempRear == self.front:
                return False
            self.rear = tempRear
            self.queue[self.rear] = value
            return True

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.queue[self.front] = None
            if self.isEmpty():
                self.front = self.rear
            else:
                self.front = (self.front + 1) % self.length
            return True
        return False

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        if self.front != self.rear or self.queue[self.front] is not None:
            return False
        return True

    def isFull(self) -> bool:
        tempRead = (self.rear + 1) % self.length
        if tempRead == self.front:
            return True
        return False
