# interpreter.py

def main():
    expression = input("Expression: ").strip()

    try:
        x_str, operator, z_str = expression.split()

        x = int(x_str)
        z = int(z_str)

        if operator == "+":
            result = x + z
        elif operator == "-":
            result = x - z
        elif operator == "*":
            result = x * z
        elif operator == "/":
            result = x / z
        else:
            print("Unsupported operator.")
            return

        print(f"{result:.1f}")

    except ValueError:
        print("Invalid input format.")

if __name__ == "__main__":
    main()
