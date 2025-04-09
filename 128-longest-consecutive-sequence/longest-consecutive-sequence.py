class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        max_seq = 0
        for num in unique_nums:
            if (num - 1) in unique_nums:
                continue

            curr_seq = 1
            while (num + 1) in unique_nums:
                curr_seq += 1
                num += 1
            
            max_seq = max(max_seq, curr_seq)

        return max_seq
