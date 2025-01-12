class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniques = set()
        for num in nums:
            if num in uniques:
                return True
            else:
                uniques.add(num)
        return False