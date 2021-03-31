//线索二叉树

/* 二叉树的二叉线索存储结构定义
线索化的实质就是将二叉链表中的空指针改为指向前驱或后继的线索。
由于前驱和后继信息只有在遍历该二叉树时才能得到。
所以，线索化的过程就是在遍历的过程中修改空指针的过程。
*/
typedef enum { Link, Thread }PointerTag;    //Link = 0表示指向左右孩子指针；Thread = 1表示指向前驱或后继的线索

typedef struct BitNode
{
    char data;                                      //结点数据
    struct BitNode* lchild, * rchild;                //左右孩子指针
    PointerTag  Ltag;                               //左右标志
    PointerTag  rtal;
}BitNode, * BiTree;

/*中序遍历线索化的递归函数*/
BiTree pre;                 //全局变量，始终指向刚刚访问过的结点
//中序遍历进行中序线索化
void InThreading(BiTree p)
{
    if (p)
    {
        InThreading(p->lchild);          //递归左子树线索化
                //===
        if (!p->lchild)           //没有左孩子
        {
            p->ltag = Thread;    //前驱线索
            p->lchild = pre; //左孩子指针指向前驱
        }
        if (!pre->rchild)     //没有右孩子
        {
            pre->rtag = Thread;  //后继线索
            pre->rchild = p; //前驱右孩子指针指向后继(当前结点p)
        }
        pre = p;
        //===
        InThreading(p->rchild);      //递归右子树线索化
    }
}


#include <stdio.h>
#include <stdlib.h>

typedef char ElemType;

// 线索存储标志位
// Link(0)：表示指向左右孩子的指针
// Thread(1)：表示指向前驱后继的线索
typedef enum { Link, Thread } PointerTag;

typedef struct BiThrNode
{
    char data;
    struct BiThrNode* lchild, * rchild;
    PointerTag ltag;
    PointerTag rtag;
} BiThrNode, * BiThrTree;

// 全局变量，始终指向刚刚访问过的结点
BiThrTree pre;

// 创建一棵二叉树，约定用户遵照前序遍历的方式输入数据
void CreateBiThrTree(BiThrTree* T)
{
    char c;

    scanf("%c", &c);
    if (' ' == c)
    {
        *T = NULL;
    }
    else
    {
        *T = (BiThrNode*)malloc(sizeof(BiThrNode));
        (*T)->data = c;
        (*T)->ltag = Link;
        (*T)->rtag = Link;

        CreateBiThrTree(&(*T)->lchild);
        CreateBiThrTree(&(*T)->rchild);
    }
}

// 中序遍历线索化
void InThreading(BiThrTree T)
{
    if (T)
    {
        InThreading(T->lchild);                // 递归左孩子线索化

        if (!T->lchild)        // 如果该结点没有左孩子，设置ltag为Thread，并把lchild指向刚刚访问的结点。
        {
            T->ltag = Thread;
            T->lchild = pre;
        }

        if (!pre->rchild)
        {
            pre->rtag = Thread;
            pre->rchild = T;
        }

        pre = T;

        InThreading(T->rchild);                // 递归右孩子线索化
    }
}

void InOrderThreading(BiThrTree* p, BiThrTree T)
{
    *p = (BiThrTree)malloc(sizeof(BiThrNode));
    (*p)->ltag = Link;
    (*p)->rtag = Thread;
    (*p)->rchild = *p;
    if (!T)
    {
        (*p)->lchild = *p;
    }
    else
    {
        (*p)->lchild = T;
        pre = *p;
        InThreading(T);
        pre->rchild = *p;
        pre->rtag = Thread;
        (*p)->rchild = pre;
    }
}

void visit(char c)
{
    printf("%c", c);
}

// 中序遍历二叉树，非递归
void InOrderTraverse(BiThrTree T)
{
    BiThrTree p;
    p = T->lchild;

    while (p != T)
    {
        while (p->ltag == Link)
        {
            p = p->lchild;
        }
        visit(p->data);

        while (p->rtag == Thread && p->rchild != T)
        {
            p = p->rchild;
            visit(p->data);
        }

        p = p->rchild;
    }
}

int main()
{
    BiThrTree P, T = NULL;

    CreateBiThrTree(&T);

    InOrderThreading(&P, T);

    printf("中序遍历输出结果为: ");

    InOrderTraverse(P);

    printf("\n");

    return 0;
}