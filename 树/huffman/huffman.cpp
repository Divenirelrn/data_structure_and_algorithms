#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "huffman.h"
#include "pQueue.h"

void traverseTree(htNode* treeNode, hlTable** table, int k, char code[256])
{
    //遍历到树结尾，往表中添加数据
    if (treeNode->left == NULL && treeNode->right == NULL)
    {
        code[k] = '\0';
        hlNode* aux = (hlNode*)malloc(sizeof(hlNode));
        aux->code = (char*)malloc(sizeof(char) * (strlen(code) + 1));
        strcpy(aux->code, code);
        aux->symbol = treeNode->symbol;
        aux->next = NULL;
        if ((*table)->first == NULL)
        {
            (*table)->first = aux;
            (*table)->last = aux;
        }
        else
        {
            (*table)->last->next = aux;
            (*table)->last = aux;
        }

    }

    //左节点不为空，设置为0
    if (treeNode->left != NULL)
    {
        code[k] = '0';
        traverseTree(treeNode->left, table, k + 1, code);

    }
    //右节点不为空，设置为1
    if (treeNode->right != NULL)
    {
        code[k] = '1';
        traverseTree(treeNode->right, table, k + 1, code);

    }
}

hlTable* buildTable(htTree* huffmanTree)
{
    //初始化霍夫曼表
    hlTable* table = (hlTable*)malloc(sizeof(hlTable));
    table->first = NULL;
    table->last = NULL;

    //辅助变量
    char code[256];
    //k保存遍历的圈数
    int k = 0;

    //遍历树计算节点
    traverseTree(huffmanTree->root, &table, k, code);
    return table;
}

htTree* buildTree(char* inputString)
{
    //计算标志出现频率
    //计算可能大小
    //(256 ASCII characters)
    int* probability = (int*)malloc(sizeof(int) * 256);

    //初始化数组
    for (int i = 0; i < 256; i++)
        probability[i] = 0;

    //将该标志视为数组索引，并计算每个标志出现的次数
    for (int i = 0; inputString[i] != '\0'; i++)
        probability[(unsigned char)inputString[i]]++;

    //保存树节点的队列
    pQueue* huffmanQueue;
    initPQueue(&huffmanQueue);

    //为字符串中的每个标志创造节点
    for (int i = 0; i < 256; i++)
        if (probability[i] != 0)
        {
            htNode* aux = (htNode*)malloc(sizeof(htNode));
            aux->left = NULL;
            aux->right = NULL;
            aux->symbol = (char)i;

            addPQueue(&huffmanQueue, aux, probability[i]);
        }

    //释放不需要的数组
    free(probability);

    //按照指定步骤创建树
    while (huffmanQueue->size != 1)
    {
        int priority = huffmanQueue->first->priority;
        priority += huffmanQueue->first->next->priority;

        htNode* left = getPQueue(&huffmanQueue);
        htNode* right = getPQueue(&huffmanQueue);

        htNode* newNode = (htNode*)malloc(sizeof(htNode));
        newNode->left = left;
        newNode->right = right;

        addPQueue(&huffmanQueue, newNode, priority);
    }

    //创建树
    htTree* tree = (htTree*)malloc(sizeof(htTree));

    tree->root = getPQueue(&huffmanQueue);

    return tree;
}

void encode(hlTable* table, char* stringToEncode)
{
    hlNode* traversal;

    printf("\nEncoding\nInput string : %s\nEncoded string : \n", stringToEncode);

    //遍历表中每个元素
    //输出找到的指定标志
    for (int i = 0; stringToEncode[i] != '\0'; i++)
    {
        traversal = table->first;
        while (traversal->symbol != stringToEncode[i])
            traversal = traversal->next;
        printf("%s", traversal->code);
    }

    printf("\n");
}

void decode(htTree* tree, char* stringToDecode)
{
    htNode* traversal = tree->root;

    printf("\nDecoding\nInput string : %s\nDecoded string : \n", stringToDecode);

    //对每个字节进行解码
    //左节点0，右节点1
    for (int i = 0; stringToDecode[i] != '\0'; i++)
    {
        if (traversal->left == NULL && traversal->right == NULL)
        {
            printf("%c", traversal->symbol);
            traversal = tree->root;
        }

        if (stringToDecode[i] == '0')
            traversal = traversal->left;

        if (stringToDecode[i] == '1')
            traversal = traversal->right;

        if (stringToDecode[i] != '0' && stringToDecode[i] != '1')
        {
            printf("The input string is not coded correctly!\n");
            return;
        }
    }

    if (traversal->left == NULL && traversal->right == NULL)
    {
        printf("%c", traversal->symbol);
        traversal = tree->root;
    }

    printf("\n");
}