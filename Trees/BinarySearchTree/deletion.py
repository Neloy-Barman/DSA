class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def traverse(node: TreeNode, nodes: list[TreeNode]):
    if not node:
        return nodes
    nodes.append(node.val)
    if node.left:
        traverse(node.left, nodes)
    # nodes.append(node.val)
    if node.right:
        traverse(node.right, nodes)
    # nodes.append(node.val)
    return nodes

# def traverse(node: TreeNode, nodes: list[TreeNode]):
#     if not node:
#         return nodes
#     nodes.append(node.val)
#     traverse(node.left, nodes)
#     traverse(node.right, nodes)
#     return nodes

def findSmallestPredecessor(node: TreeNode, pre: TreeNode):
    if node.val < pre.val:
        pre = node
    if node.left:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        return findSmallestPredecessor(node=node.left, pre=pre)
    return pre
            
def keyDeletion(node: TreeNode, head: TreeNode, key: int, stack=[]) -> TreeNode:
    if not node:
        return None
    if key == node.val:
        if stack == []:
            if not node.left and not node.right:
                head = None
            elif node.left and not node.right:
                head = node.left
            elif not node.left and node.right:
                head = node.right
            else:
                smallestNode = findSmallestPredecessor(node=node.right,pre=node.right)
                temp = smallestNode.val
                keyDeletion(node=head, head=head, key=temp, stack=[])
                node.val = temp 
        else:
            if node.left and node.right:
                smallestNode = findSmallestPredecessor(node=node.right,pre=node.right)
                temp = smallestNode.val
                keyDeletion(node=head, head=head, key=temp, stack=[])
                node.val = temp 
            else:
                changingNode = stack[-1]
                if not node.left and not node.right:
                    if key < changingNode.val:
                        changingNode.left = None
                    else:
                        changingNode.right = None
                elif node.left and not node.right:
                    if key < changingNode.val:
                        changingNode.left = node.left
                    else:
                        changingNode.right = node.left
                else:
                    if key < changingNode.val:
                        changingNode.left = node.right
                    else:
                        changingNode.right = node.right
        return head
    else:
        stack.append(node)
        if key < node.val:
            if node.left:
                return keyDeletion(node=node.left, head=head, key=key, stack=stack)
            else:
                return head
        else:
            if node.right:
                return keyDeletion(node=node.right, head=head, key=key, stack=stack)
            else:
                return head

def main():


    # # Edge Case 1
    # node2 = TreeNode(val=0)
    # node1 = TreeNode(val=1, left=node2)
    # head = node1
    # print(traverse(node=head, nodes=[]))

    # head = keyDeletion(node=head, head=head, key=1, stack = [])
    # head = keyDeletion(node=head, head=head, key=0, stack = [])
    # print(traverse(node=head, nodes=[]))


    # # Edge Case 2
    # node1 = None
    # head = node1
    # head = keyDeletion(node=node1, head=head, key=10, stack=[])
    # print(traverse(node=head, nodes=[]))


    # # Edge Case 3
    # node2 = TreeNode(val=2)
    # node1 = TreeNode(val=1, right=node2)
    # head = node1
    # print(traverse(node=head, nodes=[]))

    # head = keyDeletion(node=head, head=head, key=1, stack = [])
    # head = keyDeletion(node=head, head=head, key=2, stack = [])
    # print(traverse(node=head, nodes=[]))


    # # Proper Case 1
    # node1 = TreeNode(val=5)
    # node2 = TreeNode(val=60)
    # node3 = TreeNode(val=70, left=node2)
    # node4 = TreeNode(val=100, left=TreeNode(val=85))
    # node5 = TreeNode(val=80, left=node3, right=node4)
    # node6 = TreeNode(val=20)
    # node7 = TreeNode(val=50, left=node6, right=node5)
    # node0 = TreeNode(val=10, left=node1, right=node7)
    # head = node0
    # print(traverse(node=head, nodes=[]))
    
    # head = keyDeletion(node=head, head=head, key=10, stack = [])
    # print(traverse(node=head, nodes=[]))

    # head = keyDeletion(node=head, key=50, head=node0,stack=[])
    # print(traverse(node=head, nodes=[]))

    # head = keyDeletion(node=head, key=80, head=node0,stack=[])
    # print(traverse(node=head, nodes=[]))


    # # Proper Case 2
    # node1 = TreeNode(val=4)
    # node2 = TreeNode(val=8, left=node1)
    # node5 = TreeNode(val=70)
    # node6 = TreeNode(val=60, right=node5)
    # node7 = TreeNode(val=50, right=node6)
    # node8 = TreeNode(val=40, right=node7)
    # node3 = TreeNode(val=30, right=node8)
    # node4 = TreeNode(val=10, left=node2, right=node3)
    # head = node4
    # print(traverse(node=head, nodes=[]))

    # head = keyDeletion(node=head, head=head, key=8, stack = [])
    # print(traverse(node=head, nodes=[]))

    # head = keyDeletion(node=head, key=10, head=head,stack=[])
    # print(traverse(node=head, nodes=[]))

    # head = keyDeletion(node=head, key=70, head=head,stack=[])
    # print(traverse(node=head, nodes=[]))


    # Proper Case 2
    node60 = TreeNode(val=60)
    node80 = TreeNode(val=80)
    node70 = TreeNode(val=70, left=node60, right=node80)
    node40 = TreeNode(val=40)
    node30 = TreeNode(val=30, right=node40)
    node50 = TreeNode(val=50, left=node30, right=node70)
    head = node50
    print(traverse(node=head, nodes=[]))

    head = keyDeletion(node=head, head=head, key=50, stack = [])
    print(traverse(node=head, nodes=[]))


if __name__ == "__main__":
    main()

