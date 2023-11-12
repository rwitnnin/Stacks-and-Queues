class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    def push(self, items):
        self.items.append(items)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


