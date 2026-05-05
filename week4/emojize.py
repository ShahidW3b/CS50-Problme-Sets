import re

ALIASES = {
    "1st_place_medal": "🥇",
    "money_bag": "💰",
    "smile_cat": "😸",

    # Earth variants
    "earth_africa": "🌍",
    "earth_americas": "🌎",
    "earth_asia": "🌏",

    "candy": "🍬",
    "ice_cream": "🍨",

    # Thumbs
    "thumbs_up": "👍", "thumbsup": "👍", "+1": "👍",
    "thumbs_down": "👎", "thumbsdown": "👎", "-1": "👎",

    # Faces
    "smile": "😄", "smiley": "😃", "grinning": "😀", "wink": "😉",
    "joy": "😂", "rofl": "🤣", "sweat_smile": "😅", "cry": "😢",
}

PATTERN = re.compile(r":([A-Za-z0-9_+\-]+):")

def emojize_text(s: str) -> str:
    def repl(m: re.Match) -> str:
        key = m.group(1).lower()
        return ALIASES.get(key, m.group(0))
    return PATTERN.sub(repl, s)

def main():
    text = input("Input: ")
    print(f"Output: {emojize_text(text)}")

if __name__ == "__main__":
    main()
