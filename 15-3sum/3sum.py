class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        res = set()
        for i, num in enumerate(nums):
            if num in seen:
                continue
            seen.add(num)
            r = self.twoSum(i, nums, -num)
            if r:
                for elem in r:
                    res.add(tuple(sorted(elem)))
        return list(res)


    def twoSum(self, startIndex, nums, target) -> List[int]:
        seen = set()
        used = set()
        res = []
        for i in range(startIndex + 1, len(nums)):
            if nums[i] in used:
                continue
            need = target - nums[i]
            if need in seen:
                res.append([-target, need, nums[i]])
                used.add(nums[i])
            seen.add(nums[i])
        return res
