class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for elem in tokens:
            if elem in "+-*/":
                n, m = stack[-2], stack[-1]
                if elem == "+":
                    res = n + m
                elif elem == "-":
                    res = n - m
                elif elem == "*":
                    res = n * m
                else:
                    res = int(n / m)
                stack.pop()
                stack.pop()
                stack.append(res)
            else:
                stack.append(int(elem))

        return stack[-1]