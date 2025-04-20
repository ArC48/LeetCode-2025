class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr = nums[left] + nums[right] + nums[i]
                if curr == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                elif curr < 0:
                    left += 1
                else:
                    right -= 1

        return result
