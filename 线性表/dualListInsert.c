//˫������������

s->next = p;
s->prior = p->prior;
p->prior->next = s;
p->prior = s;
