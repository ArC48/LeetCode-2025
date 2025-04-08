class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        bucket_sort = [0] * len(nums)

        for num in counts:
            index = counts[num] - 1

            if not bucket_sort[index]:
                bucket_sort[index] = []
            bucket_sort[index].append(num)

        res = []
        i = len(nums)
        while i and k:
            while bucket_sort[i - 1]:
                res.append(bucket_sort[i - 1].pop())
                k -= 1
                if not k:
                    break
            if not k:
                break
            i -= 1

        return res



