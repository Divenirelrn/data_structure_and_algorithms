//����������main�ļ�

#include <stdio.h>
#include <stdlib.h>
#include "huffman.h"

int main(void)
{
    //�����ַ���������
    htTree* codeTree = buildTree("beep boop beer!");
    //���ݻ��������������
    hlTable* codeTable = buildTable(codeTree);

    //ʹ�û���������б���
    encode(codeTable, "beep boop beer!");
    //ʹ�û�������
    //�Գ�ʼ�ַ����ķ��Ž��н���
    decode(codeTree, "0011111000111");
    //��� : 0011 1110 1011 0001 0010 1010 1100 1111 1000 1001
    return 0;
}