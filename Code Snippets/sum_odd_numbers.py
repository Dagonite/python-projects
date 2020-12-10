# sum_odd_numbers.py
# Sum all odd numbers between 1 and 100

total = 0
for n in range(1, 101):
    if n % 2:
        total += n
print(total)

# simplified version
print(sum(range(1, 101, 2)))