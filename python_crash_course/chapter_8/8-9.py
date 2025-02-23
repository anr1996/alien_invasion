list_messages = [
    "how are you?",
    "what time is it?",
    "today is a nice day to go for a walk",
    "do you like apples and bananas?",
]

def show_messages(message_list):
    print("\n")
    for message in message_list:
        print(f"{message.title()}\n")


show_messages(list_messages) # call function show_messages to print messages in list.

