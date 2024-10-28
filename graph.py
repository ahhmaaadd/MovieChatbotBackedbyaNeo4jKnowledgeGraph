import streamlit as st
from langchain_community.graphs import Neo4jGraph
import httpx
from dotenv import load_dotenv
import os

# Connect to Neo4j
load_dotenv()
url = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")

graph = Neo4jGraph(
    url=url,
    username=username,
    password=password,
)