class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for elem in tokens:
            if elem in "+-*/":
                m = stack.pop()
                n = stack.pop()
                if elem == "+":
                    res = n + m
                elif elem == "-":
                    res = n - m
                elif elem == "*":
                    res = n * m
                else:
                    res = int(n / m)
                stack.append(res)
            else:
                stack.append(int(elem))

        return stack[-1]