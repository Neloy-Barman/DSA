class Node:
    def __init__(self, value):
       self.previous = None
       self.value = value
       self.next = None

class DoublyLinkedList:
    # Initialization
    def __init__(self, value):
       newNode = Node(value=value)
       self.head = newNode
       self.tail = self.head
       self.length = 1

    # O(1)
    def append(self, value):
       newNode = Node(value=value)
       self.tail.next = newNode
       newNode.previous = self.tail
       self.tail = newNode
       self.length += 1
       
    # O(1)
    def prepend(self, value):
       newNode = Node(value=value)
       self.head.previous = newNode
       newNode.next = self.head
       self.head = newNode
       self.length += 1
      
    # O(n)
    def insert(self, value, index):
       if index >= self.length or index < 0:
          print("Invalid index")
          return
       elif index == 0:
          return self.prepend()
       elif index == self.length - 1:
          return self.append()
       newNode = Node(value=value)
       previousNode = self.traverseToIndex(index=index-1)
       newNode.next = previousNode.next
       previousNode.next.previous = newNode
       newNode.previous = previousNode
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
            self.head.previous = None
            temp.next = None
            self.length -= 1
            return
        elif index == self.length-1:
            temp = self.tail
            self.tail = temp.previous
            self.tail.next = None
            temp.previous = None
            self.length -= 1
            return
        removingNode = self.traverseToIndex(index=index-1)
        temp = removingNode.next
        removingNode.next = temp.next
        temp.next.previous = removingNode
        temp.previous = None
        temp.next = None
        self.length -= 1
       
    # O(n)
    def traverseToIndex(self, index) -> Node:
        i = 0
        currentNode = self.head
        while i != index:
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
    def reverseTraverse(self) -> list:
        currentNode = self.tail
        values = []
        while currentNode != None:
            values.append(currentNode.value)
            currentNode = currentNode.previous
        return values

print(f"\nAfter instantiation: ")
doubly = DoublyLinkedList(10)
print(f"Values: {doubly.traverse()}, Length: {doubly.len()}")

print(f"\nAfter appending: ")
doubly.append(5)
doubly.append(16)
print(f"Values: {doubly.traverse()}, Length: {doubly.len()}")

print(f"\nAfter prepending: ")
doubly.prepend(1)
print(f"Values: {doubly.traverse()}, Length: {doubly.len()}")

print(f"\nAfter insertion: ")
doubly.insert(index=2, value=99)
print(f"Values: {doubly.traverse()}, Length: {doubly.len()}")
doubly.insert(index=2, value=88)
print(f"Values: {doubly.traverse()}, Length: {doubly.len()}")

print(f"\nAfter removal: ")
doubly.remove(index=2)
print(f"Values: {doubly.traverse()}, Length: {doubly.len()}")
doubly.remove(index=doubly.len()-1)
print(f"Values: {doubly.traverse()}, Length: {doubly.len()}")
doubly.remove(index=2)
print(f"Values: {doubly.traverse()}, Length: {doubly.len()}")

print(f"\nReverse traversal: ")
print(f"Values: {doubly.reverseTraverse()}, Length: {doubly.len()}")





