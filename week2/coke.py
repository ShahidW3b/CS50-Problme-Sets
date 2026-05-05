def main():
    amount_due = 50
    total_inserted = 0

    while total_inserted < amount_due:
        coin = int(input("Insert Coin: "))
        if coin in [25, 10, 5]:
            total_inserted += coin
        if total_inserted < amount_due:
            print("Amount Due:", amount_due - total_inserted)

    print("Change Owed:", total_inserted - amount_due)

if __name__ == "__main__":
    main()
