from collections import deque

class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.deque = deque()        # su dung deque thay vi list

    def is_empty(self):
        if len(self.deque):
            return False
        else:
            return True

    def is_full(self):
        if len(self.deque) == self.capacity:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.is_full():
            return
        else:
            self.deque.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            x = self.deque.pop()
            return x

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print(self.deque)

