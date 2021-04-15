#include "pQueue.h"
#include <stdlib.h>
#include <stdio.h>

void initPQueue(pQueue** queue)
{
    //Ϊ���ȼ��������ͷ����ڴ�
    //��ʼ����Щ�ֶε�ֵ
    (*queue) = (pQueue*)malloc(sizeof(pQueue));
    (*queue)->first = NULL;
    (*queue)->size = 0;
    return;
}
void addPQueue(pQueue** queue, TYPE val, unsigned int priority)
{
    //����������������ǲ������ָ����ֵ��
    //����һ��������Ϣ������̨
    if ((*queue)->size == MAX_SZ)
    {
        printf("\nQueue is full.\n");
        return;
    }

    pQueueNode* aux = (pQueueNode*)malloc(sizeof(pQueueNode));
    aux->priority = priority;
    aux->val = val;

    // �������Ϊ�գ����ӳ�ʼֵ
    //����ṹ������ʱ�����쳣�޸ģ����ٷ���������ǿ����֤���Ρ�
    if ((*queue)->size == 0 || (*queue)->first == NULL)
    {
        aux->next = NULL;
        (*queue)->first = aux;
        (*queue)->size = 1;
        return;
    }
    else
    {
        //����Ѿ��ж����е�Ԫ�غ�Ԫ�ص����ȼ�������Ҫ��Ӵ��ڵ�һ��Ԫ�ص����ȼ���������ӵ���һ��Ԫ�ص�ǰ�档
        //ע�⣬��Ҫ���ȼ��Ӹߵ���
        if (priority <= (*queue)->first->priority)
        {
            aux->next = (*queue)->first;
            (*queue)->first = aux;
            (*queue)->size++;
            return;
        }
        else
        {
            //�������ȼ�Ѱ�ҽڵ��λ��
            pQueueNode* iterator = (*queue)->first;
            while (iterator->next != NULL)
            {
                //���򣬽�Ԫ�ط���ͷ��
                if (priority <= iterator->next->priority)
                {
                    aux->next = iterator->next;
                    iterator->next = aux;
                    (*queue)->size++;
                    return;
                }
                iterator = iterator->next;
            }
            //������ǵ���������ǻ�û�����Ԫ�أ������ŵ�ĩβ
            if (iterator->next == NULL)
            {
                aux->next = NULL;
                iterator->next = aux;
                (*queue)->size++;
                return;
            }
        }
    }
}

TYPE getPQueue(pQueue** queue)
{
    TYPE returnValue;
    //ֻҪ��Ϊ�գ��Ӷ����л�ȡԪ��
    if ((*queue)->size > 0)
    {
        returnValue = (*queue)->first->val;
        (*queue)->first = (*queue)->first->next;
        (*queue)->size--;
    }
    else
    {
        //�������Ϊ�գ���ӡ������Ϊ�ա�
        //���ص�ǰ�ڴ��е�ֵ��returnValue
        printf("\nQueue is empty.\n");
    }
    return returnValue;
}
