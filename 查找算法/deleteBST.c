//二叉排序书删除

/*
对于一般的二叉树来说，删去树中的一个结点是没有意义的，因为：
它将使以被删除的结点为根的子树变成森林，破坏了整棵树的结构
但是，对于二叉排序树，删去树上的一个结点相当于删去有序序列中的一个记录。

只要在删除某个结点后不改变二叉排序树的特性即可。
在二叉排序树上删除一个结点的算法如下：
*/
btree* DeleteBST(btree* b, ElemType x)
{
    if (b)
    {
        if (b->data == x)
            b = DelNode(b);
        else if (b->data > x)
            b->lchild = DeleteBST(b->lchild, x);
        else
            b->rchild = DeleteBST(b->rchild, x);
    }
    return b;
}

/*

删除过程
删除过程有两种方法。
第一种过程如下：
        1、若p有左子树，找到其左子树的最右边的叶子结点r，用该叶子结点r来替代p，把r的左孩子作为r的父亲的右孩子。
        2、若p没有左子树，直接用p的右孩子取代它。
*/

btree* DelNode(btree* p) //指向指针的指针，可以直接修改地址
{
    if (p->lchild)
    {
        btree* r = p->lchild;   //r指向其左子树;  
        while (r->rchild != NULL)//搜索左子树的最右边的叶子结点r  
        {
            r = r->rchild;
        }
        r->rchild = p->rchild;

        btree* q = p->lchild;   //q指向其左子树;  
        free(p);
        return q;
    }
    else
    {
        btree* q = p->rchild;   //q指向其右子树;  
        free(p);
        return q;
    }
}

/*
第二种过程如下：
    1、若p有左子树，用p的左孩子取代它；找到其左子树的最右边的叶子结点r，把p的右子树作为r的右子树。
    2、若p没有左子树，直接用p的右孩子取代它。
*/
btree* DelNode(btree* p)
{
    if (p->lchild)
    {
        btree* r = p->lchild;   //r指向其左子树;  
        btree* prer = p->lchild;   //prer指向其左子树;  
        while (r->rchild != NULL)//搜索左子树的最右边的叶子结点r  
        {
            prer = r;
            r = r->rchild;
        }

        if (prer != r)//若r不是p的左孩子，把r的左孩子作为r的父亲的右孩子  
        {
            prer->rchild = r->lchild;
            r->lchild = p->lchild; //被删结点p的左子树作为r的左子树  
        }
        r->rchild = p->rchild; //被删结点p的右子树作为r的右子树  

        free(p);
        return r;
    }
    else
    {
        btree* q = p->rchild;   //q指向其右子树;  
        free(p);
        return q;
    }
}

/*
* 两种方法各有优劣，第一种操作简单一点点，但均衡性不如第二种，因为它将结点p的右子树全部移到左边来了。
  但是第一种方法，把r移来移去，很容易出错，其实在这里我们删除的只是p的元素值，而不是它的地址，所以完全没有必要移动指针。

  算法实现：
    仔细观察：
        发现我们删除的地址实际上是p的左子树的最右边的叶子结点r的地址。

    所以我们只要把r的数据填到p中，然后把r删除即可。
*/
btree* DelNode(btree* p)
{
    if (p->lchild)
    {
        btree* r = p->lchild;   //r指向其左子树;  
        btree* prer = p->lchild;   //prer指向其左子树;  
        while (r->rchild != NULL)//搜索左子树的最右边的叶子结点r  
        {
            prer = r;
            r = r->rchild;
        }
        p->data = r->data;

        if (prer != r)//若r不是p的左孩子，把r的左孩子作为r的父亲的右孩子  
            prer->rchild = r->lchild;
        else
            p->lchild = r->lchild; //否则结点p的左子树指向r的左子树  

        free(r);
        return p;
    }
    else
    {
        btree* q = p->rchild;   //q指向其右子树;  
        free(p);
        return q;
    }
}