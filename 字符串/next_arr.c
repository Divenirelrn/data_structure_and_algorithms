//KMP��next����ⷨ

void get_next(String T, int* next)
{
    j = 0;
    i = 1;
    next[1] = 0;
    while (i < T[0])
    {
        //���⡰=�������Σ�����д��0 == j
        if (0 == j || T[i] == T[j])
        {
            i++;
            j++;
            next[i] = j;
        }
        else
        {
            j = next[j];
        }
    }

    // ��Ϊǰ׺�ǹ̶��ģ���׺����Եġ�
}