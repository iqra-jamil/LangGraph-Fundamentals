9. Error Handling

Understand:
- What happens when a tool fails?
- What happens when an API returns an error?
- How do you handle exceptions?
- How do you handle invalid tool inputs?
- How can an agent recover from an error?
- How do retries work?
Goal: Make your agent handle failures without crashing unnecessarily.




# 1. What happens when a tool fails?**
By default, the exception is raised inside the tool node and the graph crashes. `ToolNode` can instead catch the error and return it to the LLM as a message, so the graph keeps running.

# 2. What happens when an API returns an error?**
It is treated like any tool failure. The API call inside the tool raises an exception (timeout, bad status, rate limit), and without handling, the graph stops with that error.

# 3. How do you handle exceptions?**
Wrap the risky part of the tool or node in a try/except. In the except block, return a clear error message instead of crashing, so the LLM or the graph can decide what to do next.

# 4. How do you handle invalid tool inputs?**
Define the tool's inputs with types so wrong inputs are rejected early. The validation error is sent back to the LLM as a message, and the LLM can call the tool again with corrected inputs.

# 5. How can an agent recover from an error?**
Pass the error message back into State. The LLM reads it and either retries with different inputs, tries another tool, or tells the user what went wrong. A conditional edge can also route to a fallback node when an error is in State.

# 6. How do retries work?**
When a call fails because of a temporary problem (network, rate limit), you run it again. You can set a retry policy on a node (number of attempts and delay between them), or keep a retry counter in State. Always set a maximum, so retrying cannot loop forever.