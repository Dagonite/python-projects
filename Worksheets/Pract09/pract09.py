# Practical Worksheet 9: Using Lists

from graphics import GraphWin, Polygon


# >>> fibonacci + [55, 89]
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# >>> [10, 4] * 3
# [10, 4, 10, 4, 10, 4]


'''1. Using a list, write a function display_date that takes three integer
parameters representing a day, month and year, and outputs the date as a (
readable) string. For example, the call display_date(14, 2, 2011) should
display: 14 Feb 2011. (Hint: put strings representing all the months into a
list, and index this list.) '''


def display_date(day, month, year):
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    month = months[month - 1][:3]
    print(day, month, year)


'''2. Write a function word_lengths that takes a list of strings as a
parameter, and displays each of the words alongside its length. E.g, the call
word_lengths(["bacon", "jam", "spam"]) should result in the following output:

    bacon 5
    jam 3
    spam 4
'''


def word_lengths(words):
    for word in words:
        print(word, len(word))


words = ["bacon", "jam", "spam"]


'''3. Write a function draw_hexagon that allows the user to draw a hexagon (a
shape with six vertices (points)) on a graphics window. The function should
allow the user to click on their chosen locations for the hexagon’s vertices,
and then draw the hexagon (filled in red). (Hint: A hexagon is a Polygon,
and you can make a Polygon object from a list of Point objects.) '''


def draw_hexagon():
    win = GraphWin("Hexagon", 500, 500)
    vertexes = []
    for vertices in range(6):
        vertexes.append(win.getMouse())
        print("That's point", vertices + 1)
    hexagon = Polygon(vertexes[0], vertexes[1],
                      vertexes[2], vertexes[3],
                      vertexes[4], vertexes[5])
    hexagon.setFill("red")
    hexagon.draw(win)


'''4. A test at a university is marked out of 5. Write a function test_marks
that allows a lecturer to input the unit marks of all her students, providing
a suitable way for her to say she’s finished entering marks. The function
should then output the number of students who have achieved each possible
mark. For example, if the lecturer enters the marks 4, 0, 4, 1, 1, 4,
3 and 5, the function should output:

1 student(s) got 0 marks
2 student(s) got 1 marks
0 student(s) got 2 marks
1 student(s) got 3 marks
3 student(s) got 4 marks
1 student(s) got 5 marks
'''


def test_marks():
    marks = []
    while True:
        mark = input("\nEnter a mark ('q' to quit): ")
        mark = mark.replace(" ", "")
        if mark == "" or mark[0] == "q":
            break
        elif mark.isdigit():
            mark = int(mark)
            if mark > 5:
                print("Error: Input out of range")
                continue
            marks.append(mark)
        else:
            print("Error: Invalid input")

    if marks:
        for i in range(6):
            n = marks.count(i)
            print(n, "student(s) got", i, "mark(s)")


'''5. Write a function draw_bar_chart that takes a list of integers as a
parameter, and draws a simple downwards-facing bar chart of # symbols for the
data in the list. For example, the call draw_bar_chart([3, 1, 2]) should
result in the following output:

    # # #
    #   #
    #
'''


def draw_bar_chart1(numbers):
    row_count = 0
    while True:
        row = "".join(
            [" # " if item > row_count else "   " for item in numbers])
        print(row)
        row_count += 1
        if "#" not in row:
            break


def draw_bar_chart2(numbers):
    for row_count in range(max(numbers)):
        row = "".join(
            [" # " if item > row_count else "   " for item in numbers])
        print(row)
