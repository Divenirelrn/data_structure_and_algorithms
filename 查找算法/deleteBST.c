//����������ɾ��

/*
����һ��Ķ�������˵��ɾȥ���е�һ�������û������ģ���Ϊ��
����ʹ�Ա�ɾ���Ľ��Ϊ�����������ɭ�֣��ƻ����������Ľṹ
���ǣ����ڶ�����������ɾȥ���ϵ�һ������൱��ɾȥ���������е�һ����¼��

ֻҪ��ɾ��ĳ�����󲻸ı���������������Լ��ɡ�
�ڶ�����������ɾ��һ�������㷨���£�
*/
btree* DeleteBST(btree* b, ElemType x)
{
    if (b)
    {
        if (b->data == x)
            b = DelNode(b);
        else if (b->data > x)
            b->lchild = DeleteBST(b->lchild, x);
        else
            b->rchild = DeleteBST(b->rchild, x);
    }
    return b;
}

/*

ɾ������
ɾ�����������ַ�����
��һ�ֹ������£�
        1����p�����������ҵ��������������ұߵ�Ҷ�ӽ��r���ø�Ҷ�ӽ��r�����p����r��������Ϊr�ĸ��׵��Һ��ӡ�
        2����pû����������ֱ����p���Һ���ȡ������
*/

btree* DelNode(btree* p) //ָ��ָ���ָ�룬����ֱ���޸ĵ�ַ
{
    if (p->lchild)
    {
        btree* r = p->lchild;   //rָ����������;  
        while (r->rchild != NULL)//���������������ұߵ�Ҷ�ӽ��r  
        {
            r = r->rchild;
        }
        r->rchild = p->rchild;

        btree* q = p->lchild;   //qָ����������;  
        free(p);
        return q;
    }
    else
    {
        btree* q = p->rchild;   //qָ����������;  
        free(p);
        return q;
    }
}

/*
�ڶ��ֹ������£�
    1����p������������p������ȡ�������ҵ��������������ұߵ�Ҷ�ӽ��r����p����������Ϊr����������
    2����pû����������ֱ����p���Һ���ȡ������
*/
btree* DelNode(btree* p)
{
    if (p->lchild)
    {
        btree* r = p->lchild;   //rָ����������;  
        btree* prer = p->lchild;   //prerָ����������;  
        while (r->rchild != NULL)//���������������ұߵ�Ҷ�ӽ��r  
        {
            prer = r;
            r = r->rchild;
        }

        if (prer != r)//��r����p�����ӣ���r��������Ϊr�ĸ��׵��Һ���  
        {
            prer->rchild = r->lchild;
            r->lchild = p->lchild; //��ɾ���p����������Ϊr��������  
        }
        r->rchild = p->rchild; //��ɾ���p����������Ϊr��������  

        free(p);
        return r;
    }
    else
    {
        btree* q = p->rchild;   //qָ����������;  
        free(p);
        return q;
    }
}

/*
* ���ַ����������ӣ���һ�ֲ�����һ��㣬�������Բ���ڶ��֣���Ϊ�������p��������ȫ���Ƶ�������ˡ�
  ���ǵ�һ�ַ�������r������ȥ�������׳�����ʵ����������ɾ����ֻ��p��Ԫ��ֵ�����������ĵ�ַ��������ȫû�б�Ҫ�ƶ�ָ�롣

  �㷨ʵ�֣�
    ��ϸ�۲죺
        ��������ɾ���ĵ�ַʵ������p�������������ұߵ�Ҷ�ӽ��r�ĵ�ַ��

    ��������ֻҪ��r�������p�У�Ȼ���rɾ�����ɡ�
*/
btree* DelNode(btree* p)
{
    if (p->lchild)
    {
        btree* r = p->lchild;   //rָ����������;  
        btree* prer = p->lchild;   //prerָ����������;  
        while (r->rchild != NULL)//���������������ұߵ�Ҷ�ӽ��r  
        {
            prer = r;
            r = r->rchild;
        }
        p->data = r->data;

        if (prer != r)//��r����p�����ӣ���r��������Ϊr�ĸ��׵��Һ���  
            prer->rchild = r->lchild;
        else
            p->lchild = r->lchild; //������p��������ָ��r��������  

        free(r);
        return p;
    }
    else
    {
        btree* q = p->rchild;   //qָ����������;  
        free(p);
        return q;
    }
}