class HashMap:
    """
    self.slots列表用来存储键, self.data列表用来存储值.
    当我们通过键查找值时,键在 self.slots中的index即为值
    在 self.data中的index
    """

    def __init__(self):
        self.size = 12
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))  # 计算 hashvalue

        # 如果 slots当前 hashvalue 位置上的值为None,则将新值插入
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            # 如果 slots 当前 hashvalue 位置上的值为key,则用新值替代旧值
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:  # 如果 slots 当前 hashvalue 位置上的值为其他值的话，则开始探测后面的位置
                # 重新 rehash，实际相当于探测 hashvalue后一个位置
                nextslot = self.rehash(hashvalue, len(self.slots))
                # 如果后一个位置不为空，且不等于当前值即被其他值占用，则继续探测后一个
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                # 如果后一个值为空，则插入；为原来的值，则替换
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    """余数法计算 hashvalue"""

    def hashfunction(self, key, size):
        return key % size

    """使用 +1 法来重新 rehash"""

    def rehash(self, oldhash, size):
        return (oldhash+1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:  # 如果slots当前位置上的值等于 key,则找到了对应的 value
                found = True
                data = self.data[position]
            else:  # 否则的话，rehash后继续搜寻下一个可能的位置
                position = self.rehash(position, len(self.slots))
            if position == startslot:  # 如果最后又回到了第一次搜寻的位置，则要找的 key不在 slots中
                stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
