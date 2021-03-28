#include <stdio.h>

/*
线性表(List)：
	由0个或过个数据元素组成的有限序列

前驱
后继

抽象数据类型(ADT)：
	数据类型：一组性质相同的值的集合及定义在此集合上的一些操作的总称，如整型、浮点型、字符型
		原子类型
		结构类型

	对已有的数据类型进行抽象，就有了抽象数据类型
	一个数学模型及定义在该模型上的一组操作（取决于逻辑特性，与计算机内部的实现无关）

	抽象数据类型的标准格式：
		ADT 抽象数据类型名
		Data
			数据元素之间的逻辑关系的定义
		Operation
			操作
		endADT

线性表的抽象数据类型：
	ADT 线性表（List）
	Data
		线性表的数据对象集合为{a1, a2, ...,an}，每个元素的类型均为DataType。其中，除了第一个元素a1外，都只有一个直接前驱元素，
		除最后一个元素an外，都只有一个直接后继元素，元素之间的关系是一对一的关系
	Operation
		InitList(*L):初始化
		ListEmpty(L):判断是否为空
		ClearList(*L)
		GetElem(L, i, *e)
		LocateElem(L,e):查找失败返回0
		ListInsert(*L, i, e)
		ListDelete(*L,i,*e)
		ListLength(L)
	endADT

线性表的顺序存储结构：
	三个属性：
		起始位置
		最大存储容量（一般初始化不变，扩容）
		当前长度

	LOC(ai) = LOC(a1) + (i-1)*c #c为字节数
		随时可以计算出任意位置的地址（随机存储结构）

	优缺点：
		读、写数据，时间复杂度为o(1),插入删除操作o(n)
		比较适合元素个数比较稳定，不经常插入与删除，经常存取数据的情况

		优点：
			无须为表示表中的逻辑关系而额外增加存储空间
			可以快速存取表中任意位置的元素

		缺点：
			插入与删除需要移动大量元素
			当线性表长度变化较大时，难以确定存储空间的容量
			容易造成存储空间的“碎片”




*/
#define MAXSIZE 20
typedef int ElemType;
typedef struct
{
	ElemType data[MAXSIZE];
	int length; //线性表当前长度
} SqList;

int main()
{
	
	return 0;
}