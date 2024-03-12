class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def peek(self):
        return self.first

    def enqueue(self, value):
        newNode = Node(value=value)
        if self.length == 0:
            self.first = newNode
            self.last = self.first
            self.length += 1
            return
        self.last.next = newNode
        self.last = newNode
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return
        temp = self.first
        self.first = temp.next
        temp.next = None
        self.length -= 1
    
myQueue = Queue()

myQueue.enqueue('Joy')
myQueue.enqueue('Matt')
myQueue.enqueue('Pavel')
myQueue.enqueue('Samir')

print(myQueue.peek().value)

myQueue.dequeue()
print(myQueue.peek().value)
