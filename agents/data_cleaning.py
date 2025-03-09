from crewai import Agent
from sklearn.impute import SimpleImputer
import pandas as pd
import streamlit as st
import os

class DataCleaningAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Data Cleaning Specialist",
            goal="Ensure the dataset is clean and structured for analysis.",
            backstory="An expert in data preprocessing, responsible for handling missing values and standardizing datasets."
        )
    
    def run(self, data):
        if data.empty:
            return "No dataset loaded. Please upload a dataset."
        
        imputer = SimpleImputer(strategy='most_frequent')
        data[['state', 'district', 'city']] = imputer.fit_transform(data[['state', 'district', 'city']])
        
        return data