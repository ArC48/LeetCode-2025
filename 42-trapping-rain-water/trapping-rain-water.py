class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)

        currMax = 0
        for i in range(1, len(height)):
            currMax = max(currMax, height[i - 1])
            leftMax[i] = currMax
        
        currMax = 0
        for i in range(len(height) - 2, -1, -1):
            currMax = max(currMax, height[i + 1])
            rightMax[i] = currMax
        
        res = 0
        for i in range(len(height)):
            minn = min(leftMax[i], rightMax[i])
            trapped = minn - height[i]
            if trapped > 0:
                res += trapped
        return res