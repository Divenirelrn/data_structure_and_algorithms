
NULLKEY = -65535

class HashTable:
    def __init__(self, n):
        self.h = [NULLKEY] * n
        self.count = n

    def hash(self, value): #除留余数法
        return value % self.count

    def insert_hash(self, value):
        key = self.hash(value)
        while(self.h[key] != NULLKEY): #冲突解决：开放地址法的线性探测法
            key = (key + 1) % self.count

        self.h[key] = value

    def search_hash(self, value):
        key = self.hash(value)
        while(self.h[key] != value):
            key = (key + 1) % self.count
            if self.h[key] == NULLKEY or key == hash(value):
                return -1

        return key


if __name__ == "__main__":
    ht = HashTable(10)
    ht.insert_hash(12)
    ht.insert_hash(32)
    ht.insert_hash(45)
    ht.insert_hash(20)
    ht.insert_hash(30)
    ht.insert_hash(40)
    ht.insert_hash(135)
    ht.insert_hash(1002)
    print(ht.h)

    print(ht.search_hash(45))
    print(ht.search_hash(135))
    print(ht.search_hash(1002))
    print(ht.search_hash(120))

