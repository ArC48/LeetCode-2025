class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            diff = target - num
            left = i + 1
            right = len(numbers) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] > diff:
                    right = mid - 1
                elif numbers[mid] < diff:
                    left = mid + 1
                else:
                    return [i + 1, mid + 1]
