class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    # Initialization
    def __init__(self, value):
        newNode = Node(value=value)
        self.head = newNode
        self.tail = self.head
        self.length = 1

    # O(1)
    def prepend(self, value):
        newNode = Node(value=value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
    
    # O(1)
    def append(self, value):
        newNode = Node(value=value)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1 

    # O(n)
    def insert(self, value, index):
        if index >= self.length:
            print("Invalid index..")
            return
        elif index == 0:
            return self.prepend()
        elif index == self.length - 1:
            return self.append()
        newNode = Node(value=value)
        previousNode = self.traverseToIndex(index=index-1)
        newNode.next = previousNode.next
        previousNode.next = newNode
        self.length += 1
    
    # O(n)
    def remove(self, index):
        if index < 0 or index >= self.length:
            print("Invalid index...")
            return 
        elif index == 0:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1
            return
        elif index == self.length-1:
            previousNode = self.traverseToIndex(index=self.length-2)
            previousNode.next = None
            self.tail = previousNode
            self.length -= 1
            return            
        removingNode = self.traverseToIndex(index=index-1)
        temp = removingNode.next
        removingNode.next = temp.next
        temp.next = None
        self.length -= 1 

    # O(n)
    def traverseToIndex(self, index) -> Node:
        currentNode = self.head
        i = 0
        while i!= index:
            currentNode = currentNode.next
            i += 1
        return currentNode
    
    def len(self):
        return self.length
    
    # O(n)
    def traverse(self) -> list:
        currentNode = self.head
        values = []
        while currentNode != None:
            values.append(currentNode.value)
            currentNode = currentNode.next
        return values

    # O(n)
    def reverse(self):
        if self.length == 1:
            return
        currentNode = self.tail
        temp = currentNode
        i = self.length-2
        while i >= 0:
            changingNode = self.traverseToIndex(index=i)
            currentNode.next = changingNode
            currentNode = changingNode
            i -= 1
        currentNode.next = None
        self.tail = currentNode
        self.head = temp
        return
        
print(f"\nAfter instantiation: ")
singly = SinglyLinkedList(10)
print(f"Values: {singly.traverse()}, Length: {singly.len()}")

print(f"\nAfter appending: ")
singly.append(5)
singly.append(16)
print(f"Values: {singly.traverse()}, Length: {singly.len()}")

print(f"\nAfter prepending: ")
singly.prepend(1)
print(f"Values: {singly.traverse()}, Length: {singly.len()}")

print(f"\nAfter insertion: ")
singly.insert(index=2, value=99)
print(f"Values: {singly.traverse()}, Length: {singly.len()}")

singly.insert(index=20, value=88)
print(f"Values: {singly.traverse()}, Length: {singly.len()}")

print(f"\nAfter removal: ")
singly.remove(index=2)
print(f"Values: {singly.traverse()}, Length: {singly.len()}")
singly.remove(index=2)
print(f"Values: {singly.traverse()}, Length: {singly.len()}")
# singly.remove(index=2)
# print(f"Values: {singly.traverse()}, Length: {singly.len()}")
# singly.remove(index=1)
# print(f"Values: {singly.traverse()}, Length: {singly.len()}")

print("\nAfter reverse: ")
singly.reverse()
print(f"Values: {singly.traverse()}, Length: {singly.len()}")
