

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def createBiTree(root):
    c= input("请输入字符：")

    if c == ' ':
        root = None
    else:
        node = Node(c)
        root = node
        createBiTree(root.left)
        createBiTree(root.right)


if __name__ == "__main__":
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')

    #root = e
    # root.left = a
    # root.right = g
    # a.right = c
    # c.left = b
    # c.right = d
    # g.right = f

    # preOrder(root)
    # print("\n")
    # inOrder(root)
    # print("\n")
    # postOrder(root)
    # print("\n")
    # levelOrder(root)

    treeRoot = None
    root = None
    createBiTree(root)
    preOrder(root)

