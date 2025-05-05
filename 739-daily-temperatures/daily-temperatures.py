class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(0, temperatures[0])]
        result = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            current_t = temperatures[i]

            while stack and stack[-1][1] < current_t:
                prev_index = stack[-1][0]
                days = i - prev_index
                result[prev_index] = days
                stack.pop()

            stack.append((i, current_t))

        return result
            