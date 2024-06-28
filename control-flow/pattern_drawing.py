# pattern_drawing.py
# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))
# Draw the square pattern using nested loops
for i in range(size):
    for j in range(size):
        print("* ", end="")
    print()
