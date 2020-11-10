# Practical Worksheet 1: Getting started with Python

def say_hello():
    print("Hello world")


def count():
    for i in range(10):
        print(i)


def kilos_to_pounds():
    kilos = eval(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print("The weight in pounds is", pounds)


'''
1.
Write a function called say_name that displays your name.
'''
def say_name():
    print("John Doe")


'''
2. Write a say_hello2 function that uses two print statements to display the
text:
    Hello
    World
'''
def say_hello2():
    print("Hello")
    print("World")


'''
3.
Write a function euros_to_pounds which converts an amount in Euros entered
by the user to a corresponding amount in Pounds. Assume that the exchange rate
is 1.15 Euros to the Pound. (Hint: be sure to test your solution carefully.)
'''
def euros_to_pounds():
    euros = eval(input("Enter an amount in euros: "))
    pounds = euros / 1.108
    print("The amount in pounds is", pounds)


'''
4.
Write an add_up function that asks the user to enter two numbers, and outputs
their sum.
'''
def add_up():
    first_nmbr = eval(input("Gimme a number: "))
    second_nmbr = eval(input("Gimme another number: "))
    total = first_nmbr + second_nmbr
    print("The sum of them is", total)


'''
5. Write a change_counter function. This should ask the user how many 1p, 2p
and 5p coins they have (using three separate questions), and then display the
total amount of money in pence. (Hint: remember that variable names cannot begin
with a digit, so you might like to use names like two_pence.)
'''
def change_counter():
    one_pence = eval(input("How many 1p coins do you have? "))
    two_pence = eval(input("How many 2p coins do you have? "))
    five_pence = eval(input("How many 5p coins do you have? "))
    total_pence = one_pence + two_pence * 2 + five_pence * 5
    print("The sum of your coins is", total_pence, "pence")


'''
6.
Write a ten_hellos function that uses a loop to display “hello, world!” ten times
(on separate lines).
'''
def ten_hellos():
    for i in range(10):
        print("hello, world")


'''
7.
Change the count function so that instead of counting from 0 to 9, it counts up
from 1 to 10. (Hint: Use a little arithmetic in the print statement.)
'''
def count2():
    for i in range(10):
        print(i + 1)


'''
8. [harder]
Write a function weights_table that outputs a two-column table of kilogram weights
and their pound equivalents for kilogram values 0, 10, 20 ... 100. (Don’t worry
too much about formatting the table neatly.)
'''
def weights_table():
    for i in range(11):
        print(i * 10, i * 22)


'''
9. [harder]
Write a future_value function that uses a loop to calculate the future value of
an investment amount, assuming an annual interest rate of 5.5%. The function should
ask the user for the initial amount and the number of years that it is to be
invested, and should output the final value of the investment using compound interest
with the interest compounded every year.
'''
def future_value():
    investment = eval(input("What is your investment amount? "))
    years = eval(input("Years of investment? "))
    interest_rate = .055
    return_amount = investment
    for year in range(years):
        return_amount *= (1 + interest_rate)
    print("Investing GBP {0:0.2f} for {1} years".format(investment, years),
          "will result in GBP {0:0.2f}.".format(return_amount))
