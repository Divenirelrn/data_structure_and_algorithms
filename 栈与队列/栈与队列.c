/*
ջ��
	һ���Ƚ���������Ա�Ҫ��ֻ�ڱ�β����ɾ�������
	ջ����ջ��

	�����������ջ��PUSH
	��ջ��POP

	ջ��˳��洢�ṹ����ʽ�洢�ṹ

	��ʽ�洢�ṹ��
		��ջ�����ڵ������ͷ����ջ��ָ��͵������ͷָ��϶�Ϊһ��

	�沨�����ʽ

	��׺ת��׺

���У�
	ֻ������һ�˽��в��������������һ�˽���ɾ�����������Ա�
    ��ջ�෴��������һ���Ƚ��ȳ���First In First Out, FIFO�������Ա�
    ��ջ��ͬ���ǣ�����Ҳ��һ����Ҫ�����Խṹ��ʵ��һ������ͬ����Ҫ˳����������Ϊ����

	���мȿ���������ʵ�֣�Ҳ������˳���ʵ�֡�
	��ջ�෴���ǣ�
		ջһ��������˳�����ʵ�֣����������ǳ���������ʵ�֣����Ϊ�����С�









*/

#include<stdio.h>
#include<stdlib.h>

typedef int ElemType;

//ջ��˳��洢�ṹ
typedef struct
{
	ElemType* base;
	ElemType* top;
	int stackSize;
}sqStack;

//ջ����ʽ�洢�ṹ
typedef struct StackNode
{
	ElemType data;        // ���ջ������
	struct StackNode* next;
} StackNode, * LinkStackPtr;
typedef struct LinkStack
{
	LinkStackPrt top;        // topָ��
	int count;                // ջԪ�ؼ�����
}


int main()
{



	return 0;
}