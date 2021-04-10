//循环队列插入

InsertQueue(cycleQueue* q, ElemType e)
{
	if ((q->rear + 1) % MAXSIZE == q->front)
		return; // 队列已满
	q->base[q->rear] = e;
	q->rear = (q->rear + 1) % MAXSIZE;
}
