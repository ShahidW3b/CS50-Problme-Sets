# Prompt the user for input
camel_case = input("camelCase: ")

# an empty string for the converted name
snake_case = ""

# Loop through each character in the input
for char in camel_case:
    if char.isupper():

        snake_case += "_" + char.lower()
    else:

        snake_case += char

# Output the result in snake_case
print("snake_case:", snake_case)
