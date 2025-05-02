class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = self.helper("", n, [])
        return res

    def helper(self, parentheses, n, res):
        if len(parentheses) == n * 2:
            opened = 0
            closed = 0

            for char in parentheses:
                if char == "(":
                    opened += 1
                else:
                    closed += 1
                if closed > opened:
                    return
            if opened == closed:
                res.append(parentheses)
            return

        left = self.helper(parentheses + "(", n, res)
        right = self.helper(parentheses + ")", n, res)

        return res
        