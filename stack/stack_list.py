class Stack:
    # Initialization
    def __init__(self):
        self.stack = []
        self.length = 0

    # Checking if empty or not
    def isempty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    # Pushing value 
    def push(self,value):
        self.stack.append(value)
        self.length += 1
        return self
    
    # Get size
    def getSize(self):
        return self.length

    # Popping value
    def pop(self):
        if self.isempty():
            return
        self.stack.pop()
        self.length -= 1
        return self
    
    # Peeking or viewing top element
    def peek(self):
        if self.isempty():
            return
        return self.stack[-1]
    
def main():
    # Initialization
    stack = Stack()

    # Is empty or not
    print(stack.isempty())

    # Insertion
    stack.push('Google')
    stack.push('Facebook')
    stack.push('Yahoo')
    print(stack.peek())

    print(stack.isempty())
    
    # Pop
    stack.pop()
    print(stack.peek())

    # Size
    print(f"Size of the stack: {stack.getSize()}")


if __name__ == "__main__":
    main()