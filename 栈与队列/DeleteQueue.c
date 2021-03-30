//队列出队

DeleteQueue(LinkQueue* q, ELemType* e)
{
	QueuePtr p;
	if (q->front == q->rear)
		return;
	p = q->front->next;
	*e = p->data;
	q->front->next = p->next;
	if (q->rear == p)
		q->rear = q->front;
	free(p);
}
