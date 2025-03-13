class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # constant memory solution
        current_element = nums[0]
        while nums[current_element] > 0:
            curr_idx = current_element
            nums[curr_idx] *= -1
            current_element = -nums[curr_idx]

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] *= -1

        return current_element