#利用前一趟比较结果, o(nlogn)

#完全二叉树

#大顶堆：每个双亲节点大于其孩子节点(升序)
#小顶堆：每个双亲节点小于等于其孩子节点（降序）

#从1开始编号

#将待排序序列构造成一个大顶堆（小顶堆），此时堆顶元素为最大值（最小值）
#将堆顶与末尾元素交换（将最大值放在了数组最后面）
#将剩余的n-1的数组再次构造堆
#......

import math

def swap(i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp


def heapify(l, i, last_idx):
    max = i
    if 2*i <= last_idx and l[2*i] > l[max]:
        max = 2*i

    if 2*i + 1 <= last_idx and l[2*i + 1] > l[max]:
        max = 2*i + 1

    if max != i:
        swap(i, max)
        heapify(l, max, last_idx)


def build_heap(l, last_idx):
    k = math.ceil((last_idx - 2)/2)
    for i in range(k, -1, -1):
        heapify(l, i, last_idx)


def heap_sort(l):
    for i in range(len(l)-1, 0, -1):
        build_heap(l, i)
        swap(0, i)


if __name__ == "__main__":
    l = [10,3,5,6,1,2]
    # build_heap(l, len(l) - 1)
    heap_sort(l)
    print(l)