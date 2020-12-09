"""7. Create a class to model a combination padlock, called ”Padlock”. The object
should be created with a combination as the parameter __init__(self, combination). It
is assumed that the padlock is locked when it is created. The user should be able to 
open the lock open_lock(self, entered_combination), and close it again 
close_lock(self). Additionally, the user should be able to change the combination
change_combination(self, new_combination). However, the combination can only be
changed once the padlock is open, and the new code should be of the same length as the
previous one. Hint: in the constructor, create an additional instance variable 
self.combination_no_digits to support fixing the length of the combination."""


class Padlock:
    def __init__(self, combination):
        self.combination = combination
        self.combination_no_digits = len(combination)
        self.locked = True

    def open_lock(self, entered_combination):
        if self.locked:
            if self.combination == entered_combination:
                self.locked = False
                print("Lock opened with", entered_combination)
            else:
                print("Wrong combination")
        else:
            print("Lock already opened")

    def close_lock(self):
        if not self.locked:
            self.locked = True
            print("Lock closed")
        else:
            print("Lock is already closed")

    def change_combination(self, new_combination):
        if not self.locked:
            if len(new_combination) == self.combination_no_digits:
                self.combination = new_combination
                print("Combination changed to", new_combination)
            else:
                print("Different combination lengths, try again")
        else:
            print("Combination can't be changed whilst padlock is closed")


padlock1 = Padlock([5, 4, 9])
padlock1.open_lock([5, 4, 9])
padlock1.change_combination([8, 3, 4])
padlock1.open_lock([8, 3, 4])
padlock1.close_lock()
padlock1.close_lock()
padlock1.open_lock([5, 4, 9])
padlock1.change_combination([8, 3, 4])
padlock1.open_lock([8, 3, 4])
padlock1.change_combination([8, 3, 4, 3])
