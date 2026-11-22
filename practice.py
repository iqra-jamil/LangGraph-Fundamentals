from typing import TypedDict
#1. Define the State
class State(TypedDict):
    message: str
    response: str

# Initial State:
{
    "message": "Hello",
    "response": ""
}

# 2. Node reads State
def chatbot(state: State):
    user_message = state["message"]  # read value of message from state

# 3. Node processes the information
    answer = "Hello! How can I help you?"
# 4. Node updates State
    return {"response": answer}


# 5. LangGraph applies the update
# Before the node:
{
    "message": "Hello",
    "response": ""
}

# The node returns:
{
    "response": "Hello! How can I help you?"
}

# After the update:
{
    "message": "Hello",
    "response": "Hello! How can I help you?"
}

# 6.  Next node reads the updated State

def second_node(state: State):
    print(state["message"])
    print(state["response"])

    return {"message": "Goodbye"}
# After this node executes, State becomes:

{
    "message": "Goodbye",
    "response": "Hello! How can I help you?"
}


#ROUTING FUNCTION :
def route(state: State):
    if state["tool_needed"]:
        return "tools"
    else:
        return "end"

graph.add_node("tools", ToolNode(tools))