def main():
    answer = input("What is the answer to the Great question of life, the universe, and everything? ")
    answer = answer.strip().lower()
    if answer == "42" or answer == "forty two" or answer == "forty-two":
        print("Yes")

    else:
        print("NO")

if __name__ == "__main__":
    main()

