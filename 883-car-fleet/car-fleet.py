class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd = [(position[i], speed[i]) for i in range(len(speed))]
        pos_spd.sort(key=lambda x: x[0])

        stack = []
        stack.append((target - pos_spd[-1][0]) / pos_spd[-1][1])
        for i in range(len(pos_spd) - 2, -1, -1):
            pos, speed = pos_spd[i]
            time = (target - pos) / speed
            if time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)
