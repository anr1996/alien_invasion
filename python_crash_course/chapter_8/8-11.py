current_messages = [
    "how are you?",
    "what time is it?",
    "today is a nice day to go for a walk.",
    "do you like apples and bananas?",
]

sent_messages = []


print(f"\nCurrent messages: {current_messages}\n")
print(f"Sent messages: {sent_messages}")

  

def send_messages(message_list):
    print("\n")
    while message_list:
        current_message = message_list.pop()
        print(f"Sending message: {current_message.title()}")
        sent_messages.append(current_message)
    print("\n")


send_messages(current_messages[:])  

print(f"Current messages: {current_messages}\n")
print(f"Sent messages: {sent_messages}\n")


