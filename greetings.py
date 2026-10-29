def get_user_name():
   
    name = input("Assistant: Hi! I'm Mini Alexa. What's your name? ").strip()

    if not name:
        name = "User"

    return name


def build_greeting(name):
   
    return (
        f"Assistant: Nice to meet you, {name}! "
        "Type 'help' to see what I can do."
    )
