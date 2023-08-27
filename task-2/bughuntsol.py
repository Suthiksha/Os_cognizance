def calc_average(numbers):
    total = 0
    count = 0         # here it is not double equal because we are asiigning 0 to count not checking whether count is equal to 0 or not.

    for num in numbers:
        total += num
        count += 1  
    avg = total / count # here the formula to calculate the average is total/ count where contain the number of numbers in numbers list
    return avg

# Test the function
nums = [10, 20, 30, 40, 50]
result = calc_average(nums)
print("Average:", result)   #here the variable that stores the average is result not resul
# Check if the average is even or odd
if result % 2 ==0:  #here we are checking the condition wheher result is even or odd and not assigning . so double equal should come 
    print("The average is even")
else:
    print("The average is odd")

# Generate a list of squares
squares = [num ** 2 for num in nums] # here for the list the closing square parenthesis is not there
print("Squares:", squares)

# Find the maximum square
max_square = max(squares)
print("Maximum square:", max_square)  #here the varaiable name that stores the maximum square is max_square but here the variable wrong 

# Search for a specific square
target_square = 900
if target_square in squares: #: is missing
    print("Target square found at index:", squares.index(target_square))  
else:
    print("Target square not found")

# Concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Combined list:", combined_list)

# Remove duplicates from the list
unique_list = list(set(combined_list))  
print("Unique list:", unique_list)

# Create a dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("Person's name:", person['name'])
print("Person's gender:", person.get('gender', 'Unknown'))  

# Update the person's age
person['age'] = 26
print("Updated age:", person['age']) # here in person['age) the closing squaring bracket is missing

# Add a new key-value pair
person['job'] = 'Engineer'

# Delete the city key
del person['city'] #the key city is a string datatype so should enclosed inside strings

# Print all key-value pairs in the dictionary
for key, value in person.items(): #here the items is a method and not an attribute so should include parenthesis
    print(key + ': ' + str(value))

# Check if person is from London
#if person['city'] == 'London':  #here it is a condition and not an assignment statement. so it should double equal and city key is not present
  #  print("Person is from London")

# Calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:      #: is missing
        return n * factorial(n-1)  

print("Factorial of 5:", factorial(5))

# Create a list of numbers
numbers = range(10)
print("Numbers:", numbers) # the list name is numbers not number

# Print each number in the list
for num in numbers: # : is missing
    print(num)  

# Define a class for a car
class Car:     # for defining class use :
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def info(self):
        print("Car:", self.make, self.model)  # here make and model are instance variable so should call with self

my_car = Car("Toyota", "Corolla")
my_car.info()

# Access class attributes directly
print("Car make:", my_car.make)
print("Car model:", my_car.model)

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)
#my_tuple[0] = 10  #tuples are immutable

# Open a file for writing
file = open('my_file.txt', 'w')
file.write("Hello, world!") #closing parenthesis is  missing

# Close the file
file.close() #it is a method so should include parenthesis

# Find the length of a string
message = "Hello, world!"
length = len(message) #to find length of a string correct method is len() not str.len()

# Convert a string to uppercase
uppercase_message = message.upper() #upper is a method
print("Uppercase message:", uppercase_message)

# Split a sentence into words
sentence = "This is a sentence"
words = sentence.split( ) #there is no comma in sentence so use space as separator
print("Words:", words)

# Define a function to calculate the power of a number
def power(base, exponent):
    result = base ** exponent
    return result

# Calculate the power of 2 to the 3
print("2^3:", power(2, 3))

# Use a list as a stack
stack = []
stack.append(1)  #no push method in python for stack
stack.append(2)
stack.append(3)
print("Stack:", stack)

# Pop elements from the stack
print(stack.pop())
print(stack.pop())

# Attempt to pop from an empty stack
if len(stack)>0:
    print(stack.pop()) #poping an empy stack will return error

    

# Use a dictionary as a switch-case
def switch_case(case):
    return {
        'a': "Case a",
        'b': "Case b",
        'c': "Case c",
    }.get(case, "Invalid case")

print(switch_case('b'))  # Output: Case b
print(switch_case('d'))  # Output: Invalid case


try:
    with open('data.txt', 'r') as file:
        content = file.read()
    print("File content:", content)
except FileNotFoundError:
    print("The file 'data.txt' was not found.")     #Use try except if file not founfd it with throw error
except Exception as e:
    print("An error occurred:", str(e))


# Close the file
file.close()

# Attempt to read from a closed file

#print(file.read())     #trying to read a file that is closed will throw error

# Perform division
numerator = 10
denominator = 0
if denominator != 0:
    result = numerator / denominator  #wrong variable name denominaotr and denominator should not be zero
else:
    result=0
    


# Print the result
print("Result:", result)

# Use a while loop to count from 1 to 5
count = 1
while count <= 5: # : is missing
    print(count)
    count += 1

# Print the sum of the numbers from 1 to 10
sum = 0
for i in range(11):
    sum += 1

print("Sum:", sum)

# Access elements of a list using an invalid index
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  #invalid index 10 

# Define a function that takes a default argument
def greet(name, greeting="Hello"):
    print(greeting, name)

greet("Alice")

# Swap two variables
a = 5
b = 10
a, b = b, a  

# Use an invalid escape sequence in a string
invalid_string = r"This is an \q invalid escape sequence"  #this is an invalid escape sequence

# Print the invalid string
print(invalid_string)

# Use an invalid operator
x = 10
y = 3
result = x / y   #// is invalid operator

# Print the result
print("Result:", result)
