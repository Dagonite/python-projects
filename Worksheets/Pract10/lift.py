"""1. Using the Lift class created during the introduction, add an additional method
which can be used to call the lift call_lift(self, floor_called_from). Note: your
method should make use of both the go_up, and go_down methods"""


class Lift:
    def __init__(self, max_floors):
        self.max_no_floors = max_floors
        self.current_floor = 0  # ground floor is floor 0
        print("Current floor is: floor", self.current_floor)

    def go_up(self, target_floor):
        if target_floor > self.max_no_floors:
            print("That is not a valid floor. The lift will not move")
        elif target_floor < self.current_floor:
            print("You need to go down. The lift will not move")
        else:
            floors_to_move = target_floor - self.current_floor
            for i in range(floors_to_move):
                print("Going up: floor", self.current_floor)
                self.current_floor += 1
            print("The lift has arrived at floor", self.current_floor)

    def go_down(self, target_floor):
        if target_floor < 0:
            print("This is not a valid floor. The lift will not move")
        elif target_floor > self.current_floor:
            print("You need to go up. The lift will not move")
        else:
            floors_to_move = self.current_floor - target_floor
            for i in range(floors_to_move):
                print("Going down: floor", self.current_floor)
                self.current_floor -= 1
            print("The lift has arrived at floor", self.current_floor)

    def call_lift(self, floor_called_from):
        if floor_called_from > self.current_floor:
            self.go_up(floor_called_from)
        elif floor_called_from == self.current_floor:
            print("Already on floor", floor_called_from)
        else:
            self.go_down(floor_called_from)


lift1 = Lift(10)
print("Lift called to floor 5")
lift1.call_lift(5)
