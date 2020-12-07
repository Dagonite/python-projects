################################################################################
# is_palindrome_short.py
#
# Checks if a string is a palindrome. This solution requires linear time and
# linear space so isn't the most efficient, however is very concise.
################################################################################


in_file = open("palindromes.txt", "r")
lines = in_file.readlines()
in_file.close()

for line in lines:
    line = "".join([ch for ch in line if ch.isalpha()]) \
             .replace(" ", "").lower()
    print(line, line == line[::-1])
