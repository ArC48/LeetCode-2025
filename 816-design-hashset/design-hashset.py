class MyHashSet:

    def __init__(self):
        self.storage = [[], [], [], []]
        self.elements_count = 0

    def _get_hash(self, key: int, storage_size: int) -> int:
        return key % storage_size

    def _resize_storage(self, new_size: int) -> None:
        new_storage = []

        # create buckets
        for i in range(new_size):
            new_storage.append([])

        # copy elements
        for bucket in self.storage:
            for element in bucket:
                index = self._get_hash(element, len(new_storage))
                new_storage[index].append(element)

        self.storage = new_storage

    def add(self, key: int) -> None:
        index = self._get_hash(key, len(self.storage))

        if not self.contains(key):
            self.storage[index].append(key)
            self.elements_count += 1
        
            if len(self.storage) * 4 < self.elements_count:
                self._resize_storage(len(self.storage) * 2)

    def remove(self, key: int) -> None:
        index = self._get_hash(key, len(self.storage))

        if self.contains(key):
            i = self.storage[index].index(key)
            self.storage[index].pop(i)
            self.elements_count -= 1

            if len(self.storage) // 4 > self.elements_count:
                self._resize_storage(len(self.storage) // 2)

    def contains(self, key: int) -> bool:
        index = self._get_hash(key, len(self.storage))
        return key in self.storage[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)