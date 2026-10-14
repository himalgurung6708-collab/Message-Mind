def vibe_check():
    messages = [
    ("positive"),
    ("negative"),
    ("neutral"),
]
    name = input("Enter your username. ")
    age = int(input("Enter your age. "))
    talk = input(f"What do you wanna talk about, {name}? ").lower()
    positive_count = talk.count("love")
    negative_count = talk.count("hate")
    if positive_count > negative_count:
        print(messages[0])
    elif negative_count > positive_count:
        print(messages[1])
    elif positive_count == 0 and negative_count == 0:
        print("I do not possess the ability to classify that yet. ")
    elif positive_count == negative_count:
        print(messages[2])
    
vibe_check()