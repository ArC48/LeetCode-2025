class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [(temperatures[0], 0)]

        for i in range(1, len(temperatures)):
            t = temperatures[i]

            while stack and stack[-1][0] < t:
                tm, index = stack.pop()
                res[index] = i - index
            stack.append((t, i))
        
        return res

