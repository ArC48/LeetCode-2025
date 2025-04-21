class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxx = 0
        while left < right:
            water = (right - left) * min(height[left], height[right])
            maxx = max(maxx, water)
            if height[left] <= height[right]:
                current = height[left]
                while height[left] <= current and left < right:
                    left += 1
            elif height[left] > height[right]:
                current = height[right]
                while height[right] <= current and left < right:
                    right -= 1
        return maxx
                