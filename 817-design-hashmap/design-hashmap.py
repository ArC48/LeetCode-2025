class MyHashMap:

    def __init__(self):
        self.storage = [[], [], [], []]

    def _get_index(self, key: int) -> int:
        return key % len(self.storage)

    def put(self, key: int, value: int) -> None:
        index = self._get_index(key)

        if not self._contains(key):
            self.storage[index].append((key, value))
        else:
            for i in range(len(self.storage[index])):
                if self.storage[index][i][0] == key:
                    self.storage[index][i] = (key, value)
                    break

    def get(self, key: int) -> int:
        index = self._get_index(key)

        if self._contains(key):
            for item_key, item_value in self.storage[index]:
                if item_key == key:
                    return item_value
        else:
            return -1

    def remove(self, key: int) -> None:
        index = self._get_index(key)

        if self._contains(key):
            for i in range(len(self.storage[index])):
                if self.storage[index][i][0] == key:
                    self.storage[index].pop(i)
                    return
    
    def _contains(self, key: int) -> bool:
        index = self._get_index(key)
        for item_key, item_value in self.storage[index]:
            if item_key == key:
                return True
        return False


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)