# Write a funtion that reads from roster.txt and prints the following information
# to the command line. 
#	a. how many names contain the letter 'e'
#	b. then lists the names which contain the letter 'e' 

import os
# def read_roster():

def create_list():
	f = open("roster.txt", "r")
	e_roster = []
	line = f.readline()

	count = 0

	for line in f:
		firstname = line.split()   #look at only first names, not username
		if "e" in firstname[0] or "E" in firstname[0]:  #make sure you start at first name
			count += 1
			e_roster.append(firstname[0]) 

	f.close()
	print("%d names contain the letter 'e'." %count)
	print(e_roster)


create_list()




