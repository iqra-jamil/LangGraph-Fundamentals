1. Why do you use `Annotated[list, add_messages]` instead of a plain `list` for `messages`?
2. What is a reducer in LangGraph?
3. What does a node receive, and what must it return?
4. Why is `model` created outside the node instead of inside it?
5. What does `bind_tools` do, and why must you call `invoke` on the result, not on the original model?
6. What does the `@tool` decorator do, and why does the docstring matter?
7. Why shouldn't `api_key` be an argument of `get_weather`?
8. What does `ToolNode` do, and what does it return?
9. What is the difference between `add_edge` and `add_conditional_edges`?
10. What does `tools_condition` return, and when?
11. Why do you need the path map `{"tools": "tools", END: "final_node"}`, and what would happen without it?
12. Why does `add_edge("tools", "call_model")` exist? What would happen without it?
13. Why does `final_node` return `{}`?
14. Is `END` a node? How does the graph stop?
15. What does `compile()` return, and why can't you call `invoke` on the builder?
16. How do you get only the LLM's final answer from `result`?
17. What is the difference between LangChain and LangGraph?
18. How does the graph know to stop calling tools in a loop?


1. Why do you use `Annotated[list, add_messages]` instead of a plain `list` for `messages`?
- By default, LangGraph overwrites a state key with whatever a node returns.
- Annotated attaches a reducer (add_messages) to the key, so new messages are appended to the existing list. That keeps the full conversation history (human, AI, and tool messages) for the next LLM call.

2. What is a reducer in LangGraph?
Interview-ready definition: a reducer is a function that tells LangGraph how to combine a state key's existing value with the new value a node returns.
3. what does a node receive, and what must it return?
- add_messages is one reducer. Its rule is "append the new messages to the old list." That is why old items aren't replaced. Without a reducer, the default rule is "replace."

- a node receives the current state as its argument and returns a dictionary of state updates, which LangGraph merges into the state. If it changes nothing, it returns {}.

4. Why is `model` created outside the node instead of inside it?
becasue if i would create model inside node ,whenevr node would get executed the model would be craeted and it would be inefficiency
the model doesn't change between runs, so creating it once at the start and reusing it avoids repeating the same work every time the node runs. The same applies to bind_tools, which you also moved outside the node.

5. What does `bind_tools` do, and why must you call `invoke` on the result, not on the original model?
Answer: bind_tools is a method that attaches the tools' definitions (name, arguments, description) to the model, so the model knows which tools it can request. It doesn't change the original model; it returns a new model with the tools attached. You must call invoke on that returned model, not on the original one, because only the returned model knows about the tools. The model doesn't run the tools itself; it only requests a tool call, and ToolNode executes it.

6. What does the `@tool` decorator do, and why does the docstring matter?
Answer: The @tool decorator turns a normal Python function into a tool that the LLM can request. It builds a schema from the function's name, arguments, and docstring. The docstring matters because the LLM never sees the code. It reads the name, the arguments, and the docstring to decide whether to use the tool and what values to pass. A vague or wrong docstring can make the LLM pick the wrong tool or pass wrong arguments.

7. Why shouldn't api_key be an argument of get_weather?
The LLM only knows what's in the conversation, so it can't know your key. It would guess a wrong value, or ask the user for it, and the tool call would fail.
Secrets should never be passed through the LLM. Anything in the tool's arguments becomes part of the conversation, so the key could be exposed. Keeping it outside, loaded from .env, keeps it hidden.
8. what does ToolNode do, and what does it return?
ToolNode reads the tool call (name and arguments) from the LLM's last message, runs the matching tool, and wraps each result in a ToolMessage.
It returns those ToolMessages under messages, and add_messages appends them to the state, so the LLM can read them on its next call.

9. What is the difference between `add_edge` and `add_conditional_edges`?
- add_edge connect the nodes in a fixed order like from A should definently go to B and add_conditional_edges connect the nodes based on condition the node should execute based on the condition get corrected
10. What does `tools_condition` return, and when?
- add_conditional_edges runs a routing function on the state after a node finishes. The function returns the next node's name, and the graph goes there. So the path is decided at run time.

Interview-ready: tools_condition is a prebuilt routing function that checks the LLM's last message. If it contains a tool call, it returns "tools", the name of the tool node. If it's a plain answer, it returns END.

Because it returns the name "tools", the tool node must be registered under exactly that name.

11. why do you need the path map {"tools": "tools", END: "final_node"}, and what would happen without it?

The path map translates the values the routing function returns into actual node names. Without it, tools_condition returns "tools" or END, and those names would be used directly. So "tools" would still work, but a plain answer would go straight to END, and final_node would never run. I needed the map to send the END case to final_node first.


12. why does add_edge("tools", "call_model") exist, and what would happen without it?
- if tools node get exrecuted than call model node should get executed after that
- the edge sends the tool's result back to call_model, so the LLM can read the ToolMessage and write the final answer. Without it, the graph would have no path out of tools, and the user would never get an answer built from the tool's result.


13. why does final_node return {}?

: a node must return a dictionary of state updates, so when it changes nothing, it returns an empty dictionary {}, meaning "no updates."

14. is END a node? How does the graph stop?

15. What does `compile()` return, and why can't you call `invoke` on the builder?
compile() returns a runnable graph, a new object built from the design you made with the builder. graph_builder is only a blueprint: it holds your nodes and edges but can't run them, so it has no invoke. Compiling checks the graph (for example, that every edge points to a real node) and produces the executable version, which is why you save it, as in compiled = graph_builder.compile(), and call invoke on compiled.


16. How do you get only the LLM's final answer from `result`?
result is the final state, a dictionary. Its messages key holds the whole conversation, and the LLM's final answer is the last message, so you write result["messages"][-1].content. [-1] picks the last message, and .content gets its text.
17. What is the difference between LangChain and LangGraph?
LangChain is a library of building blocks for working with LLMs. LangGraph is built on top of LangChain and controls the flow between steps, so you can add decisions, loops, and tool calls, like your agent loop where the LLM calls a tool and then goes back to the LLM.
18. How does the graph know to stop calling tools in a loop?
After every call_model run, tools_condition checks the LLM's last message. If it still contains a tool call, the graph goes to tools and loops back. When the LLM decides it has enough information and writes a plain answer, there is no tool call, so tools_condition returns END (here, routed to final_node) and the loop stops. So the LLM itself decides when to stop.