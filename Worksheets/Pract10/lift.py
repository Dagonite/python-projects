class Lift:
    def __init__(self, max_floors):
        # set the maximum number of floors (passes as a paramter)
        self.max_no_floors = max_floors
        # set the current floor to the ground (always 0)
        self.current_floor = 0
        # tell the uesr which floor the lift is on
        print("Current floor is: floor ", self.current_floor)

    def go_up(self, target_floor):
        if target_floor > self.max_no_floors:
            print("That is not a valid floor. The lift will not move")
        elif target_floor < self.current_floor:
            print("You need to go down. The lift will not move")
        else:
            floors_to_move = target_floor - self.current_floor
            for i in range(floors_to_move):
                print("Going up: floor number", self.current_floor)
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
                print("Going down: floro number", self.current_floor)
                self.current_floor -= 1
            print("The lift has arrived at floor", self.current_floor)


lift1 = Lift(10)
lift2 = Lift(6)
print()

print("Lift 1 maximum number floors:", lift1.max_no_floors)
print("Lift 2 maximum number floors:", lift2.max_no_floors, "\n")

lift1.go_up(4)
print("Lift 1 current floor:", lift1.current_floor)
print("Lift 2 current floor:", lift2.current_floor, "\n")

lift1.go_up(11)
print("Lift 1 current floor:", lift1.current_floor)
print("Lift 2 current floor:", lift2.current_floor, "\n")

lift1.go_up(2)
print("Lift 1 current floor:", lift1.current_floor)
print("Lift 2 current floor:", lift2.current_floor, "\n")

lift1.go_up(8)
print("Lift 1 current floor:", lift1.current_floor)
print("Lift 2 current floor:", lift2.current_floor, "\n")

lift1.go_down(-5)
print("Lift 1 current floor:", lift1.current_floor)
print("Lift 2 current floor:", lift2.current_floor, "\n")

lift1.go_down(5)
print("Lift 1 current floor:", lift1.current_floor)
print("Lift 2 current floor:", lift2.current_floor, "\n")

lift1.go_down(8)
print("Lift 1 current floor:", lift1.current_floor)
print("Lift 2 current floor:", lift2.current_floor, "\n")

lift2.go_up(4)
print("Lift 1 current floor:", lift1.current_floor)
print("Lift 2 current floor:", lift2.current_floor, "\n")

lift2.go_up(11)
print("Lift 1 current floor:", lift1.current_floor)
print("Lift 2 current floor:", lift2.current_floor, "\n")

lift2.go_up(2)
print("Lift 1 current floor:", lift1.current_floor)
print("Lift 2 current floor:", lift2.current_floor, "\n")

lift2.go_down(-5)
print("Lift 1 current floor:", lift1.current_floor)
print("Lift 2 current floor:", lift2.current_floor, "\n")
