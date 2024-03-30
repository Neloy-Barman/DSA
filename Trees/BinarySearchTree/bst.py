class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.val = value
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        newNode = Node(value=val)
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

    def lookup(self, value):
        currentNode = self.root
        while True:
            if currentNode.val == value:
                return 'Node Found'
            elif value < currentNode.val:
                if currentNode.left:
                    currentNode = currentNode.left
                else:
                    return "Node Not Found"
            elif value > currentNode.val:
                if currentNode.right:
                    currentNode = currentNode.right
                else:
                    return 'Node Not Found'
            else:
                return 'Node Not Found'
    
    # Normal traverse
    def traverse(self, node: Node):
        nodes = []
        nodes.append(node.val)
        if node.left:
            nodes.extend(self.traverse(node.left))
        if node.right:
            nodes.extend(self.traverse(node.right))
        return nodes

    # Breadth First Search
    def breadthFirstSearch(self, nodes: list[Node], i: int) -> list:
        if i == len(nodes):
            return [node.val for node in nodes]
        node = nodes[i]
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)
        i += 1
        return self.breadthFirstSearch(nodes, i)

    # Depth First Search
    def depthFirstSearch(self, node: Node, nodes: list):
        # Pre Order traversal
        # nodes.append(node.val)
        if node.left:
            self.depthFirstSearch(node.left, nodes)
        # In Order traversal
        nodes.append(node.val)
        if node.right:
            self.depthFirstSearch(node.right, nodes)
        # Post Order traversal
        # nodes.append(node.val)
        return nodes
    
    # remove


# Normal traverse
def traverse(node: Node, nodes):
    if node.left:
        traverse(node.left, nodes)
    if node.val:
        nodes.append(node.val)
    else:
        nodes.append(None)
    if node.right:
        traverse(node.right, nodes)
    return nodes

def isSymmetric(root: Node) -> bool:
    l, r = [], []
    if root.left:
        l = traverse(root.left, l)
    if root.right:
        r = traverse(root.right, r)
    print(l)
    print(r)
    if l == r:
        return True
    return False


def isSameTree(p: Node, q: Node) -> bool:
    np, nq, i = [p], [q], 0
    cp, cq = np[i], nq[i]
    print(cp.val, cq.val)
    while i < len(np):
        if cp.val != cq.val:
            return False
        # print(cp.val, cq.val)
        # print(cp.left, cq.left)
        # print(cp.right, cq.right)
        if cp.left and cq.left:
            np.append(cp.left)
            nq.append(cq.left)
        elif cp.left or cq.left:
            return False
        if cp.right and cq.right:
            np.append(cp.right)
            nq.append(cq.right)
        elif cp.right or cq.right:
            return False
        i += 1
        if i < len(np):
            cp, cq = np[i], nq[i]
    return True

def main():
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert(4)
    bst.insert(20)
    bst.insert(1)
    bst.insert(6)
    bst.insert(15)
    bst.insert(170)
    # bst.insert(0)
    # bst.insert(1.5)

    # traversal = bst.traverse(bst.root)
    # print(f'Normal Traversal: {traversal}')

    # print(bst.lookup(100))
    # print(bst.lookup(1.5))

    # bfsTraversal = bst.breadthFirstSearch(nodes=[bst.root], i=0)
    # print(f"Breadth First Traversal: {bfsTraversal}")

    # dfsTraversal = bst.depthFirstSearch(node=bst.root, nodes=[])
    # print(f"Depth First Traversal: {dfsTraversal}")


    # bst1 = BinarySearchTree()
    # bst1.insert(1)
    # bst1.insert(2)
    # bst1.insert(3)

    # bst2 = BinarySearchTree()
    # bst2.insert(1)
    # bst2.insert(2)
    # bst2.insert(3)

    # print(bst1.traverse(bst1.root))
    # print(bst2.traverse(bst2.root))


    # x = isSameTree(bst1.root, bst2.root)
    # print(x)

    # node1 = Node(value=3)
    # node2 = Node(value=4)

    # node3 = Node(value=4)
    # node4 = Node(value=3)

    # node5 = Node(value=2, left=node1, right=node2)
    # node6 = Node(value=2, left=node3, right=node4)

    # node7 = Node(value=1, left=node5, right=node6)

    # nodes = traverse(node=node7)
    # print(nodes)

    # print(isSymmetric(node7))

    # node1 = 

    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(2)
    bst.insert(5)
    bst.insert(3)
    bst.insert(4)
    bst.insert(6)

    nodes = bst.depthFirstSearch(bst.root, [])
    print(nodes)



if __name__ == '__main__':
    main()

