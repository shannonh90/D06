#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: 598
#   - # of words that use all aeiouy: 42
##############################################################################
# Imports

# Body
with open('words.txt', 'r') as fin:
	word_list = fin.read().split()

def uses_all(word, string):
	count = 0
	for letter in string:
		if letter in word:
			count += 1
	if count == len(string):
		return True
	return False

def find_uses_all_vowels(list):
	count = 0
	string = 'aeiou'
	for word in list:
		if uses_all(word, string):
			count += 1
			print(word)
	return count

print(find_uses_all_vowels(word_list))

#change string if you want to include y




##############################################################################
def main():
    pass  # Call your function(s) here.

if __name__ == '__main__':
    main()
