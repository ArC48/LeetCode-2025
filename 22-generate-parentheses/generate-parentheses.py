class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = self.helper("(", n, [], 1, 0)
        return res

    def helper(self, parentheses, n, res, opened, closed):
        if opened < closed : 
            return
        
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

        self.helper(parentheses + "(", n, res, opened+1, closed)
        self.helper(parentheses + ")", n, res, opened, closed+1)

        return res
        