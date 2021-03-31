//�������ı���

//ǰ�����  
void preorderTraverse(BiTree T) {
    if (T == NULL)
        return;
    printf("%c", T->data);
    preorderTraverse(T->lchild);
    preorderTraverse(T->rchild);
}

//�������  
void InorderTraverse(BiTree T) {
    if (T) {
        InorderTraverse(T->lchild);
        printf("%c", T->data);
        InorderTraverse(T->rchild);
    }
}

//�������  
void PostorderTraverse(BiTree T) {
    if (T) {
        PostorderTraverse(T->lchild);
        PostorderTraverse(T->rchild);
        printf("%c", T->data);
    }
}