7. Agent Loop

Understand:
- What is an Agent Loop?
- What is the relationship between an LLM and tools?
- How does the LLM decide whether to call a tool?
- How does the tool execute?
- How does the LLM receive the tool result?
- Why does the process repeat?

Goal: Understand the complete cycle: LLM → Tool → LLM → Response.
# What is an Agent Loop?
- An agent loop is the core execution cycle that powers autonomous AI agents. Unlike a standard chatbot that makes a single call and returns an answer, an agent loop lets an AI reason, take action, evaluate the results, and repeat until a goal is met.

- An agent loop is the cycle where the model decides what to do, a tool runs if needed, and the result goes back to the model, repeating until the model has enough to give a final answer.
- it is: model → tools → model → ... → END, and tools_condition is what decides whether to loop again or stop.

# What is the relationship between an LLM and tools?
  an LLM cant execute a tool itself ,it just send the structure tool cal (tool name and parameters) our code then like ToolNode execute the tool and sed the results back to LLM and LLM then anser

# How does the LLM decide whether to call a tool?
- the LLM sees the tool definetion (like tool name ,desc (docstring),argumnt schema) and user's msg and then based on that it decide which tool to call or whether to call a tool or not 
that is why tool's desc matter

# How does the tool execute?
Your code runs the tool, not the LLM. When the model returns a tool call, ToolNode reads the tool name and arguments from it, finds the matching Python function, and calls it with those arguments. The function's return value is then wrapped in a tool message and added to the state, so the model can read it on the next step.

# How does the LLM receive the tool result?
The tool result is added to the message list as a tool message, and the whole message list is sent to the LLM again on its next call. So the LLM doesn’t “receive” it separately; it simply reads it as part of the conversation history (user message, its own tool call, then the tool result) and uses that to continue or write the final answer.

# Why does the process repeat?
Because the LLM has no memory between calls and can't know in advance whether one tool result is enough. After each tool result, it gets called again and looks at the full history: if it still needs more information, it makes another tool call (and the loop repeats), and if it has enough, it writes the final answer and the loop stops.