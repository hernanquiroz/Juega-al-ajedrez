"""Ajedrez Cristal 3D — contenedor Streamlit.

Muestra el tablero (index.html) dentro de Streamlit.
Diseño Vibe Coding por Ing. Hernán Quiroz
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ajedrez Cristal 3D",
    page_icon="♞",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0.4rem 0.5rem 0 0.5rem; max-width: 100%;}
      iframe {border: 0; border-radius: 14px;}
    </style>
    """,
    unsafe_allow_html=True,
)

alto = st.sidebar.slider("Alto del tablero (px)", 500, 1300, 820, 10)

html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
components.html(html, height=alto, scrolling=False)
