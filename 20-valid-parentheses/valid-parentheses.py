class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif p == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif p == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else: return False
            else:
                stack.append(p)
        return not stack