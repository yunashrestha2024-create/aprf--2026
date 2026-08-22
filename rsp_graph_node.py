import streamlit as st
import pandas as pd
import plotly.express as px
from rsp_data import PILLARS
import data_fetcher

def show():
    st.subheader("📜 RSP Vacha Patra vs Reality (Structured Data)")
    
    # 1. Display the Pillars
    st.write("### 📌 The 5 Core Pillars")
    pillar_names = list(PILLARS.keys())
    
    # 2. Fetch Live Macro Data
    gdp = data_fetcher.fetch_world_bank_data("NY.GDP.MKTP.KD.ZG")
    inflation = data_fetcher.fetch_world_bank_data("FP.CPI.TOTL.ZG")
    
    # Combine Reality Data
    if gdp and inflation:
        reality_df = pd.DataFrame({
            "Year": list(gdp.keys()),
            "GDP Growth (%)": list(gdp.values()),
            "Inflation (%)": list(inflation.values())
        })
        reality_df = reality_df.sort_values("Year")
        latest_gdp = reality_df.iloc[-1]['GDP Growth (%)']
        latest_inflation = reality_df.iloc[-1]['Inflation (%)']
    else:
        latest_gdp, latest_inflation = 3.9, 6.4
    
    # 3. Build the Reality vs Target Table
    target_data = []
    for pillar, details in PILLARS.items():
        # Assign theoretical targets based on RSP manifesto
        if pillar == "Governance & Integrity":
            target_status = "Digital governance, zero corruption tolerance"
        elif pillar == "Middle-Class Expansion":
            target_status = "7% GDP growth, tax fairness"
        elif pillar == "Employment & Productivity":
            target_status = "1M jobs, reduced migration"
        elif pillar == "Connectivity & Infrastructure":
            target_status = "Smart Nepal, modern transport"
        elif pillar == "Diaspora Engagement":
            target_status = "Diaspora bond, capital return"
        
        target_data.append({
            "Pillar": pillar,
            "Number of Promises": len(details["promises"]),
            "Target": target_status,
            "Reality Check": f"GDP at {latest_gdp}%, Inflation at {latest_inflation}%"
        })
    
    target_df = pd.DataFrame(target_data)
    st.dataframe(target_df)
    
    # 4. Bar Chart: Promises per Pillar
    st.write("### 📊 Promises Distribution per Pillar")
    fig = px.bar(target_df, x="Pillar", y="Number of Promises", color="Pillar",
                 title="Distribution of RSP 100-Point Agenda")
    st.plotly_chart(fig, use_container_width=True)
    
    # 5. Live Macro Reality Chart
    st.write("### 📈 Live Macro Reality (World Bank)")
    if gdp and inflation:
        fig2 = px.line(reality_df, x="Year", y=["GDP Growth (%)", "Inflation (%)"],
                       title="Nepal Macro Reality: GDP & Inflation",
                       color_discrete_sequence=["#00ff9d", "#ff4d4d"])
        st.plotly_chart(fig2, use_container_width=True)
        st.metric("Latest GDP", f"{latest_gdp}%", "Target: 6.5%")
        st.metric("Latest Inflation", f"{latest_inflation}%", "Target: 5.0%")
    else:
        st.info("World Bank data unavailable. Showing static values.")
        st.metric("GDP", "3.9%", "Target: 6.5%")
        st.metric("Inflation", "6.4%", "Target: 5.0%")
    
    # 6. Policy Brief (Automated Research)
    st.write("### 📜 Automated Policy Brief")
    st.write(f"""
    **Research Insight:** 
    The RSP's '100 Promises' are distributed across {len(pillar_names)} core pillars. 
    The **Employment & Productivity** pillar holds the highest stakes for national development, 
    with specific targets for job creation and reducing foreign labor migration. 
    
    **Critical Gap:**
    Currently, Nepal's GDP growth is at **{latest_gdp}%** (target: 6.5%) and inflation is at **{latest_inflation}%** (target: 5.0%). 
    These macro realities indicate a **significant structural gap** between the promises and what the economy can deliver. 
    
    **Research Recommendation:**
    To achieve the RSP's targets, the government must move beyond aspirational promises and **operationalize** 
    these commitments with clear, measurable, and real-time tracking. This dashboard is designed to provide that 
    transparency and accountability.
    """)
    
    st.caption("APRF Intelligence Engine | RSP Promise vs Reality Node")
