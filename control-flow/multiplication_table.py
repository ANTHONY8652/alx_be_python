# Prompt the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))

# Initialize the loop counter
i = 1

# Use a while loop to generate and print the multiplication table
while i <= 10:
    product = number * i
    print(f"{number} * {i} = {product}")
    i += 1  # Increment the loop counter
