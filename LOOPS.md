5. Loops

Understand:
- What is a loop in LangGraph?
- How do nodes execute repeatedly?
- How do conditional edges create loops?
- How do you prevent infinite loops?
Goal: Understand how an agent can repeat tasks until a condition is met.

# What is a loop in LangGraph?
A loop in LangGraph means sending execution back to a previous Node so it can run again, usually until a condition is met.
# How do nodes execute repeatedly?
Each time the graph reaches a node, it runs that node again, even if it ran before.
A routing function sends the graph back to that node, and the node reads the updated state and does its work again.
This repeats until the routing function sees the state is good enough and sends the graph to END.

# How do conditional edges create loops?
- A conditional edge lets a routing function return the name of any node, including one that already ran.
- When it returns an earlier node, the graph goes back to it, and that part runs again.
- The loop stops when the routing function returns a different node, like END, instead.
# How do you prevent infinite loops?
- Make sure your routing function has a clear stopping condition, like going to END when the answer is good enough.
- Keep a counter in the state, such as number of tries, and send the graph to END when it reaches a limit.
- LangGraph also has a recursion limit that stops the graph with an error if it runs too many steps, which acts as a safety net.