def vibe_check():
    messages = [
    ("positive"),
    ("negative"),
    ("neutral"),
]
    name = input("Enter your username. ")
    age = int(input("Enter your age. "))
    talk = input("What do you wanna talk about? (2 sentences max). ").lower()
    if "love" in talk:
        print(messages[0])
    elif "hate" in talk:
        print(messages[1])
    elif "okay" in talk:
        print(messages[2])
vibe_check()