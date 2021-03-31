//��³˹�����㷨

int Find(int* parent, int f)
{
    while (parent[f] > 0)
    {
        f = parent[f];
    }

    return f;
}

// Kruskal�㷨������С������
void MiniSpanTree_Kruskal(MGraph G)
{
    int i, n, m;
    Edge edges[MAGEDGE];        // ����߼�����
    int parent[MAXVEX];                // ����parent���������жϱ�����Ƿ��γɻ�·

    for (i = 0; i < G.numVertexes; i++)
    {
        parent[i] = 0;
    }

    for (i = 0; i < G.numEdges; i++)
    {
        n = Find(parent, edges[i].begin);        // 4 2 0 1 5 3 8 6 6 6 7
        m = Find(parent, edges[i].end);                // 7 8 1 5 8 7 6 6 6 7 7

        if (n != m)                // ���n==m�����γɻ�·�������㣡
        {
            parent[n] = m;        // ���˱ߵĽ�β��������±�Ϊ����parent�����У���ʾ�˶����Ѿ���������������
            printf("(%d, %d) %d ", edges[i].begin, edges[i].end, edges[i].weight);
        }
    }
}