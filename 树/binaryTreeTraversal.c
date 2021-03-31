//二叉树的遍历

//前序遍历  
void preorderTraverse(BiTree T) {
    if (T == NULL)
        return;
    printf("%c", T->data);
    preorderTraverse(T->lchild);
    preorderTraverse(T->rchild);
}

//中序遍历  
void InorderTraverse(BiTree T) {
    if (T) {
        InorderTraverse(T->lchild);
        printf("%c", T->data);
        InorderTraverse(T->rchild);
    }
}

//后序遍历  
void PostorderTraverse(BiTree T) {
    if (T) {
        PostorderTraverse(T->lchild);
        PostorderTraverse(T->rchild);
        printf("%c", T->data);
    }
}