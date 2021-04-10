//双向链表插入操作

s->next = p;
s->prior = p->prior;
p->prior->next = s;
p->prior = s;
