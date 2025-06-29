class Solution:
    class CarState:
        def __init__(self, position, speed):
            self.position = position
            self.speed = speed
            self.distance = 0

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        size = len(position)

        cars = []
        for i in range(size):
            cars.append(self.CarState(position[i], speed[i]))
        
        cars.sort(key=lambda c: c.position, reverse=True)

        stk = []  
        for i in range(size):
            cur_car = cars[i]
            cur_car.distance = (target - cur_car.position) / cur_car.speed
            if not stk:
                stk.append(cur_car)
            else:
                pre_car = stk[-1]
                if cur_car.distance > pre_car.distance:
                    stk.append(cur_car)
        
        return len(stk)