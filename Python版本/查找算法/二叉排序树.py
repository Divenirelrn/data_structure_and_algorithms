
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return "Value:%d"%self.data if self.data else "NonoType"


class BitSortedTree:
    """二叉排序树（二叉搜索树）"""
    def __init__(self):
        self.root = None

    def createTree(self, l):
        for i in range(len(l)):
            node = Node(l[i])
            if self.root == None:
                self.root = node
                continue

            p = self.root
            while(p):
                if l[i] < p.data:
                    if p.left:
                        p = p.left
                    else:
                        p.left = node
                        break
                elif l[i] > p.data:
                    if p.right:
                        p = p.right
                    else:
                        p.right = node
                        break


def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end="->")
        in_order(root.right)

def bst_search(bst, value):
    """二叉排序树查找"""
    p = bst.root
    while(p):
        if p.data > value:
            p = p.left
        elif p.data < value:
            p = p.right
        else:
            return p

    return -1


def bst_search2(root, value):
    """二叉排序树查找（递归）"""
    if not root:
        return False
    else:
        if root.data == value:
            return True
        elif value < root.data:
            return bst_search2(root.left, value)
        else:
            return bst_search2(root.right, value)


def bst_insert(bst, value):
    """二叉排序树插入"""
    p = bst.root
    while (p):
        pre = p
        if p.data > value:
            p = p.left
        elif p.data < value:
            p = p.right

    if value < pre.data:
        pre.left = Node(value)
    elif value > pre.data:
        pre.right = Node(value)


def bst_delete(bst, value):
    """二叉排序树删除"""
    if not bst.root:
        return -1

    p = bst.root
    pre = p
    while p:
        if p.data == value:
            break
        elif value < p.data:
            pre = p
            p = p.left
        else:
            pre = p
            p = p.right

    if not p:
        return -1

    if p == bst.root:
        if not p.left and not p.right:
            bst.root = None
        elif not p.left:
            bst.root = bst.root.right
        elif not p.right:
            bst.root = bst.root.left
        else:
            del_node(p, pre)
    else:
        del_node(p, pre)


def del_node(p, pre):
    if not p.left and not p.right:
        if pre.left == p:
            pre.left = None
        else:
            pre.right = None
    elif not p.left:
        if pre.left == p:
            pre.left = p.right
        else:
            pre.right = p.right
    elif not p.right:
        if pre.left == p:
            pre.left = p.left
        else:
            pre.right = p.left
    else:
        r = p.left
        pre = p.left
        while(r.right):
            pre = r
            r = r.right

        if pre == r:
            p.data = r.data
            p.left = r.left
            del r
        else:
            p.data = r.data
            pre.right = r.left
            del r


if __name__ == "__main__":
    bs_tree = BitSortedTree()
    bs_tree.createTree([70,67,46,105,100,99,104,103,115,110,108,112])
    in_order(bs_tree.root)
    print("")
    # print(bst_search(bs_tree, 106))
    print(bst_search2(bs_tree.root, 105))
    # bst_insert(bs_tree, 106)
    # in_order(bs_tree.root)
    bst_delete(bs_tree, 70)
    in_order(bs_tree.root)