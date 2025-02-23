current_messages = [
    "how are you?",
    "what time is it?",
    "today is a nice day to go for a walk.",
    "do you like apples and bananas?",
]

sent_messages = []


print(f"\nCurrent messages: {current_messages}\n")
print(f"Sent messages: {sent_messages}")

  

def send_messages(message_list, messages_sent):
    
    """retrieve a list of messages that need to be sent and an empty list to store the sent messages
    in. copy one message at a time while removing it from the first list. print a message
    stating that the message is sending."""
    
    print("\n")
    while message_list:
        current_message = message_list.pop()
        print(f"Sending message: {current_message.title()}")
        messages_sent.append(current_message)
    print("\n")


send_messages(current_messages, sent_messages)  

print(f"Current messages: {current_messages}\n")
print(f"Sent messages: {sent_messages}\n")






