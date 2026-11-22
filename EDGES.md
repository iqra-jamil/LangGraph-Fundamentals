3. Edges

Understand:
- What is an Edge?
- Why do we connect nodes?
- What is START?
- What is END?
- How does execution move from one node to another?
- What is the difference between a Node and an Edge?
Goal: Understand how you define the execution flow.

# What is an Edge?
- Edge in Langgrapgh is a connection between two nodes
- it tells the Graph which node should run nxt after the current one finishes
- Edges can be fixed(always go to the same node) or can also be conditional (choose teh nxt node based on state)

#  Why do we connect nodes?
- we connect nodes so teh graph knows the order in which steps should run
- without connections evey node will sit alone and nothing would pass from one step to the nxt step
- connecting nodes lets the state moves along(Connecting nodes lets the data keep moving forward) ,so the output of node becomes the input of nxt node

# What is START?
- its the special point from where the Graph begins
- we connect it to our first node ,to tell the graph from where to start running
- nothing run before it

# What is END?
- its the special point where the grapgh stops
- when a node connects to the end ,graph finishes and return the final rsult back
- we can have more than one path that goes to end
     - it means diffrent or multiple nodes can all connect to the END,so the graph can finish from different places
     - For example, if a check fails, the graph can go to END early. If it passes, it can go through more steps and then go to END.

# How does execution move from one node to another?

- Execution starts at START and runs the first node.
- When a node finishes, the graph follows the edge from that node to find the next one, and passes along the updated state.
- This repeats until the graph reaches END, and then it stops and returns the final state.


# What is the difference between a Node and an Edge?
- A node is a step that does work, like calling a model or running a function.
- An edge is the link between nodes that decides which node runs next.
- So nodes do the work, and edges control the order.
