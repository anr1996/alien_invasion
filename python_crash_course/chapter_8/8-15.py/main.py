from functions import send_messages

current_messages = [
    "how are you?",
    "what time is it?",
    "today is a nice day to go for a walk.",
    "do you like apples and bananas?",
]

sent_messages = []


print(f"\nCurrent messages: {current_messages}\n")
print(f"Sent messages: {sent_messages}")




send_messages(current_messages, sent_messages)  

print(f"Current messages: {current_messages}\n")
print(f"Sent messages: {sent_messages}\n")

