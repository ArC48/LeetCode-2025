class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            self.move_values()
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            self.move_values()
        return self.s2[-1]

    def empty(self) -> bool:
        return len(self.s1) + len(self.s2) == 0

    def move_values(self) -> None:
        for _ in range(len(self.s1)):
            self.s2.append(self.s1.pop())



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()