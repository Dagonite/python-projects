########################################################################################
# fibonacci.py
#
# Program which prints out the Fibonacci sequence.
########################################################################################


def fibonacci_sequence(limit):
    a, b = 0, 1
    for i in range(0, limit + 1):
        print(a)
        a, b = b, a + b


fibonacci_sequence(100)
