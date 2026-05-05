def main():
    time = input("What time is it? ")
    time_in_hours = convert(time)

    if 7 <= time_in_hours <= 8:
        print("breakfast time")
    elif 12 <= time_in_hours <= 13:
        print("lunch time")
    elif 18 <= time_in_hours <= 19:
        print("dinner time")


def convert(time):
    # Spliting the input string into hours and minutes
    hours, minutes = time.split(":")
    # Converting hours and minutes to float hours
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60


if __name__ == "__main__":
    main()
