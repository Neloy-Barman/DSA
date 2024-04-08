class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# All types of necessary traversals
# Depth-First Search: - Consists of Pre-order, In-order and Post-order Traversal
def depthFirstSearch(node: TreeNode, nodes: list[int]) -> list[int]:
    if not node:
        return nodes
    # Pre-order Traversal
    nodes.append(node.val)
    if node.left:
        depthFirstSearch(node = node.left, nodes = nodes)
    # In-order Traversal
    # nodes.append(node.val)
    if node.right:
        depthFirstSearch(node = node.right, nodes = nodes)
    # Post-order Traversal
    # nodes.append(node.val)
    return nodes


# Breadth-First Search
# Way 1
# We will use only lists here both to traverse nodes and return node values
def breadthFirstSearch1(root: TreeNode):
    nodes = [root]
    i = 0
    while i < len(nodes):
        node = nodes[i]
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)
        i += 1
    return [node.val for node in nodes]


# Way 2
# We will use one list as stack to keep track of the nodes and another to store node values
def breadthFirstSearch2(root: TreeNode):
    stack = [root]
    nodes = []
    while len(stack) != 0:
        node = stack.pop(0)
        nodes.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return nodes


# Level Order Traversal
def levelOrderTraversal(root: TreeNode):
    nodes = [[root]]
    i = 0
    while i < len(nodes):
        j = 0
        temp = []
        while j < len(nodes[i]):
            node = nodes[i][j]
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            j += 1
        if temp != []:
            nodes.append(temp)
        i += 1
    return [[node.val for node in items] for items in nodes]


# Available Paths to Leaf Nodes
def availablePaths(node: TreeNode, nodes: list[int], paths: list[str]):
    if not node.left and not node.right:
        temp = ""
        for n in nodes:
            temp += f"{n}->"
        temp += f"{node.val}"
        paths.append(temp)
        return nodes, paths
    nodes.append(node.val)
    if node.left:
        nodes, paths = availablePaths(node=node.left, nodes=nodes, paths=paths)
    if node.right:
        nodes, paths = availablePaths(node=node.right, nodes=nodes, paths=paths)
    nodes.pop()
    return nodes, paths


# Find if a target sum exists in a available path to leaf node
def targetSumExists(node: TreeNode, nodes: list[int], target: int, matchFound: bool):
    if not node.left and not node.right:
        if sum(nodes)+node.val == target:
            matchFound = True
        return nodes, matchFound
    if not matchFound:
        nodes.append(node.val)
        if node.left:
            nodes, matchFound = targetSumExists(node=node.left, nodes=nodes, target=target, matchFound=matchFound)
        if node.right:
            nodes, matchFound = targetSumExists(node=node.right, nodes=nodes, target=target, matchFound=matchFound)
        nodes.pop()
    return nodes, matchFound


def main():
    node1 = TreeNode(val=7)
    node2 = TreeNode(val=2)
    node3 = TreeNode(val=11, left=node1, right=node2)
    node4 = TreeNode(val=4, left=node3)
    node5 = TreeNode(val=1)
    node6 = TreeNode(val=4, right=node5)
    node7 = TreeNode(val=13)
    node8 = TreeNode(val=8, left=node7, right=node6)
    root = TreeNode(val=5, left=node4, right=node8)

    # Depth-First Search
    nodes = depthFirstSearch(node=root, nodes=[])
    print(f"Depth-First Search: {nodes}")

    # Breadth-First Search
    # Way 1
    nodes = breadthFirstSearch1(root=root)
    print(f"Breadth-First Search(way 1): {nodes}")

    # Way 2
    nodes = breadthFirstSearch2(root=root)
    print(f"Breadth-First Search(way 2): {nodes}")

    # Level-Order traversal
    nodes = levelOrderTraversal(root=root)
    print(f"Level-Order Traversal: {nodes}")

    # All available paths to leaf nodes
    _, paths = availablePaths(node=root, nodes=[], paths=[])
    print(f"Available paths to leaf nodes: {paths}")

    # A path exists 5->8->13 exists and the sum of this path is 26, we will try to see if the sum is found.
    _, matchFound = targetSumExists(node=root, nodes=[], target=26, matchFound=False)
    print(f"Sum exists: {matchFound}")

    
if __name__ == "__main__":
    main()
