class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)

        currMax = 0
        for i in range(len(height)):
            leftMax[i] = currMax
            currMax = max(currMax, height[i])
        
        currMax = 0
        for i in range(len(height) - 1, -1, -1):
            rightMax[i] = currMax
            currMax = max(currMax, height[i])

        res = 0
        for i in range(len(height)):
            trapped = min(leftMax[i], rightMax[i]) - height[i]
            if trapped > 0:
                res += trapped
        return res