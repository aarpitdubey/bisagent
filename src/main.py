import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv
from dashboard import render_dashboard
from upload import load_data
import streamlit as st
from crewai import Task, Crew
from agents.data_cleaning import DataCleaningAgent
from agents.visualization import DataVisualizationAgent
from agents.hotspot_prediction import IndustrialHotspotAgent
from src.upload import load_data
load_dotenv()

# Set API Key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# ✅ Add Dataset Upload Button
st.sidebar.title("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])
data = load_data(uploaded_file)

# Initialize agents
data_cleaning_agent = DataCleaningAgent()
data_viz_agent = DataVisualizationAgent()
hotspot_agent = IndustrialHotspotAgent()

# Create tasks with expected output
data_cleaning_task = Task(
    agent=data_cleaning_agent,
    description="Clean and preprocess data",
    expected_output="A cleaned dataset with missing values handled."
)

data_viz_task = Task(
    agent=data_viz_agent,
    description="Generate visualizations",
    expected_output="Industry distribution charts and insights."
)

hotspot_task = Task(
    agent=hotspot_agent,
    description="Predict industrial hotspots",
    expected_output="Identified regions where new industries are likely to emerge."
)

# ✅ Correctly pass `tasks` as a keyword argument
data_crew = Crew(tasks=[data_cleaning_task, data_viz_task, hotspot_task])

# Run tasks
st.sidebar.title("Agentic AI Dashboard")
selected_task = st.sidebar.radio("Select a Task:", ["Data Cleaning", "Data Visualization", "Industrial Hotspot Prediction"])

if st.button("Run Task"):
    result = data_crew.kickoff()  # ✅ Execute tasks correctly
    st.write(result)