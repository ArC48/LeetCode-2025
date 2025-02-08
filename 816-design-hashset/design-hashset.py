class MyHashSet:

    def __init__(self):
        self.storage = [[], [], [], []]

    def _get_hash(self, key: int) -> int:
        return key % len(self.storage)

    def add(self, key: int) -> None:
        index = self._get_hash(key)

        if not self.contains(key):
            self.storage[index].append(key)

    def remove(self, key: int) -> None:
        index = self._get_hash(key)

        if self.contains(key):
            i = self.storage[index].index(key)
            self.storage[index].pop(i)

    def contains(self, key: int) -> bool:
        index = self._get_hash(key)
        return key in self.storage[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)