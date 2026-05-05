def main():
    # List of month names to numbers
    months = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }

    while True:
        date_input = input("Date: ").strip()

        # Try numeric format: M/D/YYYY
        if "/" in date_input:
            try:
                parts = date_input.split("/")
                if len(parts) != 3:
                    continue
                month, day, year = parts
                month = int(month)
                day = int(day)
                year = int(year)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
            except ValueError:
                continue

        # Try "Month D, YYYY" format
        elif "," in date_input:
            try:
                month_day, year = date_input.split(",")
                year = int(year.strip())
                month_name, day = month_day.strip().split(" ")
                day = int(day)
                month = months.get(month_name)
                if month and 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
            except (ValueError, AttributeError):
                continue

        # Invalid format; prompt again
        else:
            continue


if __name__ == "__main__":
    main()
