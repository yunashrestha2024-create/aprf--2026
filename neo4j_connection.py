# neo4j_connection.py
import streamlit as st
from neo4j import GraphDatabase
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, NEO4J_DATABASE
from rsp_data import PILLARS

@st.cache_resource
def get_driver():
    return GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def populate_graph():
    driver = get_driver()
    with driver.session(database=NEO4J_DATABASE) as session:
        # Merge Pillars
        for pillar, details in PILLARS.items():
            session.run("MERGE (p:Pillar {name: $pillar})", pillar=pillar)
            
            # Merge Promises and link to Pillar
            for promise in details['promises']:
                session.run("""
                    MERGE (pr:Promise {text: $promise})
                    MERGE (p:Pillar {name: $pillar})
                    MERGE (pr)-[:BELONGS_TO]->(p)
                """, promise=promise, pillar=pillar)
    driver.close()
    return True
