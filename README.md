Agentic AI Travel Planning Assistant
An AI-powered travel planner built using LangChain, Groq LLM, and Streamlit that automatically creates personalized travel itineraries with flights, hotels, tourist attractions, weather forecasts, and budget estimation.

Features:
Flight search from JSON dataset
Hotel recommendation system
Tourist places discovery
Real-time weather forecast using Open-Meteo API
Budget estimation
Day-wise itinerary generation
LangChain ReAct Agent for autonomous decision making
Streamlit web interface

Tech Stack:
- Python
- LangChain
- LangGraph
- Groq API
- Streamlit
- Open-Meteo API
- JSON Datasets

Project Structure:
project/
|- agent/
|- data/
|- tools/
|- utils/
|- app.py
|- requirements.txt
|- README.md

Installation:
1. Clone Repository:
   git clone - https://github.com/mansik05/AgenticAI_travel
   cd AgenticAI_travel

2. Create Virtual Environment:
   python -m venv venv
   Activate environment:
   Windows: venv\Scripts\activate
   Mac/Linux: source venv/bin/activate

3. Install Dependencies:
   pip install -r requirements.txt

4. Add Environment Variables:
   Create a .env file:
   GROQ_API_KEY= not mentioning here but can be found in the project .env file.
   
5. Run Application:
   streamlit run app.py
   - User enters travel details
   - LangChain agent selects tools automatically

   Tools fetch:
   - Flights
   - Hotels
   - Tourist places
   - Weather
   AI generates optimized itinerary and budget.

Example Query:
Plan a 3-day trip from Mumbai to Goa under 12000 INR.

Sample Output:
- Cheapest flight recommendation
- Best hotel suggestion
- Weather forecast
- Tourist attractions
- Day-wise itinerary
- Budget breakdown

Future Improvements:
- Real-time flight APIs
- Google Maps integration
- Voice assistant
- Database support
- User authentication
