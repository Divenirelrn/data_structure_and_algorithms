#include "pQueue.h"
#include <stdlib.h>
#include <stdio.h>

void initPQueue(pQueue** queue)
{
    //为优先级队列类型分配内存
    //初始化这些字段的值
    (*queue) = (pQueue*)malloc(sizeof(pQueue));
    (*queue)->first = NULL;
    (*queue)->size = 0;
    return;
}
void addPQueue(pQueue** queue, TYPE val, unsigned int priority)
{
    //如果队列已满，我们不必添加指定的值。
    //返回一个错误信息到控制台
    if ((*queue)->size == MAX_SZ)
    {
        printf("\nQueue is full.\n");
        return;
    }

    pQueueNode* aux = (pQueueNode*)malloc(sizeof(pQueueNode));
    aux->priority = priority;
    aux->val = val;

    // 如果队列为空，增加初始值
    //如果结构在运行时发生异常修改（很少发生），会强制验证两次。
    if ((*queue)->size == 0 || (*queue)->first == NULL)
    {
        aux->next = NULL;
        (*queue)->first = aux;
        (*queue)->size = 1;
        return;
    }
    else
    {
        //如果已经有队列中的元素和元素的优先级，我们要添加大于第一个元素的优先级，将它添加到第一个元素的前面。
        //注意，需要优先级从高到低
        if (priority <= (*queue)->first->priority)
        {
            aux->next = (*queue)->first;
            (*queue)->first = aux;
            (*queue)->size++;
            return;
        }
        else
        {
            //根据优先级寻找节点的位置
            pQueueNode* iterator = (*queue)->first;
            while (iterator->next != NULL)
            {
                //降序，将元素放在头部
                if (priority <= iterator->next->priority)
                {
                    aux->next = iterator->next;
                    iterator->next = aux;
                    (*queue)->size++;
                    return;
                }
                iterator = iterator->next;
            }
            //如果我们到了最后，我们还没有添加元素，将它放到末尾
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
    //只要不为空，从队列中获取元素
    if ((*queue)->size > 0)
    {
        returnValue = (*queue)->first->val;
        (*queue)->first = (*queue)->first->next;
        (*queue)->size--;
    }
    else
    {
        //如果队列为空，打印“队列为空”
        //返回当前内存中的值到returnValue
        printf("\nQueue is empty.\n");
    }
    return returnValue;
}
