import streamlit as st

from agent.travel_agent import run_travel_agent


st.title("Agentic AI Travel Planner")


source = st.text_input("Enter Source City")

destination = st.text_input("Enter Destination")

days = st.number_input(
    "Number of Days",
    min_value=1,
    max_value=10,
    value=3
)

budget = st.number_input(
    "Budget (₹)",
    min_value=1000,
    value=15000
)


if st.button("Generate Trip Plan"):

    query = f"""
    Plan a {days}-day trip from {source} to {destination}.

    Budget: {budget} INR

    Include:
    - flights
    - hotels
    - tourist attractions
    - weather
    - budget estimation
    - day-wise itinerary
    """

    with st.spinner("AI is planning your trip..."):

        result = run_travel_agent(query)

    st.success("Trip Plan Generated!")

    st.write(result)