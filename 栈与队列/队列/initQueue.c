/*
�������У�
һ�����ڴ��д���һ��ͷ��㡣
���ǽ����е�ͷָ���βָ�붼ָ��������ɵ�ͷ��㣬��Ϊ��ʱ�ǿն��С�
*/

initQueue(LinkQueue* q)
{
    q->front = q->rear = (QueuePtr)malloc(sizeof(QNode));
    if (!q->front)
        exit(0);
    q->front->next = NULL;
}
