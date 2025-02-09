class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            curr = nums[i]
            missing = target - curr
            if missing in seen:
                return [seen[missing], i]
            else:
                seen[curr] = i
        
