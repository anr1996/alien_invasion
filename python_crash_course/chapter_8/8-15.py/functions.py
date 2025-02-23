def send_messages(message_list, sent_messages):
    print("\n")
    while message_list:
        current_message = message_list.pop()
        print(f"Sending message: {current_message.title()}")
        sent_messages.append(current_message)
    print("\n")
