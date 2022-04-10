class Stack:

    def __init__(self):
        self.items = []
        top = None

    def is_empty(self):
        return self.items == []

    # push function
    def push(self, data):
        self.items.append(data)

    # pop function
    def pop(self):
        return self.items.pop()
    
    def traversal(self):
        for i in self.items:
            print(i)

s = Stack()

s.push(1)
s.push(2)
s.push(3)
print("Elements in Stack : ")
s.traversal()
print("Pop element : ",s.pop())
print("Pop element : ",s.pop())
print("After pop Elements in Stack : ")
s.traversal()
