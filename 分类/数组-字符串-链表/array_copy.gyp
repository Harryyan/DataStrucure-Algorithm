import copy

print("浅拷贝 - - 拷贝数组地址")

# 浅拷贝 -- 拷贝数组地址
list1 = [1, 2, 3, 4]
list3 = list1

list3.append(9)
print(list3)
print(list1)
print(id(list1))
print(id(list3))

print("浅拷贝 - - 数组地址不同，但是共享内容；当内容发生改变再重新分配内存")

# 浅拷贝 -- 拷贝数组内容地址; 数组地址不同，但是共享内容；当内容发生改变再重新分配内存
list2 = [1, 2, 3, [7, 8, 9]]
list4 = list2.copy()  # or list2[:]
print(id(list2[0]))
print(id(list4[0]))
print(list4)
print(id(list2))
print(id(list4))
list4.insert(0, "b")
list4[-1].append("a")
print(list4)
print(list2)
print(id(list2[0]))
print(id(list4[0]))

print("深拷贝 - - 完全分配新内存")

# 深拷贝 - - 完全分配新内存 (但是内部元素一开始还是共享地址)

list5 = ["21", "23112", "ssdafdsf"]
list6 = copy.deepcopy(list5)

print(id(list5))
print(id(list6))

# print(id(list5[2]))
# print(id(list6[2]))
for ele in list5:
    print(id(ele), end=" ")
print("\n")

for ele in list6:
    print(id(ele), end=" ")
print("\n")

list6[-1].append("a")
list6.insert(0, "b")

print(id(list5[0]))
print(id(list6[0]))

print(list5)

print(list2)
