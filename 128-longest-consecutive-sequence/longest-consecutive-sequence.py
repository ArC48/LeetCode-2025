class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)

        counter = 0

        for num in uniques:
            if num - 1 in uniques:
                continue
            
            curr_counter = 1
            while num + 1 in uniques:
                curr_counter += 1
                num += 1
            
            counter = max(counter, curr_counter)
        
        return counter
