/*
栈：
	一个先进后出的线性表，要求只在表尾进行删除与插入
	栈顶、栈底

	插入操作，进栈，PUSH
	出栈，POP

	栈的顺序存储结构与链式存储结构

	链式存储结构：
		将栈顶放在单链表的头部，栈顶指针和单链表的头指针合二为一。

	逆波兰表达式

	中缀转后缀

队列：
	只允许在一端进行插入操作，而在另一端进行删除操作的线性表。
    与栈相反，队列是一种先进先出（First In First Out, FIFO）的线性表。
    与栈相同的是，队列也是一种重要的线性结构，实现一个队列同样需要顺序表或链表作为基础

	队列既可以用链表实现，也可以用顺序表实现。
	跟栈相反的是：
		栈一般我们用顺序表来实现，而队列我们常用链表来实现，简称为链队列。









*/

#include<stdio.h>
#include<stdlib.h>

typedef int ElemType;

//栈的顺序存储结构
typedef struct
{
	ElemType* base;
	ElemType* top;
	int stackSize;
}sqStack;

//栈的链式存储结构
typedef struct StackNode
{
	ElemType data;        // 存放栈的数据
	struct StackNode* next;
} StackNode, * LinkStackPtr;
typedef struct LinkStack
{
	LinkStackPrt top;        // top指针
	int count;                // 栈元素计数器
}


int main()
{



	return 0;
}