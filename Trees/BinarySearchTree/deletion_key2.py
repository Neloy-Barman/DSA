class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def traverse(node: TreeNode, nodes: list[TreeNode]):
    nodes.append(node.val)
    if node.left:
        traverse(node.left, nodes)
    # nodes.append(node.val)
    if node.right:
        traverse(node.right, nodes)
    # nodes.append(node.val)
    return nodes


def findSmallestPredecessor(node: TreeNode, pre: TreeNode):
    if node.val < pre.val:
        pre = node
    if node.left:
        return findSmallestPredecessor(node=node.left, pre=pre)
    return pre

def deletion(node: TreeNode, head: TreeNode, key: int, stack: list[TreeNode]):
    if key == node.val:
        if node.left and node.right:
            smallestNode = findSmallestPredecessor(node=node.right, pre=node.right)
            temp = smallestNode.val
            # print(f"Before Nodes: {traverse(node=head, nodes=[])}")
            # deletion(node=head, head=head, key=temp, stack=[])
            # print(f"After Nodes: {traverse(node=head, nodes=[])}")
            node.val = temp
        else:
            changingNode = stack[-1]
            # print(f"Changing Node val: {changingNode.val}")
            if not node.left and not node.right:
                if key < changingNode.val:
                    changingNode.left = None
                else:
                    changingNode.right = None
            if not node.left and node.right:
                if key < changingNode.val:
                    changingNode.left = node.right
                else:
                    changingNode.right = node.right
            else:
                if key < changingNode.val:
                    changingNode.left = node.left
                else:
                    changingNode.right = node.left
        return 1
    else:
        stack.append(node)
        if key < node.val:
            if node.left:
                return deletion(node.left, head, key, stack)
            else:
                return 0
        elif key > node.val:
            if node.right:
                return deletion(node.right, head, key, stack)
            else:
                return 0



def main():

    # Tree 1
    # node1 = TreeNode(val=4)
    # node2 = TreeNode(val=8, left=node1)
    # node5 = TreeNode(val=70)
    # node6 = TreeNode(val=60, right=node5)
    # node7 = TreeNode(val=50, right=node6)
    # node8 = TreeNode(val=40, right=node7)
    # node3 = TreeNode(val=30, right=node8)
    # node4 = TreeNode(val=10, left=node2, right=node3)

    # nodes = traverse(node=node4, nodes=[])
    # print(nodes)

    # found = delete(head=node4, key=70)
    # print(f"This is the key: {found}")

    # found = deletion(node=node4, key=4, stack = [])
    # print(f"Node Found or not: {found}")

    # nodes = traverse(node=node4, nodes=[])
    # print(nodes)

    # node1 = TreeNode(val=5)
    # node2 = TreeNode(val=60)
    # node3 = TreeNode(val=70, left=node2)
    # node4 = TreeNode(val=100, left=TreeNode(val=85))
    # node5 = TreeNode(val=80, left=node3, right=node4)
    # node6 = TreeNode(val=20)
    # node7 = TreeNode(val=50, left=node6, right=node5)
    # node0 = TreeNode(val=10, left=node1, right=node7)

    # Normal Traverse
    # nodes = traverse(node=node0, nodes=[])
    # print(f"Pre-order Traversal: {nodes}")
    # print(f"In-order Traversal: {nodes}")
    # print(f"Post-order Traversal: {nodes}")

    # deletion(node=node0, key=50, head=node0,stack=[])
    # nodes = traverse(node=node0, nodes=[])
    # print(f"{nodes}")

    # deletion(node=node0, key=80, head=node0, stack=[])
    # nodes = traverse(node=node0, nodes=[])
    # print(nodes)

    # deletion(node=node0, key=10, head=node0, stack=[])
    # nodes = traverse(node=node0, nodes=[])
    # print(nodes)

    node2 = TreeNode(val=2)
    node1 = TreeNode(val=1, right=node2)
    head = node1
    # Traverse
    print(traverse(node=node1, nodes=[]))

    deletion(node=node1, head=head, key=2, stack=[])
    print(traverse(node=node1, nodes=[]))




if __name__ == "__main__":
    main()

