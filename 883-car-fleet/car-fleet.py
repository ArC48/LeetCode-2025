class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [ (target - car[0]) / car[1] for car in cars ]
        fleets = 1
        curr_fleet_time = times.pop()
        while times:
            time = times.pop()
            if time > curr_fleet_time:
                fleets += 1
                curr_fleet_time = time

        return fleets

