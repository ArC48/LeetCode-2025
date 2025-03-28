class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]
        postfixes = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            prefixes.append(prefixes[i] * nums[i])
        
        for i in range(len(nums) - 1, -1, -1):
            postfixes[i] = postfixes[i + 1] * nums[i]

        res = []
        for i in range(len(nums)):
            current = prefixes[i] * postfixes[i + 1]
            res.append(current)

        return res