class Queue:
    def __init__(self):
        self.queue = []
        self.length = 0

    # Whether empty or not 
    def isEmpty(self):
        if self.length == 0:
            return True
        return False

    # Size of the queue
    def getSize(self):
        return self.length

    # Enqueue
    def enqueue(self,value):
        self.queue.append(value)
        self.length += 1
        return self
    
    # Dequeue
    def dequeue(self):
        if self.length == 0:
            return
        self.queue.pop(0)
        self.length -= 1
        return self

    # Peeking first element 
    def peek(self):
        if self.length == 0:
            return
        return self.queue[0]

def main():
    # Initialization
    queue = Queue()

    # Is empty or not
    print(queue.isEmpty())

    # Enqueue
    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(11)

    print(queue.peek())
    print(queue.isEmpty())

    # Dequeue
    queue.dequeue()
    queue.dequeue()
    # queue.dequeue()
    # queue.dequeue()

    print(queue.peek())

    # Size of the queue
    print(f"Size of the queue: {queue.getSize()}")






if __name__ == "__main__":
    main()