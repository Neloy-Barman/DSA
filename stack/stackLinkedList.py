class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        newNode = Node(value=value)
        if self.length == 0:
            self.top = newNode
            self.bottom = self.top
            self.length += 1
            return
        newNode.next = self.top
        self.top = newNode
        self.length += 1
        return self

    def peek(self):
        return self.top

    def pop(self):
        if self.length == 0:
            return
        temp = self.top
        self.top = temp.next
        self.length -= 1
        temp.next = None
    
    def isEmpty(self):
        if self.length != 0:
            return False
        return True
    
myStack = Stack()

myStack.push('google')
myStack.push('Udemy')
myStack.push('Discord')

# print(myStack.length)





