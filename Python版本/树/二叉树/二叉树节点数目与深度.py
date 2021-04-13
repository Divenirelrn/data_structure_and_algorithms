def nodeCount(root):
    """节点数目"""
    global num
    if root:
        num += 1
        nodeCount(root.left)
        nodeCount(root.right)

def treeNodenums(node):
    """节点数目"""
    if node == None:
        return 0
    num1 = treeNodenums(node.left)
    num2 = treeNodenums(node.right)
    return num1 + num2 + 1

def bTreeDepth(node):
    """二叉树深度"""
    if node == None:
         return 0
    ldepth = bTreeDepth(node.left)
    rdepth = bTreeDepth(node.right)
    return (max(ldepth, rdepth) + 1)

num = 0