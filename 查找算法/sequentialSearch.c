//˳�����

// ��C������
// ˳������Ż�������aΪҪ���ҵ����飬nΪҪ���ҵ�����ĳ��ȣ�keyΪҪ���ҵĹؼ���
int Sq_Search(int* a, int n, int key)
{
    int i = n;
    a[0] = key
        while (a[i] != key)
        {
            i--;
        }

    return i;
}

//�Ż��汾
// ��C������
// ˳����ң�aΪҪ���ҵ����飬nΪҪ���ҵ�����ĳ��ȣ�keyΪҪ���ҵĹؼ���
int Sq_Search(int* a, int n, int key)
{
    int i;
    for (i = 1; i <= n; i++)
    {
        if (a[i] == key)
        {
            return i;
        }
    }
    return 0;
}