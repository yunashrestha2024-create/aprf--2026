import streamlit as st
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

def show():
    st.subheader("🔗 Rhizomatic Knowledge Graph")
    G = nx.Graph()
    G.add_node("RSP Promises", color="red")
    G.add_node("Macro Reality", color="green")
    G.add_node("Well-being", color="purple")
    G.add_node("AI Capability", color="cyan")
    G.add_node("Education", color="orange")
    
    G.add_edge("RSP Promises", "Macro Reality")
    G.add_edge("Macro Reality", "Well-being")
    G.add_edge("AI Capability", "Education")
    G.add_edge("Education", "Well-being")
    
    net = Network(height="600px", width="100%", bgcolor="#0e1117", font_color="#ffffff")
    net.from_nx(G)
    components.html(net.generate_html(), height=600, width="100%")
