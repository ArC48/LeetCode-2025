class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                for i in range(len(nums)):
                    nums[i] = abs(nums[i])
                return index + 1
            nums[index] = -nums[index]
        