#To write ten numbers to a file, do this in the interpreter:

import random
numbers = random.sample(range(100), 10)
print(numbers)

ten_numbers = open('ten_numbers.txt', 'w')
ten_numbers.write(str(numbers)
ten_numbers.close()

ten_numbers()
# if want to do it the other way:
# with open("ten_numbers.txt", "w") as f:
# 	ten_numbers.write(str(numbers)

