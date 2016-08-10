# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(nestedlists):
	""" calculates total of all numbers in a list of lists
	t: list of list of numbers
	"""
	total = 0
	for numbers in nestedlists:
		if type(numbers) == int:
			total += numbers
		else:
			total += nested_sum(numbers) 
	return total


##############################################################################
def main():
	print(nested_sum([1,2,[7]]))
	print(nested_sum([1,2,4,[5,6],[8,9,10]]))

if __name__ == '__main__':
    main()