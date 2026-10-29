def get_greeting():
    name = input("What is your name? ").strip()

    if not name:
        name = "World"

    return f"Hello, {name}! Welcome to Python."


print(get_greeting())