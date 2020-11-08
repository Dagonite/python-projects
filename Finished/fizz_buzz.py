def FizzBuzz(x):
    for nmbr in range(1, x + 1):
        output = ""

        if (nmbr % 3 == 0):
            output += "Fizz"

        if (nmbr % 5 == 0):
            output += "Buzz"

        # if (nmbr % 7 == 0):
        #     output += "Tozz"

        if output == "":
            output = nmbr

        print(output)


x = eval(input("Give me the range: "))
FizzBuzz(x)
