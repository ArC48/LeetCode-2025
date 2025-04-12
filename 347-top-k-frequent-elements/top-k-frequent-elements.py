class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        bucket_sort = [0] * len(nums)
        for key in counts:
            freq = counts[key]
            if not bucket_sort[freq - 1]:
                bucket_sort[freq - 1] = []
            bucket_sort[freq - 1].append(key)
        
        res = []
        for i in range(len(bucket_sort) - 1, -1, -1):
            if bucket_sort[i]:
                while bucket_sort[i] and k:
                    res.append(bucket_sort[i].pop())
                    k -= 1
        return res