import os
from dotenv import load_dotenv

#from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.tools import tool

from langgraph.prebuilt import create_react_agent

from tools.flight_tool import search_flights
from tools.hotel_tool import search_hotels
from tools.places_tool import search_places
from tools.weather_tool import get_weather
from tools.budget_tool import calculate_budget

load_dotenv()

# ---------------- LLM ----------------
#llm = ChatOpenAI(
 #   model="gpt-4o-mini",
 #   temperature=0.3
#)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    api_key=os.getenv("GROQ_API_KEY")
)

# ---------------- TOOLS ----------------
@tool
def flight_tool(route: str):
    """
    Search flights.
    Input format:
    Hyderabad to Goa
    """

    try:
        source, destination = route.split(" to ")

        return str(
            search_flights(source, destination)
        )

    except Exception as e:
        return str(e)


@tool
def hotel_tool(city: str):
    """
    Search hotels by city
    """

    return str(search_hotels(city))


@tool
def places_tool(city: str):
    """
    Search tourist places by city
    """

    return str(search_places(city))


@tool
def weather_tool(city: str):
    """
    Get weather forecast for destination
    """

    # Goa coordinates example
    return str(get_weather(15.2993, 74.1240))


@tool
def budget_tool(input_text: str):
    """
    Calculate estimated trip budget
    """

    return str(calculate_budget(5000, 3000, 3))

tools = [
    flight_tool,
    hotel_tool,
    places_tool,
    weather_tool,
    budget_tool
]

# ---------------- AGENT ----------------

agent = create_react_agent(
    model=llm,
    tools=tools
)

# ---------------- RUN ----------------

def run_travel_agent(user_query):

    result = agent.invoke({
        "messages": [
            ("user", user_query)
        ]
    })

    return result["messages"][-1].content
