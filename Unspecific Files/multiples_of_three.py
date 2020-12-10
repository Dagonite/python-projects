# multiples_of_three.py
# Print all multiples of 3 between 1 and 100

# using a third argument
for n in range(3, 101, 3):
    print(n)

# using modulus
for n in range(1, 101):
    if n % 3 == 0:
        print(n)