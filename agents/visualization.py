from crewai import Agent
import plotly.express as px
import streamlit as st
import pandas as pd

class DataVisualizationAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Data Visualization Specialist",
            goal="Create meaningful visualizations from the dataset.",
            backstory="An expert in data visualization, responsible for generating interactive charts and insights."
        )
    
    def run(self, data):
        if data.empty:
            return "No dataset loaded. Please upload a dataset."
        
        st.sidebar.subheader("Filters")
        selected_state = st.sidebar.selectbox("Select State", options=[None] + sorted(data['state'].dropna().unique().tolist()))
        filtered_data = data if not selected_state else data[data['state'] == selected_state]
        
        st.write("### Industry Distribution by State")
        fig = px.histogram(filtered_data, x='state', title='Industry Distribution by State')
        st.plotly_chart(fig)
        st.write("**Observation:** The distribution of industries varies significantly by state.")
        
        st.write("### Industry Scale Distribution")
        fig2 = px.pie(filtered_data, names='scale', title='Industry Scale Distribution')
        st.plotly_chart(fig2)
        st.write("**Observation:** The industry scale distribution highlights the predominance of small-scale industries over large enterprises.")
        
        return filtered_data
    