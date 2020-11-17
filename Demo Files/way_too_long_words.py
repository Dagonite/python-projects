################################################################################
# way_too_long_words.py
#
# Program that takes a specified number of words, converting each one if its
# length is strictly more than 10 characters. These long words will be replaced
# with a string starting with the first character of the word and ending with
# the last character of the word. Inbwetween will be the number of letters that
# make up the rest of the word.
################################################################################

def way_too_long_words():
    for i in [0]*int(input("Enter the number of words to convert: ")):
        word = input("Enter a word: ")
        length = len(word) - 2
        print([word, word[0] + str(length) + word[-1]][length > 8])


way_too_long_words()
