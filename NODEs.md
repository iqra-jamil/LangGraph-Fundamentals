2. Nodes In LangGrapgh

Understand:
- What is a Node?
- What does a Node do?
- How do you create a Node function?
- How does a Node receive State?
- How does a Node return updated State?
- Can a graph have multiple nodes?
Goal: Understand how individual tasks are performed inside a graph.


# - What is a Node?
- A Node is a python function that perform a specific task in graph 
- here graph means the complete wrkflow of langGraph where multiple nodes are connected to each other and defines how our agent is executing its steps

#### For example:
- One node receives the user's message.
- Another node calls an LLM.
- Another node processes the LLM's response.
Each node perform a specif operation as a part of graph's workflow
a node can be an individual step in our agent's workflow


# What does a Node do?

A Node performs a specific operation in your LangGraph workflow.

Here's what happens when a Node executes:

1. It receives the current State from the graph.
2. It performs its assigned operation. For example, calling an LLM, processing a message, or calculating something.
3. It can return new information or updated values for the State.
4. LangGraph uses that updated State when executing the next step.

Example:

Imagine you have a chatbot with two nodes:

- Node 1: Receives the user's question and sends it to the LLM.
- Node 2: Processes the LLM's response.

Each Node handles its own part of the workflow.

Important: A Node does not decide the entire graph's execution flow by itself. Edges define where execution goes next.

# How do you create a Node function?
- In LangGraph, you create a Node function using a normal Python function.
- A basic Node function has two parts:
    1. It accepts State as an argument.
    2. It performs an operation and returns a dictionary containing the updated State.
- To register  function as a Node, we use:
    builder.add_node("chatbot", chatbot)
- StateGraph() is a class of LangGraph which we use to create whole strcuture of our agent's work flow 
- or we can say we use to to create new graph 
- we provide it with a state schema that define which information our graph will manage
- while initiating stateGraph() we use an object or a varaible wihc is called builder 
- we use builder object to add and connect nodes Inside the workflow created by StateGraph()


## Note : we can define a state using different instances like TypedDict, dataclass, or Pydantic

# How does a Node receive State?
- in langgrapgh aik Node rcve krti hai current state ko automatically ,
jab langGraph node ko execute krti hai
- here is how it works: 
   1. we define State schema using an instace like Typedict jo ye specify krti hain k kon se information state hold kry ge
   2. when we create a node function we accept , state as a parameter
   3. when langGraph execute Node function to current state automaticaly Node function ko pass ho jati hai or whi state execute hoti h
- LangGraph passes the actual State value automatically when it executes the Node we dont pass the state value manually


#  How does a Node return updated State?
- a node return updated State using retrn statemnt of python
- when node finish prforming its operation ,it return a dictionary conatining the inforation it want to update or add in the current state 
- A Node usually returns only the State fields it wants to update, not necessarily the entire State.


#  Can a graph have multiple nodes?
Yes. A LangGraph workflow can have multiple Nodes.

Each Node performs a different operation. we add them using `builder.add_node()`.

For example, a chatbot might have:

1. `input_node`: Receives the user's message.
2. `llm_node`: Sends the message to the LLM.
3. `response_node`: Processes the LLM's response.

These Nodes are connected so LangGraph knows which one to execute next.

# how do we execute a node
Note : Compile means preparing your workflow so LangGraph can execute it.
- we dont execute a node by calling its function directly
#first we complie the wrkflow 
- langgraph execute Node when  we run the compiled workflow
- the process has three steps:
      1. Register the node using builder.add_node().
      2. compile the workflow using builder.compile
      3. execute the wrkflow using app.invoke

- invoke() starts or execute the workflow and then langGrapgh execute the Nodes according to the order or connections we defined
- we define the order or conncetions using edges