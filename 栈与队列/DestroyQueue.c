//Ïú»Ù¶ÓÁĞ

DestroyQueue(LinkQueue* q)
{
	while (q->front) {
		q->rear = q->front->next;
		free(q->front);
		q->front = q->rear;
	}
}
