
class Node:
    def __init__(self, val,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def breadthFirstSearch(node: Node) -> list[int]:
    stack, nodes = [node], []
    while stack != []:
        node = stack.pop(0)
        nodes.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return nodes

def allPaths(node: Node, nodes):
    if not node:
        return nodes
    if not node.left and not node.right:
        # print(f"Leaf Node: {node.val}, available nodes: {nodes}")
        for n in nodes:
            print(f"{n} -> ", end="")
        print(node.val)
        sum_ = sum(nodes)+node.val
        print(f"Path sum: {sum_}")
        return nodes
    nodes.append(node.val)
    if node.left:
        allPaths(node=node.left, nodes=nodes)
    if node.right:
        allPaths(node=node.right, nodes=nodes)
    nodes.pop()
    return nodes


def availablePaths(node: Node, nodes):
    if not node.left and not node.right:
        for n in nodes:
            print(f"{n} -> ", end="")
        print(node.val)
        return nodes
    nodes.append(node.val)
    if node.left:
        availablePaths(node=node.left, nodes=nodes)
    if node.right:
        availablePaths(node=node.right, nodes=nodes)
    nodes.pop()
    return nodes


def pathSums(node: Node, nodes: list[int], sums: list[int]):
    if not node.left and not node.right:
        sums.append(sum(nodes)+node.val)
        return nodes, sums
    nodes.append(node.val)
    if node.left:
        pathSums(node=node.left, nodes=nodes, sums = sums)
    if node.right:
        pathSums(node=node.right, nodes=nodes, sums = sums)
    nodes.pop()
    return nodes, sums


def matchPathSum(node: Node, nodes: list[int], target: int, matchFound: bool):
    if not node.left and not node.right:
        print(f"MatchFound value in leaf node: {matchFound}")
        if sum(nodes)+node.val == target:
            print("Match Found")
            matchFound = True
        return nodes, matchFound
    if not matchFound:
        print(f"This is the value: {node.val}, Match: {matchFound}")
        nodes.append(node.val)
        if node.left:
            nodes, matchFound = matchPathSum(node=node.left, nodes=nodes, target=target, matchFound = matchFound)
        if node.right:
            nodes, matchFound = matchPathSum(node=node.right, nodes=nodes, target=target, matchFound = matchFound)
        nodes.pop()
        return nodes, matchFound
    else:
        return nodes, matchFound


def main():
    # Tree 1
    node1 = Node(val=9)
    node2 = Node(val=15)
    node3 = Node(val=7)
    node4 = Node(val=20, left=node2, right=node3)
    node5 = Node(val=3, left=node1, right=node4)
    # nodes = breadthFirstSearch(node=node5)
    # print(nodes)


    availablePaths(node=node5, nodes=[])

    _, sums = pathSums(node=node5, nodes=[], sums=[])
    print(sums)

    _, matchFound = matchPathSum(node=node5, nodes=[], target=38, matchFound=False)
    print(matchFound)

    # Tree 2
    # node1 = Node(val=1)
    # node2 = Node(val=3)
    # node3 = Node(val=6)
    # node4 = Node(val=4, left=node2, right=node3)
    # node5 = Node(val=5, left=node1, right=node4)
    # nodes = breadthFirstSearch(node=node5)
    # print(nodes)

if __name__ == "__main__":
    main()
