# leetcode 39

def find_number(list):
    half = len(list) // 2
    hash_table = {}
    i = 0

    for item in list:
        if item in hash_table:
            hash_table[item] += 1
        else:
            hash_table[item] = 1

    for key in hash_table:
        if hash_table[key] > half:
            return key

    return None


list = [1, 2, 3, 3, 3, 3, 3, 8]
result = find_number(list)

print(result)
