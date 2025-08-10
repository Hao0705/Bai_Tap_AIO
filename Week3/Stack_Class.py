class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []

    def is_empty(self):
        if len(self.list):
            return False
        else:
            return True

    def is_full(self):
        return self.capacity == len(self.list)

    def pop_stack(self):
        if self.is_empty():
            return None
        else:
            value = self.list.pop(-1)
            return value

    def push_stack(self, value):
        if self.is_full():
            return
        else:
            self.list.append(value)

    def top_stack(self):
        if self.is_empty():
            return None
        else:
            return self.list[-1]

    def print_stack(self):
        if self.is_empty():
            print("Khong co phan tu nao")
        else:
            index = 1
            for i in self.list:
                print(f"Phan tu thu {index}: {i}")
                index += 1

stack = MyStack(3)
stack.push_stack(1)
stack.push_stack(2)

stack.print_stack()
print(stack.is_full())
print(stack.pop_stack())