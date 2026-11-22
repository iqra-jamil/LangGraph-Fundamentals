6. Tool Nodes

Understand:
- What is a Tool in an AI agent?
- What is the difference between a Tool and a Node?
- How do you define a custom tool?
- What is ToolNode?
- What is tools_condition?
- How does an LLM decide when to call a tool?
- How does the tool result return to the LLM?


#  What is a Tool in an AI agent?
- A tool is a function that an AI agent can call to do something the model can’t do on its own, like searching the web, doing math, or reading a database.
- The model decides which tool to use and what input to give it, and the tool runs and sends the result back.
- The agent then uses that result to continue its work or write the final answer.

# How do you define a custom tool?
A custom tool is defined by three parts:
  - Name 
  - description
  - input schema (the details of parameters)
- our actual function then does the real work. The model only chooses the tool and fills in the arguments. our code runs the function and sends the result back to LLM.
- tools are the functions we describe to the model
- the result of a tool is ToolMessage

# why we call it custom tool
- bcz we write functiona nd its description for our own specific need,
### builtin Tools
- unlike built-in tools that come ready-made with the platform/provider (like web search).
- other built-in tools include file srch,image generation etc
# custom tools vs built in tools
- custom tools are the tools we write and run ourself,
- built-in tools are provided and run by the platform,the platform provider like gpt,anthropic already built them ,we just turn thm on when we call the model
# whats is docString?
- doc string is a description we write inside a function in triple quotes ,that description tell what function does 
# whats is @tool
- @tool is a decorator from langchain and  langGraph
- we write a normal function and @tool turn it into a tool automatically
- @tool reads teh function name,its docstring(as its description) and its parameters with their datatypes and create tool definetion for us
- so instead of writeing tool's name ,descrp etc (tool definetion) into tool.json it create it autmatically
# What is ToolNode?(its actually a node)
- its a readymade component in langraph that execute the model's requested tool autmatically and wrap the results inside Toolmessage we dont need to do it manulay

# What is tools_condition?
its a readymade function in langGraph that chks the last msg of the mdoel if it requeted the tool then it will route to the ToolNode,if not then it will end the graph so we will ahve no need to use if-else
### note these are readymade tools of frameworks like lanGraph for the ease of manual work
# How does an LLM decide when to call a tool?
The model reads your user’s message along with each tool’s name and description, then decides whether a tool is needed to answer. If one fits, it returns a tool call with the arguments instead of a normal reply. If none fits, it just answers directly.

#  How does the tool result return to the LLM?
we wrap the result of tool execution into Toolmsg with its matching tool_call_id and then we append the wrapped result into conversation list and send that list to the LLm and call the mdoel again ,the model thn read the results and writes the final anser