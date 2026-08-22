import streamlit as st
import rsp_graph_node
import macro_node
import wellbeing_node
import simulation_node
import knowledge_graph

st.set_page_config(page_title="APRF Intelligence Engine 2026", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main { background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%); color: white; }
    .stTitle { color: #00ff9d; font-size: 3rem; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.title("APRF Intelligence Engine 2026")
st.subheader("National-Global Policy Intelligence System")

# Navigation Sidebar
st.sidebar.title("🧭 System Navigation")
node = st.sidebar.radio(
    "Select Node",
    ["📜 RSP Promise vs Reality", "🌐 Macro Reality", "🕊️ Well-being", "🔮 Simulation", "🔗 Knowledge Graph"]
)

if node == "📜 RSP Promise vs Reality":
    rsp_graph_node.show()
elif node == "🌐 Macro Reality":
    macro_node.show()
elif node == "🕊️ Well-being":
    wellbeing_node.show()
elif node == "🔮 Simulation":
    simulation_node.show()
elif node == "🔗 Knowledge Graph":
    knowledge_graph.show()

st.caption("© 2026 APRF Intelligence Engine | Svatantrya System")
