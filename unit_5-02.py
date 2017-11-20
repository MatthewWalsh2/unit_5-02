# created by Matthew Walsh
# created for ics3u
# created on nov 2017
# finds the max value in an array

from numpy import random

def find_max_value(array = []):
    # finds max value in array
    
    max_number = array[0]
    
    for number in array:
        if max_number < number:
            max_number = number
            
    return max_number

# input
counter = 0
random_numbers = []

while counter < 10:
    number = random.randint(1, 10 + 1)
    print(number)
    random_numbers.append(number)
    counter = counter + 1
        

# process
largest_value = find_max_value(random_numbers)

# output
print("\nThe max value is " + str(largest_value) + ".\n")
