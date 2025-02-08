class MyHashMap:

    def __init__(self):
        self.storage = [[], [], [], []]
        self.items_count = 0

    def _get_index(self, key: int, storage_size: int) -> int:
        return key % storage_size

    def resize(self, size: int) -> None:
        new_storage = []
        for _ in range(size):
            new_storage.append([])
        
        for bucket in self.storage:
            for key, value in bucket:
                index = self._get_index(key, len(new_storage))
                new_storage[index].append((key, value))
        self.storage = new_storage

    def put(self, key: int, value: int) -> None:
        index = self._get_index(key, len(self.storage))

        if not self._contains(key):
            self.storage[index].append((key, value))
            self.items_count += 1
            if len(self.storage) * 4 < self.items_count:
                self.resize(len(self.storage) * 4)
        else:
            for i in range(len(self.storage[index])):
                if self.storage[index][i][0] == key:
                    self.storage[index][i] = (key, value)
                    break

    def get(self, key: int) -> int:
        index = self._get_index(key, len(self.storage))

        if self._contains(key):
            for item_key, item_value in self.storage[index]:
                if item_key == key:
                    return item_value
        else:
            return -1

    def remove(self, key: int) -> None:
        index = self._get_index(key, len(self.storage))

        if self._contains(key):
            for i in range(len(self.storage[index])):
                if self.storage[index][i][0] == key:
                    self.storage[index].pop(i)
                    self.items_count -= 1
                    if len(self.storage) // 4 > self.items_count:
                        self.resize(len(self.storage) // 4)
                    break
    
    def _contains(self, key: int) -> bool:
        index = self._get_index(key, len(self.storage))
        for item_key, item_value in self.storage[index]:
            if item_key == key:
                return True
        return False


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)