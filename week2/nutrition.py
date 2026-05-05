def main():
    # FDA poster: 20 most frequently consumed raw fruits in the U.S.
    fruits = {
        "apple": 130,
        "banana": 110,
        "grapes": 90,
        "kiwifruit": 90,
        "orange": 80,
        "pear": 100,
        "pineapple": 50,
        "strawberries": 50,
        "watermelon": 80,
        "blueberries": 85,
        "cantaloupe": 50,
        "sweet cherries": 100,
        "peach": 60,
        "plums": 70,
        "nectarine": 60,
        "raspberries": 65,
        "blackberries": 60,
        "lime": 20,
        "lemon": 15,
        "avocado": 50
    }

    fruit_input = input("Fruit: ").strip().lower()

    if fruit_input in fruits:
        print(f"Calories: {fruits[fruit_input]}")

if __name__ == "__main__":
    main()
