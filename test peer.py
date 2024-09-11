from lab_chat import get_peer_node, join_group, get_channel

#Functions:

def get_username():
    username = input("Enter Username: ").strip()
    return username.upper()

def get_group():
    group = input("Join Group: ").strip()
    return group.upper()

def get_message():
    message = input("Input Message: ").strip()
    return message

def initialize_chat():
    username = get_username()
    group = get_group()
    node = get_peer_node(username)
    join_group(node,group)
    chat_channel = get_channel(node,group)
    print(f"{username}joined{group}")
    return chat_channel

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")

#print(get_username(),get_group(),get_message())
#print(type(initialize_chat()))
print(start_chat())
