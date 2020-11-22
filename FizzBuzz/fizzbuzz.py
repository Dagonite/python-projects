def fizz_buzz(x):
    for n in range(1, x + 1):
        output = ""

        if n % 3 == 0:
            output = "Fizz"

        if n % 5 == 0:
            output += "Buzz"

        print(output or n)


x = int(input("Give me the range: "))
fizz_buzz(x)
