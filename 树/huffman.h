#pragma once
#ifndef _HUFFMAN_H
#define _HUFFMAN_H

//����������ʼ������
typedef struct _htNode {
    char symbol;
    struct _htNode* left, * right;
}htNode;

/*
        ���ǽ�����������װ����һ���ṹ�У���Ϊ�������ǿ��ܻ�����񡰴�С�����������ԣ���֤����չ�ԡ�
        �������ǲ����޸�����Դ���롣
*/
typedef struct _htTree {
    htNode* root;
}htTree;

//��������ڵ㣨����ʵ�֣�
typedef struct _hlNode {
    char symbol;
    char* code;
    struct _hlNode* next;
}hlNode;

//�����������
typedef struct _hlTable {
    hlNode* first;
    hlNode* last;
}hlTable;

htTree* buildTree(char* inputString);
hlTable* buildTable(htTree* huffmanTree);
void encode(hlTable* table, char* stringToEncode);
void decode(htTree* tree, char* stringToDecode);

#endif
