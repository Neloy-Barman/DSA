
class Node:
    def __init__(self, val):
        self.left = None
        self.val = val
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        newNode = Node(val=val)
        if self.root == None:
            self.root = newNode
            return
        currentNode = self.root
        while True:
            if val <= currentNode.val:
                if currentNode.left != None:
                    currentNode = currentNode.left
                else:
                    currentNode.left = newNode
                    return self
            else:
                if currentNode.right != None:
                    currentNode = currentNode.right
                else:
                    currentNode.right = newNode
                    return self
    
    def lookup(self, val):
        currentNode = self.root
        while True:
            if val < currentNode.val:
                if currentNode.left:
                    currentNode = currentNode.left
                else:
                    return None
            elif val > currentNode.val:
                if currentNode.right:
                    currentNode = currentNode.right
                else:
                    return None
            elif val == currentNode.val:
                return currentNode




            
def traverse(node):
    # nodes = []
    nodes = {}
    if node.left != None:
        # nodes.extend(traverse(node=node.left))
        traverse(node=node.left)
    # nodes = [node.val]
    # print(node.val, nodes)
    nodes[node.val] = node
    if node.right != None:
        # nodes.extend(traverse(node=node.right))
        traverse(node=node.right)
    # return nodes.append(node.val)
    return nodes
            
def main():
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)

    node = tree.lookup(17)
    if node:
        print(node)
    # nodes = traverse(tree.root)
    # print(nodes)

if __name__ == "__main__":
    main()