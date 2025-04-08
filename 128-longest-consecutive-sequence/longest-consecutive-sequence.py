class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)

        max_seq = 0

        for num in uniques:
            if num - 1 in uniques:
                continue
            
            curr_seq = 0
            while num in uniques:
                curr_seq += 1
                max_seq = max(max_seq, curr_seq)
                num += 1
        
        return max_seq