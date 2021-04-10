//循环队列初始化

initQueue(cycleQueue* q)
{
	q->base = (ElemType*)malloc(MAXSIZE * sizeof(ElemType));
	if (!q->base)
		exit(0);
	q->front = q->rear = 0;
}
