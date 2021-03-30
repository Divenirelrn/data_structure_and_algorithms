//Ë«ÏòÁ´±íÉ¾³ý²Ù×÷

p->prior->next = p->next;
p->next->prior = p->prior;
free(p);