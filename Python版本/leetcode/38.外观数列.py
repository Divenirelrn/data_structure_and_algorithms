
class Solution:
    def countAndSay(self, n: int) -> str:
        item = "1"

        for _ in range(1, n):
            temp = ""
            count = 1
            len_item = len(item)
            i = 0
            while i < len_item:
                while i < len_item-1 and item[i] == item[i+1]:
                    count += 1
                    i += 1

                temp += str(count) + item[i]

                i += 1
                count = 1
            item = temp

        return item