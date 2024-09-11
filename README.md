def get_peer_node(username):    # function name is get_peer_node
    username: This is the user's username
The get_peer_node function probably returns your peer's username, the function appears to set both the user's username 
and the username of the person they are talking to as headers at the top of the chat window. 

def join_group(node, group):    # function name is join_group
    node: this is the peer to peer node of the group being connected to
    group: this is the name of the group being connected to
The join_group function does not return anything, it appears to write print "Joined group:" followed by the name of the 
group being connected to when the connection is established. 

def chat_task(ctx, pipe, n, group):    # function name is chat_task
    ctx: This is a ZeroMQ Connection Context(not sure)
    pipe: This is a communications pipe polled by ZeroMQ for messages.(not sure)
    n: This is the peer to peer node my chat app is connected as
    group: This is the peer chat group I wanted to join
The chat_task method does not return anything, it appears to be the send/recieve manager.

def get_channel(node, group)    # function name is get_channel
    node:this is the peer to peer node of the channel being connected to
    group:this is the group the channel is a part of, or maybe vice versa
this function returns something but im not sure what it is, the function appears to connect you to a channel 


