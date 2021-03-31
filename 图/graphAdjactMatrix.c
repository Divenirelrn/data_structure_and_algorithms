/*����ͼ���ڽӾ���*/

// ʱ�临�Ӷ�ΪO(n+n^2+e)

#define MAXVEX 100                        // ��󶥵���
#define INFINITY 65535                // ��65535�����������

typedef struct
{
    char vexs[MAXVEX];                                // �����
    int arc[MAXVEX][MAXVEX];                // �ڽӾ���
    int numVertexes, numEdges;                // ͼ�е�ǰ�Ķ������ͱ���
} MGraph;

// ����������ͼ���ڽӾ���
void CreateMGraph(MGraph* G)
{
    int i, j, k, w;

    printf("�����붥�����ͱ�����\n");
    scanf("%d %d", &G->numVertexes, &G->numEdges);

    for (i = 0; i < G->numVertexes; i++)
    {
        scanf("%c", &G->vexs[i]);
    }

    for (i = 0; i < G->numVertexes; i++)
    {
        for (j = 0; j < G->numVertexes; j++)
        {
            G->arc[i][j] = INFINITY;                        // �ڽӾ����ʼ��
        }
    }

    for (k = 0; k < G->numEdges; k++)
    {
        printf("�������(Vi,Vj)�ϵ��±�i,�±�j�Ͷ�Ӧ��Ȩw:\n");                // ��ֻ�����ӣ�����û�������Ҫ���и���
        scanf("%d %d %d", &i, &j, &w);
        G->arc[i][j] = w;
        G->arc[j][i] = G->arc[i][j];                        // ��������ͼ���Գƾ���
    }
}