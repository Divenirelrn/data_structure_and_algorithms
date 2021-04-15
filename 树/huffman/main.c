//霍夫曼编码main文件

#include <stdio.h>
#include <stdlib.h>
#include "huffman.h"

int main(void)
{
    //根据字符串建立树
    htTree* codeTree = buildTree("beep boop beer!");
    //根据霍夫曼树建立表格
    hlTable* codeTable = buildTable(codeTree);

    //使用霍夫曼表进行编码
    encode(codeTable, "beep boop beer!");
    //使用霍夫曼树
    //对初始字符串的符号进行解码
    decode(codeTree, "0011111000111");
    //输出 : 0011 1110 1011 0001 0010 1010 1100 1111 1000 1001
    return 0;
}