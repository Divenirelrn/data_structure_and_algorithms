//创建一个栈

#include "栈与队列.c"

#define STACK_INIT_SIZE 100
initStack(sqStack* s)
{
	s->base = (ElemType*)malloc(
	STACK_INIT_SIZE * sizeof(ElemType));

	if (!s->base)
		exit(0);
	s->top = s->base;
	s->stackSize = STACK_INIT_SIZE;
}