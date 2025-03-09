from crewai import Agent
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
import pandas as pd
import streamlit as st

class IndustrialHotspotAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Industrial Growth Predictor",
            goal="Predict future industrial hotspots based on past trends.",
            backstory="A data scientist specializing in geospatial and economic forecasting, providing insights into potential industrial growth areas."
        )
    
    def run(self, data):
        if data.empty:
            return "No dataset loaded. Please upload a dataset."
        
        df = data.dropna(subset=['state', 'district', 'latitude', 'longitude'])
        X = pd.get_dummies(df[['state', 'district', 'latitude', 'longitude']])
        y = (df['scale'].notnull()).astype(int)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20]}
        model = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5)
        model.fit(X_train, y_train)
        y_pred = model.best_estimator_.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        st.write("### Industrial Hotspot Prediction")
        st.write(f"**Prediction Model Accuracy:** {accuracy:.2f}")
        st.write("**Observation:** The industrial hotspot prediction model helps in identifying regions where new industries are likely to emerge.")
        
        return df
    
    