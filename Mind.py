def analyze_sentiment(talk):
    positive_count = talk.count("love") + talk.count("enjoy") + talk.count("like")
    negative_count = talk.count("hate") + talk.count("dislike") + talk.count("bad")
    if positive_count > negative_count:
        return "positive"
    elif negative_count > positive_count:
        return "negative"
    elif positive_count == 0 and negative_count == 0:
        return "unknown"
    elif positive_count == negative_count:
        return "neutral"
def vibe_check():
    messages = [
    ("positive"),
    ("negative"),
    ("neutral"),
]
    name = input("Enter your username. ")
    age = int(input("Enter your age. "))
    talk = input(f"What do you wanna talk about, {name}? ").lower()
    result = analyze_sentiment(talk)
    if result == "positive":
        print(messages[0])
    elif result == "negative":
        print(messages[1])
    elif result == "unknown":
        print("I do not possess the ability to classify that yet. ")
    elif result == "neutral":
        print(messages[2])
    
vibe_check()