#include<stdio.h>
#include<stdlib.h>

#define HASHSIZE 12
#define NULLKEY -65535

typedef struct
{
	int* elem; //数据元素的基址，动态分配数据
	int count; //元素个数
}HashTable;

int InitHashTable(HashTable *H)
{
	H->count = HASHSIZE;
	H->elem = (int*)malloc(HASHSIZE * sizeof(int));
	if (!H->elem)
	{
		return -1;
	}
	for (int i = 0; i < HASHSIZE; i++)
	{
		H->elem[i] = NULLKEY;
	}
	return 0;
}

//使用除留余数法
int Hash(int key)
{
	return key % HASHSIZE;
}

//插入
void InsertHash(HashTable* H, int key)
{
	int addr;
	addr = Hash(key);

	while (H->elem[addr] != NULLKEY) //如果不为空，冲突出现
	{
		addr = (addr + 1) % HASHSIZE; //开发定址法的线性探测
	}

	H->elem[addr] = key;
}

//查找
int SearchHash(HashTable H, int key, int *addr)
{
	*addr = Hash(key);
	while (H.elem[*addr] != key)
	{
		*addr = (*addr + 1) % HASHSIZE;
		if (H.elem[*addr] == NULLKEY || *addr == Hash(key))
		{
			return -1;
		}

	}
	return 0;
}