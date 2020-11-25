################################################################################
# word_capitalization.py
#
# Program that asks the user for a word and capitalizes it, ignoring letters
# (aside from the first) that are already capitalized.
################################################################################

def word_capitalization():
    string = input("Enter a word: ")
    print(string[0].upper() + string[1:])


word_capitalization()
