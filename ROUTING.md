4. Conditional Routing

Understand:
- What is conditional routing?
- Why do we need it?
- What is a routing function?
- How does a routing function decide the next node?
- How does add_conditional_edges() work?
Goal: Make your graph choose different paths based on conditions.


# What is conditional routing?
- conditional routing means choosing which node should execute based on a condition.
- For example, in a chatbot:
    - If the user asks a normal question, route to the LLM Node.
    - If the LLM requests a tool, route to the Tool Node.

- LangGraph use conditional edges to make these decisions .
- In LangGraph, conditional routing is the decision-making process, and conditional edges are the mechanism or feature used to implement it we implement it using add_conditional_edges().
- in short : conditional edges use hoty hain conditional rendering ko implement krny k liy

# Why do we need it?
- Without it, the graph would always follow the same fixed path, no matter what happens.
- We need it so the graph can make decisions, like retrying a step, picking a different tool, or stopping early.
- This makes the workflow smarter and lets it react to the results of earlier steps.

### Note : the diffrence between node and routing function is that node update the state and routing function tell which node should be execute nxt 


# what is routing function?
- a routing function is a python function that rcv state and chks a condition and decide which node langGraph should execute nxt .

- routing function rcv state, chks conditions and returns a value indicating which Node should execute next.

- for example a routing function wants to chk if an llm want to call a tool or not
     - if yes it returns 'tools' node
     - if no it returns 'end' node

- LangGraph uses the returned value to choose the next Node through add_conditional_edges()


# How does a routing function decide the next node?
- a routing function take the current uodated state as input and chk the conditions in the current state and returns a value that value and identified which node should execute nxt
- LangGraph uses this returned value to determine which Node to execute next through add_conditional_edges()
- Important: The routing function makes the decision. LangGraph handles the actual movement(internally) to the next Node.

#  How does add_conditional_edges() work?
- add_conditional_edges()  connects node to a routing function
- we connect both bcz whn a node finihes its work,then graph needs to ask someone which node should i run nxt 
- the link or the connection between both tell the graph ask which routing function
- When the node ends, the graph runs your routing function with the current state, and the function returns the name of the next node.
- The graph then goes to that node, and you can also give a map of names so the function’s answer points to the right node.
