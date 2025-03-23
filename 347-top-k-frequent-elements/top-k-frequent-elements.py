class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        # bucket sort
        buckets = []
        for _ in range(len(nums) + 1): buckets.append([])

        for element, count in counts.items():
            buckets[count].append(element)
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:
                for elem in buckets[i]:
                    result.append(elem)
                    k -= 1
                    if k == 0:
                        break
            if not k:
                break
                
        return result
                