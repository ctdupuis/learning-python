name = "Cody"
age = 10 + 15

print("name: " + name)
print("age: " + str(age))


## Booleans
# True and False must be capitalized
truthy = True
falsy = False

# similar to ==
5 is 5 #=> True
5 is not 5 #=> False
5 is not 6 #=> True 

"This" is "This" #=> True
True is True #=> True
"True" is True #=> False
"True" is str(True) #=> True


## Lists 
# Lists are just Arrays

entertainment = ["Movies", "Games", "Music"]
print(entertainment[1])

numbers = [1,2,3]
print(numbers[0])


## Dictionaries
# Dictionaries are Hashes or Objects

myself = {
    "name": {
        "first": "Cody",
        "last": "Dupuis"
    },
    "age": 25,
    "employed": True,
    "languages": ["Ruby", "JavaScript", "Python"]
}

print(myself["name"]["last"])
print(myself["age"])


## Built-in Functions

# Print a string
print("string")

# Convert to a String
str(6)

# Convert to an Integer
int("6")

# Convert to a Float
float("6.0")

# Convert to a Boolean
bool("True")

# Returns the length of an array or string
len([1,2,3]) #length

# Returns an array sorted
sorted([2,3,1])

# Numbers get first priority, then capital letters, then lowercase letters
sorted(["a", "B", "C", "d", "5", "6.5"]) 


## Defining Functions

# Define function
# Functions aren't closed by an end keyword, they are run based on indentation
def print_string(string):
    print(string)

# Using default arguments
def introduce_yourself(name, age = 25):
    print("My name is", name, "and I am", age, "years old")

# Call function
print_string("string")

# Using keyword arguments 
# (name = "Cody") == (name: "Cody")
introduce_yourself(name = "Cody")

# Functions with flexible number of arguments
# Each indentation is another block of code
def print_people(*people):
    for person in people:
        print("This person is", person)

print_people("Cody", "Miah")


## Return values

def do_math(num1, num2):
    return num1 + num2

math1 = do_math(1, 3) #=> 4


## If Statements

check = False

if check == False:
    print("It is False")
elif check == True: 
    print("It is actually True")
else: 
    print("It is not a Boolean")


## Loops

# For
numbers = [1,2,3]

for number in numbers:
    print(number)

# While
run = True
current = 1

while run:
    if current == 100:
        run = False
    else:
        print(current)
        current += 1


## Importing Libraries

# re is a regex library
import re

string = "'I AM NOT YELLING', she said. Though we knew it not to be true"

# Replace all capital letters, punctuation, and whitespace
new_string = re.sub('[A-Z./,+" "]', '', string)