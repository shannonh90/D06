#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1:
#       2:
#       3:
##############################################################################
# Imports

# Body
#part 1

def uses_only(word, string):
	for char in word:
		if char not in string:
			return False
		return True

#part 2
def special_sentence(user_string):
	fin = open("words.txt", "r")
	lines = fin.readlines()

	string_list = list(user_string)
	for word in lines:
		if uses_only(word.strip(), string_list):
			print(word.strip())

#im close, but not quite. 


##############################################################################
def main():
    pass
    special_sentence("acefhlo")

if __name__ == '__main__':
    main()
