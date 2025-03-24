class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        bucket_sort = []
        for i in range(len(nums) + 1): bucket_sort.append([])

        for key, value in hashmap.items():
            bucket_sort[value].append(key)

        result = []
        for i in range(len(bucket_sort) - 1, 0, -1):
            while bucket_sort[i] and k:
                result.append(bucket_sort[i].pop())
                k -= 1
            if not k:
                break
        
        return result

        