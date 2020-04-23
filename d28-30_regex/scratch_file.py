import re

def notRegex():
    """Shows examples of when not to use regex"""
    text = "Wow, I love Okinawa"
    print(text.startswith("Wow"))
    print(text.startswith("I love"))
    print(text.endswith("Okinawa"))
    print("I love" in text)
    # Replaces part of string with another
    # Strings are immutable; must be saved to new string
    new_text = text.replace("Okinawa", "America")
    print(new_text)

if __name__ == "__main__":
    notRegex()