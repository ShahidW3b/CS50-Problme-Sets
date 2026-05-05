# bank.py
text = input("Greeting:‍‍‍‍‍‍‍‍ ").strip()

if text.startswith("Hello"):
    print("$0")
elif text.startswith("Hello, Newman"):
    print("$0")
elif text.startswith("Hey"):
    print("$20")
elif text.startswith("How you doing?"):
    print("$20")
elif text.startswith("What's happening?"):
    print("$100")
elif text.startswith("What's up?"):
    print("$100")
elif text.startswith("How's it going?"):
    print("$20")

