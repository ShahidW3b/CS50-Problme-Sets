# figlet.py

import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    # No command-line arguments: choose random font
    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(fonts))

    # Two command-line arguments: must specify font
    elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font") and sys.argv[2] in fonts:
        figlet.setFont(font=sys.argv[2])

    # Any other usage: exit with error
    else:
        sys.exit("Invalid usage")

    text = input("Input: ")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
