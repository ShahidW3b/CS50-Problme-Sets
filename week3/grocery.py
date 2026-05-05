from collections import Counter

def main():
    items = []

    try:
        while True:
            item = input().strip()
            if item:
                items.append(item.upper())
    except EOFError:
        pass
    counts = Counter(items)

    # Print items sorted alphabetically
    for item in sorted(counts):
        print(counts[item], item)

if __name__ == "__main__":
    main()
