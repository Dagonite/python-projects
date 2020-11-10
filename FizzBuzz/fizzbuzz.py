def fizz_buzz(x):
    for n in range(1, x + 1):
        output = ""

        if (n % 3 == 0):
            output += "Fizz"

        if (n % 5 == 0):
            output += "Buzz"

        # if (nmbr % 7 == 0):
        #     output += "Tozz"

        if output == "":
            output = n

        print(output)


x = eval(input("Give me the range: "))
fizz_buzz(x)
