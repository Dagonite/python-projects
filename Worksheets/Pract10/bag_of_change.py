'''
8.
Create a class called ”BagOfChange”, which will model a collection of coins
(1p, 2p, 5p, 10p, 20p, 50p, £1, £2). The constructor will take the quantity of
each coin as individual parameters and convert them into a single list
__init__(self, pence1, pence2, pence5, pence10, pence20, pence50, pound1, pound2).
You will need to include methods to allow users to:

take a specific coin out remove_coin(self, coin);
add a specific coin into the collection add_coin(self, coin);
calculate the total number of coins total_no_coins(self);
and calculate the total value of the coins in the collection total_value(self).

Hint: for the remove_coin and add_coin methods, you may need to create an
additional instance variable in the constructor self.coins =
[1,2,5,10,20,50,100,200] which you can use to help you find the relevent index.
'''


class BagOfChange:
    def __init__(self, pence1, pence2, pence5, pence10, pence20, pence50, pound1, pound2):
        self.bag_of_change = [pence1, pence2, pence5, pence10,
                              pence20, pence50, pound1, pound2]
        self.coins = [1, 2, 5, 10, 20, 50, 100, 200]

    def remove_coin(self, coin):
        if coin in self.coins:
            coin_index = self.coins.index(coin)

            if self.bag_of_change[coin_index] > 0:
                self.bag_of_change[coin_index] -= 1
                print(str(coin) + "p", "coin removed from the bag")
            else:
                print("No", str(coin) + "p coins in the bag to remove")

        else:
            print(str(coin) + "p coin does not exist")

    def add_coin(self, coin):
        if coin in self.coins:
            coin_index = self.coins.index(coin)
            self.bag_of_change[coin_index] += 1
            print(str(coin) + "p coin added to the bag")
        else:
            print(str(coin) + "p coin does not exist")

    def total_no_coins(self):
        return self.bag_of_change

    def total_value(self):
        # note: could have map lambda here instead
        value = sum([a*b for a, b in zip(self.bag_of_change, self.coins)])
        return f"Sum of coins in bag: £{value/100:.2f}"


bag1 = BagOfChange(2, 3, 1, 4, 2, 5, 11, 3)
print(bag1.total_value())
bag1.remove_coin(5)
bag1.remove_coin(8)
bag1.remove_coin(5)
bag1.remove_coin(20)
bag1.remove_coin(20)
bag1.add_coin(20)
bag1.add_coin(18)
bag1.add_coin(100)
print(bag1.total_no_coins())
print(bag1.total_value())
