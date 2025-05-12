class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd = [(position[i], speed[i]) for i in range(len(speed))]
        pos_spd.sort(key=lambda x: x[0])

        fleets = 1
        current_fleet_time = (target - pos_spd[-1][0]) / pos_spd[-1][1]
        for i in range(len(pos_spd) - 2, -1, -1):
            p, s = pos_spd[i]
            time = (target - p) / s
            if time > current_fleet_time:
                current_fleet_time = time
                fleets += 1
            
        return fleets