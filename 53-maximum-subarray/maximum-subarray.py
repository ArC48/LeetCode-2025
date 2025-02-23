class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = nums[0]

        curr = 0
        for num in nums:
            curr += num
            maxx = max(maxx, curr)
            if curr < 0:
                curr = 0
        return maxx

