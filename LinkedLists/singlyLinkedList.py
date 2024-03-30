class Node:
    def __init__(self, value):
        self.val = value
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
            values.append(currentNode.val)
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
        
# print(f"\nAfter instantiation: ")
# singly = SinglyLinkedList(10)
# print(f"Values: {singly.traverse()}, Length: {singly.len()}")

# print(f"\nAfter appending: ")
# singly.append(5)
# singly.append(16)
# print(f"Values: {singly.traverse()}, Length: {singly.len()}")

# print(f"\nAfter prepending: ")
# singly.prepend(1)
# print(f"Values: {singly.traverse()}, Length: {singly.len()}")

# print(f"\nAfter insertion: ")
# singly.insert(index=2, value=99)
# print(f"Values: {singly.traverse()}, Length: {singly.len()}")

# singly.insert(index=20, value=88)
# print(f"Values: {singly.traverse()}, Length: {singly.len()}")

# print(f"\nAfter removal: ")
# singly.remove(index=2)
# print(f"Values: {singly.traverse()}, Length: {singly.len()}")
# singly.remove(index=2)
# print(f"Values: {singly.traverse()}, Length: {singly.len()}")
# # singly.remove(index=2)
# # print(f"Values: {singly.traverse()}, Length: {singly.len()}")
# # singly.remove(index=1)
# # print(f"Values: {singly.traverse()}, Length: {singly.len()}")

# print("\nAfter reverse: ")
# singly.reverse()
# print(f"Values: {singly.traverse()}, Length: {singly.len()}")

# singly2 = SinglyLinkedList(7)
# singly2.append(9)
# singly2.append(6)
# singly2.append(6)
# singly2.append(7)
# singly2.append(8)
# singly2.append(3)
# singly2.append(0)
# singly2.append(9)
# singly2.append(5)
    
# singly2 = SinglyLinkedList(1)
# singly2.append(2)
# singly2.append(3)
# singly2.append(4)
# singly2.append(5)

singly2 = SinglyLinkedList(1)
singly2.append(2)
singly2.append(3)




def swapNodes(head: Node, k: int) -> Node:
    slow, fast = head, head
    counter, ch = 1, None
    while fast != None and fast.next != None:
        counter += 1
        print(counter)
        if counter == k:
            print('Counter accessed')
            ch = slow
        print(f"Slow: {slow.val}, Fast: {fast.val}")
        slow = slow.next
        fast = fast.next.next
        print(f"Slow: {slow.val}, Fast: {fast.val}")

    print(f"Changing: {ch.val}")

    if fast:
        slow = slow.next
    
    print(f"Counter: {counter}, slow: {slow.val}")

    chnext = None
    while counter != k-1:
        print(counter)
        if counter == k:
            chnext = slow
        slow = slow.next
        counter -= 1
    print(f"Value: {chnext.val}")
    # temp1 = ch.next
    # temp2 = chnext.next
    # chprev.next = chnext
    # chnext.next = temp1
    # ch.next = temp2
    temp = chnext.val
    chnext.val = ch.val
    ch.val = temp
    return head

swapNodes(singly2.head, k=2)

print(singly2.traverse())


# print(singly2.traverse())

# def isPalindrome(head: Node) -> bool:
#     slow, fast, stack = head, head, []
#     while fast != None and fast.next != None:
#         print(slow.val)
#         stack.append(slow.val)
#         slow = slow.next
#         fast = fast.next.next
#     currentNode = slow
#     if fast:
#         currentNode = slow.next
#     while currentNode != None:
#         if stack[-1] != currentNode.val:
#             print("It' False")
#             return False
#         stack.pop()
#         currentNode = currentNode.next
#     print("It' True")
#     return True

# isPalindrome(head=singly2.head)

