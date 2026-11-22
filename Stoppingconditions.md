8. Stopping Conditions

Understand:
- How does an agent know when to stop?
- What is END?
- How do conditional edges determine when execution ends?
- What happens when an agent reaches its iteration limit?
- How can you prevent endless execution?
Goal: Make sure your agent terminates at the right time.


# How does an agent know when to stop?
- aik agent tab stop hota hai jab LLM k response main koi tool call na ho
- After every LLM setup routing chk which is tools_condition looks at the resposne of an LLM,if the resposne contain a tool call the graph will move to the tool node and if the resposne dont contain a toool call it will have a simple plain anser then the Graph will move to the END node and execution stops
- so the llm itself decide it is done by answering instead of asking for a tool
# What is END?
- END is a special built in marker in langGraph to tell that Graph is finished 
- the Node we mark as END retrn the final state

# How do conditional edges determine when execution ends?
- conditional edges uses routing function to determine when execution ends
- routing function is the one that takes state and return where to go nxt(which node should execute nxt)
- one of the possible destination id END node
- ager routing function daikhta h k stoping condition jo hai wo true hai means for example llm ka las resposne final ans h koi tool call nai h to matlab task complete ho gia h the routing function will then return END node and graph stops
- and if condtion false hoti h to ruting function will return anyother node that is not marked as END and the graph will continue
- so the routing function take the decision and END is the destination it picks when work is finished

# What happens when an agent reaches its iteration limit?
- LangGraph has a built-in limit on how many steps a graph can run, called the **recursion limit** (25 by default). If the agent reaches it before hitting `END`, LangGraph stops the graph and raises a `GraphRecursionError`.

- So the agent does not finish normally or return a final answer. It is cut off with an error, which protects you from running forever.
# How can you prevent endless execution?
You prevent endless execution in three main ways:

1. **Set the recursion limit.** LangGraph stops the graph with an error once it reaches the step limit, so it can never run forever. You can raise or lower this limit in the graph's run settings.

2. **Add a counter in State.** Store the number of loops in State, and have the routing function return `END` when the counter reaches your maximum. This lets you stop gracefully instead of with an error.

3. **Write a clear stop condition.** Make sure the routing function always has a path to `END`, such as when the LLM gives an answer with no tool call.