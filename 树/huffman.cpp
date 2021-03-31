#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "huffman.h"
#include "pQueue.h"

void traverseTree(htNode* treeNode, hlTable** table, int k, char code[256])
{
    //����������β���������������
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

    //��ڵ㲻Ϊ�գ�����Ϊ0
    if (treeNode->left != NULL)
    {
        code[k] = '0';
        traverseTree(treeNode->left, table, k + 1, code);

    }
    //�ҽڵ㲻Ϊ�գ�����Ϊ1
    if (treeNode->right != NULL)
    {
        code[k] = '1';
        traverseTree(treeNode->right, table, k + 1, code);

    }
}

hlTable* buildTable(htTree* huffmanTree)
{
    //��ʼ����������
    hlTable* table = (hlTable*)malloc(sizeof(hlTable));
    table->first = NULL;
    table->last = NULL;

    //��������
    char code[256];
    //k���������Ȧ��
    int k = 0;

    //����������ڵ�
    traverseTree(huffmanTree->root, &table, k, code);
    return table;
}

htTree* buildTree(char* inputString)
{
    //�����־����Ƶ��
    //������ܴ�С
    //(256 ASCII characters)
    int* probability = (int*)malloc(sizeof(int) * 256);

    //��ʼ������
    for (int i = 0; i < 256; i++)
        probability[i] = 0;

    //���ñ�־��Ϊ����������������ÿ����־���ֵĴ���
    for (int i = 0; inputString[i] != '\0'; i++)
        probability[(unsigned char)inputString[i]]++;

    //�������ڵ�Ķ���
    pQueue* huffmanQueue;
    initPQueue(&huffmanQueue);

    //Ϊ�ַ����е�ÿ����־����ڵ�
    for (int i = 0; i < 256; i++)
        if (probability[i] != 0)
        {
            htNode* aux = (htNode*)malloc(sizeof(htNode));
            aux->left = NULL;
            aux->right = NULL;
            aux->symbol = (char)i;

            addPQueue(&huffmanQueue, aux, probability[i]);
        }

    //�ͷŲ���Ҫ������
    free(probability);

    //����ָ�����贴����
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

    //������
    htTree* tree = (htTree*)malloc(sizeof(htTree));

    tree->root = getPQueue(&huffmanQueue);

    return tree;
}

void encode(hlTable* table, char* stringToEncode)
{
    hlNode* traversal;

    printf("\nEncoding\nInput string : %s\nEncoded string : \n", stringToEncode);

    //��������ÿ��Ԫ��
    //����ҵ���ָ����־
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

    //��ÿ���ֽڽ��н���
    //��ڵ�0���ҽڵ�1
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