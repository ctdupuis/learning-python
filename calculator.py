import re

print("Python Calculator")
print("Type 'quit' to exit.")

previous = 0
run = True

def perform_math():
    global run
    # equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))

        
    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-Z,.;:()+" "]', "", equation)
        previous = eval(equation)
        print(previous)

while run:
    perform_math()