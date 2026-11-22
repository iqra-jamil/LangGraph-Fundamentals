# LangGraph** 
is a Python library for building AI agents as a graph. Instead of writing one long script where the LLM runs once, you design the agent as a set of steps (nodes) connected by paths (edges), and the agent moves through them, including looping back, until the task is done.
# Note:langGraph is built on the top of langChain
# How the 10 topics fit together:

- **State** is the shared memory of the graph. It holds the messages, results, and any data the agent needs as it runs.
- **Nodes** are the steps. Each node is a function that reads the State, does one job (call the LLM, run a tool), and returns updates to the State.
- **Edges** connect the nodes and define the order. START is where the graph begins and END is where it finishes.
Edges set the order the nodes run in, and each node updates the State before the next node runs.
........................................................................................................................................................................................
- **Conditional routing** lets the graph choose the next node based on the State, for example "if the LLM wants a tool, go to the tool node; otherwise finish."
- **Loops** appear when a conditional edge sends execution back to an earlier node, so steps can repeat.
- **Tool nodes** are the nodes that run external functions (search, calculator, API) on the LLM's behalf.
- **Agent loop** is what you get when you combine them: LLM node → conditional route → tool node → back to the LLM node, repeating.
- **Stopping conditions** are the routes that lead to END, so the loop doesn't run forever.
- **Error handling** keeps the graph from crashing when a tool or API fails.
- **Build one simple agent** puts all of the above into a single working project.





# Tool calling project vs Agent

## Tool calling project (one round)**
- The LLM asks for tools, your code runs them, and the results go back to the LLM once.
- The LLM then gives the final answer.
- It works when the tools are independent, like weather and time.
- It cannot handle a case where the next tool depends on the previous tool's result.

## Agent (loop)**
- The LLM asks for tools, the tools run, and the results go back to the LLM.
- The LLM can ask for more tools, and this repeats until it has no more tool requests.
- Only then does it give the final answer.
- It handles independent tools and tools that depend on each other.

## LangGraph** is a library that builds this repeating loop for you.