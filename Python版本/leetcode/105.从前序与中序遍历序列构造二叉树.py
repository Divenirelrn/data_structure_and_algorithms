#递归
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def inner(root_idx, left, right):
            # print("root_idx:", root_idx, left, right)
            if root_idx >= len_pre or left > right:
                return

            root = None
            left_root = None
            right_root = None
            sub_order = inorder[left: right + 1]
            in_idx = inorder.index(preorder[root_idx])
            if root_idx + 1 < len_pre and preorder[root_idx + 1] in inorder[left:in_idx]:
                left_root = inner(root_idx + 1, left, in_idx - 1)
                i = len_pre
                for i in range(root_idx + 2, len_pre):
                    if preorder[i] in inorder[in_idx + 1: right + 1]:
                        break

                if i != len_pre:
                    right_root = inner(i, in_idx + 1, right)

            elif root_idx + 1 < len_pre and preorder[root_idx + 1] in inorder[in_idx + 1:right + 1]:
                right_root = inner(root_idx + 1, in_idx + 1, right)

            root = TreeNode(preorder[root_idx])
            root.left = left_root
            root.right = right_root
            return root

        len_pre = len(preorder)
        if len_pre == 0:
            return None
        return inner(0, 0, len_pre - 1)


#迭代
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        len_pre = len(preorder)
        if not len_pre:
            return None

        idx = 0
        left, right = 0, len_pre - 1
        root = None
        node = TreeNode(preorder[idx])
        root = node
        s = [(node, left, right, idx)]

        while len(s) and idx < len_pre:
            parent, left, right, idx = s.pop()
            if left > right:
                continue

            p_idx = inorder.index(parent.val)
            if idx + 1 < len_pre and preorder[idx + 1] in inorder[left: p_idx + 1]:
                l_node = TreeNode(preorder[idx + 1])
                parent.left = l_node
                i = idx + 2
                while i < len_pre:
                    if preorder[i] in inorder[p_idx + 1: right + 1]:
                        break
                    i += 1

                if i != len_pre:
                    r_node = TreeNode(preorder[i])
                    parent.right = r_node
                    s.append((r_node, p_idx + 1, right, i))

                s.append((l_node, left, p_idx - 1, idx + 1))

            elif idx + 1 < len_pre and preorder[idx + 1] in inorder[p_idx + 1: right + 1]:
                r_node = TreeNode(preorder[idx + 1])
                parent.right = r_node
                s.append((r_node, p_idx + 1, right, idx + 1))

        return root


#优化版本
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def inner(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            pre_root = preorder[pre_left]
            in_root = hash_t[pre_root]

            root = TreeNode(pre_root)
            left_num = in_root - in_left
            left_node = inner(pre_left + 1, pre_left + left_num, in_left, in_root - 1)
            right_node = inner(pre_left + left_num + 1, pre_right, in_root + 1, in_right)

            root.left = left_node
            root.right = right_node

            return root

        len_pre = len(preorder)
        if len_pre == 0:
            return None
        hash_t = {val: idx for idx, val in enumerate(inorder)}
        return inner(0, len_pre - 1, 0, len_pre - 1)











