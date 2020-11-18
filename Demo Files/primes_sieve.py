################################################################################
# primes_sieve.py
#
# Program which prints prime numbers up to a limit. Begins by creating a list
# of size limit and marking 0 and 1 as non-primes. Beginning with 2, all of
# its multiples are labelled false. This is repeated with 3 and then with 5
# and so on until it reaches the end of the list.
#
# Yield is used so the program doesn't crash when large numbers are used.
################################################################################

def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for n in range(i * i, limit, i):
                a[n] = False


primes = primes_sieve(100000)

for n in primes:
    print(n)
