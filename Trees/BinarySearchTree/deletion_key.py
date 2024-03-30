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

def delete(head: TreeNode, key: int):
    cn = head
    stack = []
    while True:
        if key == cn.val:
            print(f"This is the stack: {[node.val for node in stack]}")
            node = stack[-1]
            print(f"Last value: {node.val}")
            if key > node.val:
                print("Greater")
                node.right = None
            else:
                print("Lesser")
                node.left = None
            return 'Node found and deleted'
        elif key < cn.val:
            if cn.left:
                stack.append(cn)
                cn = cn.left
            else:
                return 'Node not found'
        elif key > cn.val:
            if cn.right:
                stack.append(cn)
                cn = cn.right
            else:
                return 'Node not found'


def findSmallestPredecessor(node: TreeNode, pre: TreeNode):
    if node.val < pre.val:
        pre = node
    if node.left:
        return findSmallestPredecessor(node=node.left, pre=pre)
    return pre

def deletion(node: TreeNode, head: TreeNode, key: int, stack: list[TreeNode]):
    print(f"This is the head value: {head.val}, node value: {node.val}, stack: {[n.val for n in stack]}")
    if key == node.val:
        changingNode = stack[-1]
        if key < changingNode.val:
            if not node.left and not node.right:
                changingNode.left = None
            elif not node.left and node.right:
                changingNode.left = node.right
            elif node.left and not node.right:
                changingNode.left = node.left
            else:
                smallestNode = findSmallestPredecessor(node=head, pre=node.right)
                temp = smallestNode.val 
                deletion(node=head, head = head, key=temp, stack=[])
                node.val = temp
        else:
            if not node.right and not node.left:
                changingNode.right = None
            elif not node.right and node.left:
                changingNode.right = node.left
            elif node.right and not node.left:
                changingNode.right = node.right
            else:
                # print([node.val for node in stack])
                # print(node.val)
                smallestNode = findSmallestPredecessor(node=node.right, pre=node.right)
                # print(f"This is the smallest: {smallestNode.val}")
                temp = smallestNode.val 
                # print(f"This value is to be placed: {temp}, Stack: {stack[0].val}")
                deletion(node=head, head=head, key=temp, stack=[])
                nodes = traverse(node=stack[0], nodes=[])
                # print(nodes)
                # print(changingNode.val)
                node.val = temp
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
            

def deletion2(node: TreeNode, head: TreeNode, key: int, stack=[]):
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
                deletion2(node=head, head=head, key=temp, stack=[])
                node.val = temp 
        else:
            if node.left and node.right:
                smallestNode = findSmallestPredecessor(node=node.right,pre=node.right)
                temp = smallestNode.val
                deletion2(node=head, head=head, key=temp, stack=[])
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
                return deletion2(node=node.left, head=head, key=key, stack=stack)
            else:
                return head
        else:
            if node.right:
                return deletion2(node=node.right, head=head, key=key, stack=stack)
            else:
                return head

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

    node1 = TreeNode(val=5)
    node2 = TreeNode(val=60)
    node3 = TreeNode(val=70, left=node2)
    node4 = TreeNode(val=100, left=TreeNode(val=85))
    node5 = TreeNode(val=80, left=node3, right=node4)
    node6 = TreeNode(val=20)
    node7 = TreeNode(val=50, left=node6, right=node5)
    node0 = TreeNode(val=10, left=node1, right=node7)

    # Normal Traverse
    # nodes = traverse(node=node0, nodes=[])
    # print(f"Pre-order Traversal: {nodes}")
    # print(f"In-order Traversal: {nodes}")
    # print(f"Post-order Traversal: {nodes}")

    # deletion(node=node0, key=50, head=node0,stack=[])
    # nodes = traverse(node=node0, nodes=[])
    # print(f"\n\n{nodes}")

    # deletion(node=node0, key=80, head=node0, stack=[])
    # nodes = traverse(node=node0, nodes=[])
    # print(nodes)

    # deletion(node=node0, key=10, head=node0, stack=[])
    # nodes = traverse(node=node0, nodes=[])
    # print(nodes)

    # Edge Case 1
    node2 = TreeNode(val=0)
    node1 = TreeNode(val=1, left=node2)
    head = node1
    # print(traverse(node=head, nodes=[]))

    head = deletion2(node=head, head=head, key=1, stack = [])
    head = deletion2(node=head, head=head, key=0, stack = [])
    # print(traverse(node=head, nodes=[]))

    # Edge Case 2
    node1 = None
    head = node1
    head = deletion2(node=node1, head=head, key=10, stack=[])
    # print(traverse(node=head, nodes=[]))

    # Edge Case 3
    node2 = TreeNode(val=2)
    node1 = TreeNode(val=1, right=node2)
    head = node1
    # print(traverse(node=head, nodes=[]))

    head = deletion2(node=head, head=head, key=1, stack = [])
    head = deletion2(node=head, head=head, key=2, stack = [])
    # print(traverse(node=head, nodes=[]))


    # Proper Case
    node1 = TreeNode(val=5)
    node2 = TreeNode(val=60)
    node3 = TreeNode(val=70, left=node2)
    node4 = TreeNode(val=100, left=TreeNode(val=85))
    node5 = TreeNode(val=80, left=node3, right=node4)
    node6 = TreeNode(val=20)
    node7 = TreeNode(val=50, left=node6, right=node5)
    node0 = TreeNode(val=10, left=node1, right=node7)
    head = node0
    # print(traverse(node=head, nodes=[]))
    
    head = deletion2(node=head, head=head, key=10, stack = [])
    print(traverse(node=head, nodes=[]))




if __name__ == "__main__":
    main()

