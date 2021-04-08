import os


class OrderedList(object):
    def __init__(self):
        super(OrderedList, self).__init__()
        self.__data = list()
        self.__length = 0

    def __len__(self):
        return self.__length

    def getList(self):
        return self.__data

    def getElem(self, idx):
        """获取元素"""
        if(self.__length == 0 or idx < 1 or idx > self.__length):
            return -1
        return self.__data[idx-1]

    def insertElem(self, idx, elem):
        """插入元素"""
        if(idx < 1 or idx > self.__length + 1):
            return -1

        if(idx == self.__length + 1): #在表尾
            self.__data.append(elem)
        else: #不在表尾
            self.__data.append(self.__data[self.__length - 1])
            for i in range(self.__length - 1, idx - 1, -1):
                self.__data[i] = self.__data[i-1]
            self.__data[idx-1] = elem

        self.__length += 1
        return 0

    def deleteElem(self, idx):
        """删除元素"""
        if(idx < 1 or idx > self.__length):
            return -1

        delElem = self.__data[idx-1]

        for i in range(idx - 1, self.__length - 1):
            self.__data[i] = self.__data[i+1]
        self.__data.pop()

        self.__length -= 1

        return delElem


if __name__ == "__main__":
    ol = OrderedList()
    ol.insertElem(0,10)
    ol.insertElem(1,20)
    ol.insertElem(2,30)
    ol.insertElem(3,40)
    ol.insertElem(4,50)
    ol.insertElem(5,60)
    print(ol.getList())
    print(len(ol))

    res = ol.getElem(6)
    print("get:", res)

    ol.deleteElem(0)
    ol.deleteElem(3)
    print(ol.getList())
    print(len(ol))



