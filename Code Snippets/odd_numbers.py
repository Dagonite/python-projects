# odd_numbers.py
# Print all odd numbers between 1 and 100

# using a third argument
for n in range(1, 101, 2):
    print(n)

# using modulus
for n in range(1, 101):
    if n % 2:
        print(n)

# using a bitwise operator
for n in range(1, 101):
    if n & 1:
        print(n)