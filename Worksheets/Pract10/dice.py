'''4.
Create a class called ”Dice”. This class will be used to simulate throwing a
dice, with the side labels defined by the user when the dice is created
__init__(self, side_labels) - where side_labels is a list of any length. The
constructor should also have a variable which calculates the number of sides on
the dice (you should be able to get this from the length of the list). The class
will need one method, throw_dice(self), which simulates throwing the dice, and
returns the side it lands on.
'''


class Dice:
    def __init__(self, side_labels):
        self.side_labels = side_labels
        self.sides = len(side_labels)

    def throw_dice(self):
        from random import choice

        return choice(self.side_labels)


dice1 = Dice([1, 2, 3, 4, 5, 6])
print("Die 1 has", dice1.sides, "sides")
for i in range(5):
    print("Roll", str(i+1) + ":", dice1.throw_dice())

print()

dice2 = Dice([3, 3, 4, 4, 5, 6])
print("Die 2 has", dice2.sides, "sides")
for i in range(5):
    print("Roll", str(i+1) + ":", dice2.throw_dice())

print()

dice3 = Dice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
print("Die 3 has", dice3.sides, "sides")
for i in range(5):
    print("Roll", str(i+1) + ":", dice3.throw_dice())
