//循环队列出队

DeleteQueue(cycleQueue* q, ElemType* e)
{
	if (q->front == q->rear)
		return; // 队列为空
	*e = q->base[q->front];
	q->front = (q->front + 1) % MAXSIZE;
}
