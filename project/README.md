10. Build One Simple Agent

Build an agent that:
- Accepts a user's question.
- Uses an LLM.
- Has access to one or two tools.
- Decides when to call a tool.
- Receives tool results.
- Generates a final response.
- Stops when the task is complete.


This is the workflow of **LangGraph** (the graph part of LangChain). The steps in order:

1. **Define the state**, the shared data the graph carries.
2. **Write the node functions.** Each takes the state and returns a dict with the updates. You don't pass the state yourself; the graph passes it in when it runs the node.
3. **Create the graph** with `StateGraph`, giving it your state class.
4. **Register each node** with `add_node`, giving it a name and its function. 
5. **Connect the nodes with edges** using `add_edge`. Connect `START` to your first node, each node to the next, and the last node to `END`. For routing decisions you use `add_conditional_edges` instead.
6. **Compile the graph** with `compile`. This turns your design into something runnable.
7. **Run graph** with `invoke`, passing the initial state.


Updated workflow:

Define the state.
Define tools with @tool (if you use tools), and give them to the model so it knows they exist.(no need to write tool schema)
Write node functions (the LLM node takes state, returns updates).
Create the graph with StateGraph.
Register nodes with add_node (include a ToolNode for the tools).
Add add_edge from START to the first node.
Add add_conditional_edges from the LLM node, using tools_condition as the routing function.
Add add_edge from the tool node back to the LLM node, so the LLM can read the tool result.
Compile the graph.
Run it with invoke.


# CONFUSIONS
# WHAT IS THE DIFFERENCE BETWEEN add_edge and add_conditonal_edges (routing functon)
- add_edge doesen't involve routing function at all it dont use the nodes returned by a routing function its fixed it goes from Node A to node B and up to so on
- the node returned by the routing function is used by add_conditional_edges not add_edge
- add_conditional_edges connect the node to the routing function and a routing function looks at the state and return a node that should execute nxt and the path is decided at the run time 
- so when we say add_conditional_edges connect the node to the routing function we mean when node A finishes run this routing function and go to the node returned by that routing function 
- Use **`add_edge`** when the next step is always the same. Example: `START` always goes to your first node, or the tool node always goes back to the LLM node.

- Use **`add_conditional_edges`** when the next step depends on the state and could be different each time. Example: after the LLM node, go to the tool node if the LLM asked for a tool, otherwise go to `END`.
- @tool: a decorator that turns a normal function into a tool the LLM can request.
- ToolNode: a ready-made node that runs the tool the LLM asked for and returns the result as a ToolMessage.
- tools_condition: a ready-made routing function. If the LLM's last message asks for a tool, it returns the tool node. If not, it returns END.

# difference between history.add_message(...) and add_messages

- history.add_message(...) is a method on chat history object like AI messages,human msgs etc we call it manually ourself at the moment we want to store a message
- add_message is a reducer function used in state definition ,wenever call it ourself langgraph call it automatically whenever a node returns messages ,to merge the returned messages into the state 

Both do the same job of appending messages to a history, but in the first you do it by hand, and in the second LangGraph does it for you because nodes can only return updates.


# LangChain Vs LangGraph
- **LangChain** is a library of building blocks for working with LLMs: models (like `ChatGroq`), messages, prompts, tools, and chains that run steps one after another.

- **LangGraph** is built on top of LangChain and is used to control the **flow** between steps. It lets you define a state, nodes, and edges, so you can add decisions, loops, and tool calls (like the agent loop where the LLM calls a tool and then goes back to the LLM).

In short: LangChain gives you the pieces, LangGraph decides the order they run in.

# Annotated from typping module :
- without Annotated, LangGraph only sees list and uses its default, which is replace. With it, LangGraph sees add_messages and appends.
- it allows us to attach extra metadata to a type without chianging the actual type

# get outside things by passing them as arguments
The rule "get outside things by passing them as arguments" applies to normal functions that you call, because you decide what goes in. Nodes and tools are different: they are called by something else, so you can't add arguments freely.

# Note: In both cases, anything else (like model or the API key) is read from the global scope.

# tools_condition and add_conditional_edges 
- tools_condition checks the LLM's last message and returns the next node's name: the tool node if the LLM asked for a tool, or END if it's a plain answer.
- add_conditional_edges takes that returned name and sends the graph there