class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value=value)
        if not self.root:
            self.root = node
        else:
            currentNode = self.root
            while currentNode != None:
                if currentNode.value > node.value:
                    currentNode = currentNode.left
                else:
                    currentNode = currentNode.right
            currentNode = node

    def lookup(self, value):
        pass

    # remove

def main():
    bst = BinarySearchTree()

if __name__ == '__main__':
    main()

