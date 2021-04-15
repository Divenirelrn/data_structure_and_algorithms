#pragma once
#ifndef _HUFFMAN_H
#define _HUFFMAN_H

//霍夫曼树初始化定义
typedef struct _htNode {
    char symbol;
    struct _htNode* left, * right;
}htNode;

/*
        我们将整个树“封装”在一个结构中，因为将来我们可能会添加像“大小”这样的属性，保证可拓展性。
        这样我们不必修改整个源代码。
*/
typedef struct _htTree {
    htNode* root;
}htTree;

//霍夫曼表节点（链表实现）
typedef struct _hlNode {
    char symbol;
    char* code;
    struct _hlNode* next;
}hlNode;

//定义霍夫曼表
typedef struct _hlTable {
    hlNode* first;
    hlNode* last;
}hlTable;

htTree* buildTree(char* inputString);
hlTable* buildTable(htTree* huffmanTree);
void encode(hlTable* table, char* stringToEncode);
void decode(htTree* tree, char* stringToDecode);

#endif
