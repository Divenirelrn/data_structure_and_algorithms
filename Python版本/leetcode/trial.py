
l = [[0,1],[4,9],[2,6],[5,7]]
# l.sort(key=lambda x: x[1], reverse=True)
l = sorted(l, key=lambda x: x[1])
print(l)


l2 = [{"name": "liruonan", "age": 18}, {"name": "liruonan3", "age": 20}, {"name": "liruonan2", "age": 16}, {"name": "liruonan7", "age": 20}]
# l2.sort(key=lambda x: x["age"])
l2 = sorted(l2, key=lambda x: x["name"])
print(l2)

key_value = {}

# 初始化
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323

# key_value = sorted(key_value.items(), key=lambda x: x[1], reverse=True)
# print(key_value)

a = [1,2,3,4,5]
b = a.copy()
b[0] = 9
print("a:", a, id(a))
print("b:", b, id(b))

key_value2 = key_value.copy()
key_value2[2] = 100
print("key_value:", key_value)
print("key_value2:", key_value2)