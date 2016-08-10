#	modify script from problem D06ex03 to write results to a file


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

#write to a new file
	new = open('e_roster.txt', 'w')
	new.write("There are " + str(count) + " names with 'e'" + "\n")
	new.write((str(e_roster)))
	new.close

create_list()