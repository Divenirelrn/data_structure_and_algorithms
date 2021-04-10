//Ïú»ÙÒ»¸öÕ»

DestroyStack(sqStack* s) {
	int i, len;
	len = s->stackSize;
	for (i = 0; i < len; i++) {
		free(s->base);
		s->base++;
	}
	s->base = s->top = NULL;
	s->stackSize = 0;
}
