class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []

    def is_empty(self):
        if len(self.list):
            return False
        else:
            return True

    def is_full(self):
        if len(self.list) == self.capacity:
            return True
        else:
            return False

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            value = self.list.pop(-1)
            return value

    def enqueue(self, value):
        if self.is_full():
            print("The Queue is full.")
        else:
            self.list.insert(0, value)

    def front(self):
        if self.is_empty():
            print("The Queue is empty.")
            return None
        else:
            return self.list[-1]

queue = MyQueue(3)
queue.enqueue(1)
queue.enqueue(2)

print(queue.is_empty())
print(queue.is_full())
print(queue.front())
print(queue.dequeue())
print(queue.front())
print(queue.dequeue())
print(queue.is_empty())
