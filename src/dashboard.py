import streamlit as st
import plotly.express as px

def render_dashboard(data):
    if data.empty:
        st.write("No dataset loaded. Please upload a dataset.")
        return
    
    st.sidebar.subheader("Filters")
    selected_state = st.sidebar.selectbox("Select State", options=[None] + sorted(data['state'].dropna().unique().tolist()))
    filtered_data = data if not selected_state else data[data['state'] == selected_state]
    
    fig = px.histogram(filtered_data, x='state', title='Industry Distribution by State')
    st.plotly_chart(fig)
    st.write("**Observation:** The distribution of industries varies significantly by state.")
    
    fig2 = px.pie(filtered_data, names='scale', title='Industry Scale Distribution')
    st.plotly_chart(fig2)
    st.write("**Observation:** The industry scale distribution highlights the predominance of small-scale industries over large enterprises.")
