#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports
import os

# Body
def has_no_e(word):
	for letter in word:
		if 'e' in word:
			return False
		return True


def print_no_e():
	f = open("words.txt", "r")
	e_count = 0
	total_count = 0

	for word in f:
		if has_no_e(word):
			e_count += 1
			total_count += 1
			print(word.strip())
		else:
			total_count += 1
	
	percentage = (100*(e_count/total_count))
	print("%d percent of words don't have an 'e.'" %percentage)




##############################################################################
def main():
    pass  
    print_no_e()

if __name__ == '__main__':
    main()
