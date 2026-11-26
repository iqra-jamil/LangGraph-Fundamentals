from typing import TypedDict,Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import SystemMessage
from  langchain_groq import ChatGroq
from langgraph.graph import StateGraph,START,END
from langchain.tools import tool
from langgraph.prebuilt import ToolNode,tools_condition 
import datetime
import os
import requests
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv('API_KEY')

#tools
@tool
def get_weather(city_name):
    """
    Get the current weather of a city.

    Args:
        city_name: Name of the city, e.g. "Lahore".

    Returns:
        A dictionary with the weather data of that city (temperature in Celsius, conditions, humidity, wind, etc.).
    """
    API_URL=f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city_name}&units=metric"
    data=requests.get(API_URL)
    print(data.status_code)
    res=data.json()
    return res
@tool
def date_time():
    """
    get the current date and time
    Args :
    Returns:
    A dictionary with current date and time
    """
    current_date_time=datetime.datetime.now()
    date=current_date_time.date()
    time=current_date_time.time()
    return {"date": str(date), "time": str(time)}

# define state +build frst node (call_model)

class myState(TypedDict):
    messages:Annotated[list,add_messages]
# call the model
model=ChatGroq(
    model="openai/gpt-oss-120b"
)
model_with_tools=model.bind_tools([get_weather,date_time])

# model node
def call_model(myState):
    messages=myState["messages"]
    systemmsgs=[SystemMessage(content="You are a helpful agent")]
    resposne=model_with_tools.invoke(systemmsgs+messages)
    return {"messages":[resposne]}  

#final_node
def final_node(myState):
     print("Final answer:", myState["messages"][-1].content)
     return {} # no updates

# create graph,register node, handle edges
graph_builder=StateGraph(myState) #creating the graph
graph_builder.add_node("call_model",call_model)
graph_builder.add_edge(START,"call_model")
tool=ToolNode([get_weather,date_time])
graph_builder.add_node("tools",tool)
graph_builder.add_node("final_node",final_node)
#tools_condition and add_conditional_edges
graph_builder.add_conditional_edges("call_model",tools_condition,{"tools": "tools", END: "final_node"})
graph_builder.add_edge("tools","call_model")
graph_builder.add_edge("final_node", END)
#tools condition is a routing function which will return "tools" or END
compiled=graph_builder.compile()
result=compiled.invoke({"messages":"whats the weather today in islamabad"})


