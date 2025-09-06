class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd = [(position[i], speed[i]) for i in range(len(position))]
        pos_spd.sort(key=lambda x: x[0])

        last_speed = (target - pos_spd[-1][0]) / pos_spd[-1][1]
        fleets = 1

        for i in range(len(pos_spd) - 2, -1, -1):
            current_speed = (target - pos_spd[i][0]) / pos_spd[i][1]
            if current_speed > last_speed:
                fleets += 1
                last_speed = current_speed

        return fleets

