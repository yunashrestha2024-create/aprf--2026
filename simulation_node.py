import streamlit as st
import plotly.express as px
import pandas as pd

def show():
    st.subheader("🔮 Policy Simulation Node")
    stimulus = st.slider("Fiscal Stimulus (% of GDP)", 0, 10, 3)
    edu_invest = st.slider("Education Investment (% of Budget)", 0, 20, 8)
    
    sim_gdp = 3.9 + (stimulus * 0.4) + (edu_invest * 0.1)
    sim_inflation = 6.4 + (stimulus * 0.2) - (edu_invest * 0.05)
    sim_wellbeing = 58 + (edu_invest * 0.5)
    
    st.metric("Simulated GDP", f"{sim_gdp:.2f}%")
    st.metric("Simulated Inflation", f"{sim_inflation:.2f}%")
    st.metric("Simulated Well-being", f"{sim_wellbeing:.2f}")
