# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Input validation using a while loop
while size <= 0:
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))

# Draw the square pattern using nested loops
row = 1
while row <= size:
    column = 1
    while column <= size:
        print("* ", end="")
        column += 1
    print()
    row += 1
