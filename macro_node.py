import streamlit as st
import pandas as pd
import plotly.express as px
from data_fetcher import fetch_world_bank_data

def show():
    st.subheader("🌐 Macro Reality Node")
    
    gdp = fetch_world_bank_data("NY.GDP.MKTP.KD.ZG")
    inflation = fetch_world_bank_data("FP.CPI.TOTL.ZG")
    
    if gdp and inflation:
        df = pd.DataFrame({
            "Year": list(gdp.keys()),
            "GDP (%)": list(gdp.values()),
            "Inflation (%)": list(inflation.values())
        })
        df = df.sort_values("Year")
        st.line_chart(df.set_index("Year"))
        st.metric("Latest GDP", f"{df.iloc[-1]['GDP (%)']}%")
        st.metric("Latest Inflation", f"{df.iloc[-1]['Inflation (%)']}%")
    else:
        st.warning("World Bank data unavailable. Using static data.")
        st.metric("GDP", "3.9%")
        st.metric("Inflation", "6.4%")
