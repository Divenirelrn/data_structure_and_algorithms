#include<stdio.h>
#include<stdlib.h>

#define HASHSIZE 12
#define NULLKEY -65535

typedef struct
{
	int* elem; //����Ԫ�صĻ�ַ����̬��������
	int count; //Ԫ�ظ���
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

//ʹ�ó���������
int Hash(int key)
{
	return key % HASHSIZE;
}

//����
void InsertHash(HashTable* H, int key)
{
	int addr;
	addr = Hash(key);

	while (H->elem[addr] != NULLKEY) //�����Ϊ�գ���ͻ����
	{
		addr = (addr + 1) % HASHSIZE; //������ַ��������̽��
	}

	H->elem[addr] = key;
}

//����
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