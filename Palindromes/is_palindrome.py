################################################################################
# is_palindrome.py
#
# Checks if a string is a palindrome in linear time. Works by using two
# iterators, one at the beginning of the string and one at the end of the
# string. The iterators work their way toward eachother, ignoring non
# alphanumeric characters along the way.
################################################################################


def is_palindrome(line):
    i = 0
    j = len(line) - 1

    while i < j:
        while not line[i].isalnum() and i < j:
            i += 1
        while not line[j].isalnum() and i < j:
            j -= 1

        if line[i].lower() != line[j].lower():
            return False

        i += 1
        j -= 1
    return True


in_file = open("palindromes.txt", "r")
for line in in_file:
    print(line[:-1], is_palindrome(line))
in_file.close()
