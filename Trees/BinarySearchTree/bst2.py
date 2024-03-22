
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

# Clumsy Version   
# def breadthFirstSearch(root: Node):
#     nodes = [root]
#     values = [root.val]
#     i = 0
#     while True:
#         if i == len(nodes):
#             # print("i greater than total nodes")
#             break
#         # print(f"Within BFS: {values[i]}")
#         n, v = traverse(nodes[i])
#         nodes.extend(n)
#         values.extend(v)
#         # print(values)
#         i += 1
#     print(values)


# def traverse(node: Node):
#     nodes = []
#     values = []
#     if node.left:
#         nodes.append(node.left)
#         values.append(node.left.val)
#     if node.right:
#         nodes.append(node.right)
#         values.append(node.right.val)
#     # print(f"Within traverse: {values}")
#     return nodes, values


# Clean Version
# def breadthFirstSearch(root: Node):
#     nodes = [root]
#     i = 0
#     while i < len(nodes):
#         nodes.extend(traverse(nodes[i]))
#         i += 1
#     return [node.val for node in nodes]

# def traverse(node: Node):
#     nodes = []
#     if node.left:
#         nodes.append(node.left)
#     if node.right:
#         nodes.append(node.right)
#     return nodes
            

def breadthFirstSearch(nodes: list,i):
    if i >= len(nodes):
        return [node.val for node in nodes]
    node = nodes[i]
    if node.left:
        nodes.append(node.left)
    if node.right:
        nodes.append(node.right)
    i  += 1
    return breadthFirstSearch(nodes,i)


def depthFirstSearch(node: Node, nodes):
    nodes.append(node.val)
    if node.left:
        depthFirstSearch(node=node.left, nodes=nodes)
    if node.right:
        depthFirstSearch(node = node.right, nodes=nodes)



def main():
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(20)
    tree.insert(1)
    tree.insert(6)
    tree.insert(15)
    tree.insert(170)
    tree.insert(0)
    tree.insert(1.5)
    # tree.insert(170)
    # tree.insert(15)
    # tree.insert(1)
    # tree.insert(0)
    # tree.insert(1.5)

    # nodes = traverse(tree.root)
    # print(nodes)

    nodes = breadthFirstSearch([tree.root],0)
    print(nodes)

    # nodes = []
    # print(f"Before Traversal: {nodes}")
    # depthFirstSearch(tree.root, nodes=nodes)
    # print(f"After Traversal: {nodes}")

if __name__ == "__main__":
    main()