import streamlit as st
import streamlit.components.v1 as components

st.title("Interactive 3D Network Graph")

# Embed the GitHub Pages-hosted HTML file
url = "https://mkp-7.github.io/Network-Graph/a.html"

components.iframe(url, height=800, scrolling=True)
