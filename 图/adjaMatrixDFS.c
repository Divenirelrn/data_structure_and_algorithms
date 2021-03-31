// �ڽӾ����������޵ݹ��㷨
// �ڽӾ���Ĵ������������ʮ����Դ���벿��
// ��C������(www.fishc.com)

#define TRUE 1
#define FALSE 0
#define MAX 256

typedef int Boolean;        // �������Ƕ���BooleanΪ�������ͣ���ֵΪTRUE��FALSE
Boolean visited[MAX];        // ���ʱ�־������

void DFS(MGraph G, int i)
{
    int j;

    visited[j] = TRUE;                        // ���ʹ��Ķ�������ΪTRUE
    printf("%c ", G.vexs[i]);        // ��ӡ����
    for (j = 0; j < G.numVertexes; j++)
    {
        if (G.arc[i][j] == 1 && !visited[j])
        {
            DFS(G, j);                        // ��Ϊ���ʵ��ڽӶ���ݹ����
        }
    }
}

// �ڽӾ������ȱ�������
void DFSTraverse(MGraph G)
{
    int i;

    for (i = 0; i < G.numVertexes; i++)
    {
        visited[i] = FALSE;                // ��ʼ�����ж���״̬����δ���ʹ�״̬
    }

    for (i = 0; i < G.numVertexes; i++)
    {
        if (!visited[i])                // ������ͨͼ��ֻ��ִ��һ��
        {
            DFS(G, i);
        }
    }
}