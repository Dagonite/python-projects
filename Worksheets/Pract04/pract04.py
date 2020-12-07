# Practical Worksheet 4: Strings and Files

from graphics import GraphWin, Line, Point, Rectangle, Text


def numerical_encoding_of_characters():
    print()
    print("Numerical encoding of characters")
    print("--------------------------------")
    print(ord("a"))
    print(ord("b"))
    print(ord("A"))
    print(ord("z"))
    print(ord("b") - ord("a") + 1)
    print(ord("z") - ord("a") + 1, "\n")

    print("chr does the opposite of ord")
    print("----------------------------")
    print(chr(98))
    print(chr(120))
    print(chr(960))
    print(chr(8364))


# Reading files ([:-1] removes the new line after every paragraph)
def read_file():
    in_file = open("quotation.txt", "r")
    contents = in_file.read()
    print(contents)
    in_file.close()


def readlines_file():
    in_file = open("quotation.txt", "r")
    contents = in_file.readlines()
    print(contents)
    in_file.close()


def readline_file():
    in_file = open("quotation.txt", "r")
    line = in_file.readline()
    print(line[:-1])
    in_file.close()


def sequence_file():
    in_file = open("quotation.txt", "r")
    for line in in_file:
        print(line[:-1])
    in_file.close()


# Writing files
def create_file():
    out_file = open("my_file.txt", "w")
    print("Hello world!", file=out_file)
    print(42, file=out_file)
    print("Goodbye world!", file=out_file)
    out_file.close()


'''1. Write a personal_greeting function which, after asking for the user’s
name, outputs a personalised greeting. E.g., for user input Sam, the function
should output the greeting Hello Sam, nice to see you! (note the details of
the spaces and punctuation). '''


def personal_greeting():
    first_name = input("Enter your first name: ")
    print("Hello", first_name + ", nice to see you!")


'''2. Write a formal_name function which asks the user to input his/her given
name and family name, and then outputs a more formal version of their name.
E.g. on input Sam and Brown, the function should output S. Brown (again note
the spacing and punctuation). '''


def formal_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print(first_name[0] + ".", last_name)


'''3. Copy the kilos_to_pounds conversion function from your pract01.py file.
Modify this function so that its output takes the form of a message such as
“12.34 kilos is equal to 27.15 pounds”, where both the user’s kilos value and
the calculated pounds values are displayed to two decimal places. '''


def kilos_to_pounds():
    kilos = eval(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print("{0:0.2f} kilos is equal to {1:0.2f} pounds".format(kilos, pounds))


'''4. Suppose the University decides that students’ email addresses should be
made up of the first 4 letters of their surname, the first letter of their
forename, and the final two digits of the year they entered the university,
separated by dots. Write a function called generate_email that outputs an
email address given a student’s details. (E.g., if the user enters the
following information: Sam, Brown and 2015, the function should output:

    brow.s.15@myport.ac.uk
'''


def generate_email():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    entry_year = input("Enter the year you joined: ")
    email = (last_name[0:4] + "." + first_name[0] + "." +
             entry_year[2:] + "@myport.ac.uk").lower()
    print(email)


'''
5.
A teacher awards letter grades for test marks as follows: 8, 9 or 10 marks
give an A, 6 or 7 marks give B, 4 or 5 marks give C, and 0, 1, 2 or 3 marks all
give F. Using string indexing, write a function grade_test which asks the user
for a mark (between 0 and 10) and displays the corresponding grade.
'''


def grade_test():
    mark = eval(input("Enter your mark between 0 and 10: "))
    grade = "FFFFCCBBAAA"
    print("Your grade is", grade[mark])


'''6. Write a function graphic_letters which first asks the user to enter a
word, opens a graphics window, and then allows the user to display the
letters of the word at different locations by clicking the mouse once for
each letter. (Use the setSize method of the Text class to make the letters
appear big.) '''


def graphic_letters():
    word = input("Enter a word: ")
    win = GraphWin("Letters")

    for ch in word:
        position = win.getMouse()
        message = Text(position, ch)
        message.setSize(20)
        message.draw(win)


'''7. Write a sing_a_song function which outputs a “song” based on a single
word. The user should be asked for the song’s word, how many lines long the
song should be, and how many times the word should be repeated on each line.
For example, if the user enters the word “dum” and the numbers 2 and 4,
the function should then output the following song (note that the spaces are
important): dum dum dum dum dum dum dum dum '''


def sing_a_song():
    word = input("Enter the song's word: ")
    lines = eval(input("Enter how many lines long the song is: "))
    repeats = eval(input("Enter how many times the word is repeated on each "
                         "line: "))

    for i in range(lines):
        for j in range(repeats):
            if j == repeats - 1:
                print("{:8}".format(word))
            else:
                print("{:8}".format(word), end="")


'''8. Write a function exchange_table that gives a table of euros values and
their equivalent values in pounds, using an exchange rate of 1.108 euros to
the pound. The euros values should be 0, 1, 2, . . . , 20, and should be
right justified. The pounds values should be 6 right justified and given to
two decimal places (i.e. with decimal points lined up and with pence values
after the points). '''


def exchange_table():
    for euros in range(21):
        pounds = euros / 1.108
        print("{0:2} {1:6.2f}".format(euros, pounds))


'''9. Write a make_acronym function that allows the user to enter a phrase,
and then displays an acronym (the first letters of the words in capitals) for
that phrase. For example, if the user enters “University of Portsmouth”,
the function should display UOP. (Hint: first use the split method to find
the words in the inputted string.) '''


def make_acronym():
    phrase = input("Enter the phrase: ").upper()
    words = phrase.split()
    for i in range(len(words)):
        current_word = words[i]
        print(current_word[0], end="")


'''10. [harder] Write a name_to_number function that asks the user for their
name and converts it into a numerical value by adding up the “values” of its
letters (where ‘a’ is 1, ‘b’ is 2, . . . ‘z’ is 26). So, for example,
“Sam” has the value 19 + 1 + 13 = 33. '''


def name_to_number():
    first_name = input("Enter your first name: ").lower()
    number = 0
    for ch in first_name:
        number += ord(ch) - 96
    print(number)


'''11. Write a file_in_caps function which displays the contents of a file in
capital letters. The name of the input file should be entered by the user. '''


def file_in_caps():
    out_file = open("Battles - Atlas.txt", "w")
    print("People won't be people\nWhen they hear this sound\nThat's been "
          "glowing in the dark at the edge of town", file=out_file)
    out_file.close()

    text_file = input("Enter the text file you want to use (try Battles - "
                      "Atlas): ")
    in_file = open(text_file + ".txt", "r")
    for line in in_file:
        print(line[:-1].upper())
    in_file.close()


'''12. [harder] The file rainfall.txt from the unit web-site contains
rainfall data in mm for several UK cities for a particular day, in the form:

    Portsmouth 9
    London 5
    Southampton 12

Write a function rainfall_chart that displays this data as a textual bar
chart using one asterisk for each mm of rainfall; e.g., given the above data
the output should be:

    Portsmouth  *********
    London      *****
    Southampton ************
'''


def rainfall_chart():
    in_file = open("rainfall.txt", "r")
    for line in in_file:
        city = line.split()[0]
        print("{0:14}".format(city), end="")
        rainfall = int(line.split()[1])
        print("*" * rainfall)
    in_file.close()


'''Now write a graphical version graphical_rainfall_chart that displays a
similar bar chart in a graphical window but uses filled rectangles instead of
sequences of asterisks. '''


def graphical_rainfall_chart():
    win = GraphWin("Rainfall Chart", 1100, 300)
    y_axis = Line(Point(50, 50), Point(50, 260))
    y_axis.draw(win)

    x_axis = Line(Point(50, 260), Point(1050, 260))
    x_axis.draw(win)

    colours = ["red", "green", "orange", "blue", "white",
               "yellow", "black", "brown", "gray"]

    in_file = open("rainfall.txt", "r")
    item = 0
    for line in in_file:
        city = Text(Point((item + 1) * 100, 270), line.split()[0])
        city.draw(win)
        current_rainfall = int(line.split()[1])
        rectangle = Rectangle(Point((item + .5) * 100, 260 - current_rainfall * 3.7),
                              Point((item + 1.5) * 100, 260))
        rectangle.setFill(colours[item])
        rectangle.draw(win)
        item += 1

    for i in range(6):
        rainfall = Text(Point(30, 255 - i * 36), i * 10)
        rainfall.draw(win)

    in_file.close()


'''10. [harder] Write a rainfall_in_inches function that reads the rainfall
data from rainfall.txt, and outputs the data to a file rainfall_inches.txt
where all the mm values are converted to inches (there are 25.4mm in an
inch). The inch values should be given to two decimal places, so the
Portsmouth line above will become:

    Portsmouth 0.35
'''


def rainfall_in_inches():
    in_file = open("rainfall.txt", "r")
    out_file = open("rainfall_inches.txt", "w")
    for line in in_file:
        city = line.split()[0]
        print("{0:14}".format(city), end="", file=out_file)
        rainfall = int(line.split()[1])
        print("{0:0.2f}".format(rainfall / 25.4), file=out_file)
    out_file.close()
    in_file.close()


'''11. [harder] In Linux, there is a command called wc which reports the
number of characters, words and lines in a file. Write a function wc which
performs the same task. The name of the file should be entered by the user. '''


def wc():
    text_file = input("Enter the text file you want to use (try Battles - "
                      "Atlas): ")
    in_file = open(text_file + ".txt", "r")

    contents = in_file.read()
    characters = contents.count("")
    print("There are", characters, "characters in this file")

    words = len(contents.split())
    print("There are", words, "words in this file")

    lines = sum(1 for line in open(text_file + ".txt"))
    print("There are", lines, "lines in this file")
    in_file.close()
