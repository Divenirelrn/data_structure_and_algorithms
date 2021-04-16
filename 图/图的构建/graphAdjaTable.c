//ͼ���ڽӱ�

#define MAXVEX 100

typedef struct EdgeNode                        // �߱���
{
    int adjvex;                                        // �ڽӵ��򣬴洢�ö����Ӧ���±�
    int weight;                                        // ���ڴ洢Ȩֵ�����ڷ���ͼ���Բ���Ҫ
    struct EdgeNode* next;                // ����ָ����һ���ڽӵ�
} EdgeNode;

typedef struct VertexNode                // �������
{
    char data;                                        // �����򣬴洢������Ϣ
    EdgeNode* firstEdge;                // �߱�ͷָ��
} VertexNode, AdjList[MAXVEX];

typedef struct
{
    AdjList adjList;
    int numVertexes, numEdges;        // ͼ�е�ǰ�������ͱ���
} GraphAdjList;

// ����ͼ���ڽӱ�ṹ
void CreateALGraph(GraphAdjList* G)
{
    int i, j, k;
    EdgeNode* e;

    printf("�����붥�����ͱ�����\n");
    scanf("%d %d", &G->numVertexes, &G->numEdges);

    // ��ȡ������Ϣ�����������
    for (i = 0; i < G->numVertexes; i++)
    {
        scanf("%c", &G->adjList[i].data);
        G->adjList[i].firstEdge = NULL;                // ��ʼ����Ϊ�ձ�
    }

    for (k = 0; k < G->numEdges; k++)
    {
        printf("�������(Vi,Vj)�ϵĶ�����ţ�\n");
        scanf("%d %d", &i, &j);

        e = (EdgeNode*)malloc(sizeof(EdgeNode));
        e->adjvex = j;                                                // �ڽ����Ϊj
        e->next = G->adjList[i].firstEdge;
        G->adjList[i].firstEdge = e;

        e = (EdgeNode*)malloc(sizeof(EdgeNode));
        e->adjvex = i;                                                // �ڽ����Ϊi
        e->next = G->adjList[j].firstEdge;
        G->adjList[j].firstEdge = e;
    }
}