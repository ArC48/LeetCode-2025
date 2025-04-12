class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * (len(nums) + 1)
        postfixes = [1] * (len(nums) + 1)

        for i in range(1, len(nums)):
            curr = prefixes[i - 1] * nums[i - 1]
            prefixes[i] = curr
        
        for i in range(len(nums) - 1, -1, -1):
            curr = postfixes[i + 1] * nums[i]
            postfixes[i] = curr
        
        res = []
        for i in range(len(nums)):
            curr = prefixes[i] * postfixes[i + 1]
            res.append(curr)

        return res