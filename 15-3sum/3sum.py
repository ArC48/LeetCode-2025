class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                summ = nums[left] + num + nums[right]
                if summ == 0:
                    res.append([nums[left], num, nums[right]])
                    right -= 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                elif summ < 0:
                    left += 1
                else:
                    right -= 1
        return res
                