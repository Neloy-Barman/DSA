class Node:
    def __init__(self,val, left = None, right=None):
        self.left = left
        self.val = val
        self.right = right

def findDepth(node, depth):
    if not node:
        print("Here it goes")
        return depth
    depth += 1
    print(node.val, depth)
    # if node.left and node.right:
    #     return findDepth(node.left, depth) and findDepth(node.right, depth)
    # else:
        # return findDepth(node.left, depth) or findDepth(node.right, depth)
    leftDepth = findDepth(node.left, depth)
    rightDepth = findDepth(node.right, depth)

    if leftDepth >= rightDepth:
        return leftDepth
    else:
        return rightDepth
    # elif node.left:
    #     return findDepth(node.left, depth)
    # elif node.right:
    #     return findDepth(node.right, depth)



def bfs(node):
    nodes, i, right = [[node]], 0, True
    while i < len(nodes):
        print(nodes[i], right)
        inner = []
        if right:
            j = 0
            while j < len(nodes[i]):
                if nodes[i][j].right:
                    inner.append(nodes[i][j].right)
                if nodes[i][j].left:
                    inner.append(nodes[i][j].left)
                j += 1
        else:
            j = len(nodes[i])-1
            while j > -1:
                if nodes[i][j].left:
                    inner.append(nodes[i][j].left)
                if nodes[i][j].right:
                    inner.append(nodes[i][j].right)
                j -= 1
        print([node.val for node in inner])
        if inner != []:
            nodes.append(inner)
        i += 1
        right = not right
        print(f"Right after changing: {right}")
    
    return [[node.val for node in items] for items in nodes]



def main():
    # node1 = Node(val=9)
    # node2 = Node(val=15)
    # node3 = Node(val=7)
    # node4 = Node(val=20, left=node2, right=node3)
    # node5 = Node(val=3, left=node1, right=node4)

    # depth = findDepth(node5, 0)
    # print(depth)

    # node1 = Node(val=1)
    # # node2 = Node(val=2, left=node1)

    # node2 = Node(val=2, right=node1)

    # depth = findDepth(node2, 0)
    # print(depth)

    # print(1 or 2)

    # node1 = Node(val=4)
    # node2 = Node(val=5)
    # node3 = Node(val=2, left=node1, right=node2)
    # node4 = Node(val=3)
    # node5 = Node(val=1, left=node3, right=node4)

    # depth = findDepth(node5, 0)
    # print(depth)

    node1 = Node(val=4)
    node2 = Node(val=2, left=node1)

    node3 = Node(val=5)
    node4 = Node(val=3, right=node3)

    node5 = Node(val=1, left=node2, right=node4)

    nodes = bfs(node=node5)
    print(nodes)



if __name__ == "__main__":
    main()