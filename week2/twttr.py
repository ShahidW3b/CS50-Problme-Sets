# Prompt the user for input
text = input("Enter text: ")

# Create a string of vowels
vowels = "aeiouAEIOU"

# Build the output by omitting vowels
result = ""
for char in text:
    if char not in vowels:
        result += char

# Print the result
print(result)

