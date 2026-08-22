# rsp_graph_node.py
import streamlit as st
import pandas as pd
import plotly.express as px
from neo4j_connection import get_driver, populate_graph
from config import NEO4J_DATABASE
from rsp_data import PILLARS
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

def show():
    st.subheader("📜 RSP Vacha Patra vs Reality (Graph)")
    
    # 🚀 The Populate Button (This is what you're looking for!)
    if st.button("🚀 Populate RSP Graph into Neo4j"):
        if populate_graph():
            st.success("✅ Graph populated! Nodes and edges created.")
        else:
            st.error("Connection failed. Check credentials in config.py.")
    
    # Visualize Graph (Now with real data!)
    driver = get_driver()
    G = nx.Graph()
    with driver.session(database=NEO4J_DATABASE) as session:
        # Fetch Nodes
        result = session.run("MATCH (n) RETURN n")
        for record in result:
            node = record["n"]
            node_name = node.get("name", node.get("text", str(node)))
            G.add_node(node_name)
        # Fetch Edges
        result = session.run("MATCH (a)-[r]->(b) RETURN a, b")
        for record in result:
            a = record["a"].get("name", record["a"].get("text", str(record["a"])))
            b = record["b"].get("name", record["b"].get("text", str(record["b"])))
            G.add_edge(a, b)
    
    # Visualize using Pyvis
    net = Network(height="600px", width="100%", bgcolor="#0e1117", font_color="#ffffff", notebook=False)
    net.from_nx(G)
    components.html(net.generate_html(), height=600, width="100%")
    
    # Analysis Table
    target_data = []
    for pillar, details in PILLARS.items():
        target_data.append({
            "Pillar": pillar,
            "Number of Promises": len(details['promises']),
            "Reality Check": "GDP at 3.9%, Inflation at 6.4%"
        })
    st.dataframe(pd.DataFrame(target_data))
