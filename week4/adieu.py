names = []

# Continuously prompt the user for names until Ctrl+D
while True:
    try:
        name = input()
        names.append(name)
    except EOFError:
        break

# If there's only one name
if len(names) == 1:
    print(f"Adieu, adieu, to {names[0]}")

# If there are two names
elif len(names) == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")

# If there are three or more names
else:
    # Join all names except the last with ", "
    beginning = ", ".join(names[:-1])
    # Add ", and" before the last name
    print(f"Adieu, adieu, to {beginning}, and {names[-1]}")
