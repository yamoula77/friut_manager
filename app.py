import streamlit as st
from fruit_managers import *

st.title("Dashboard de Plantation")

inventaire = ouvrir_inventaire()
prix = ouvrir_prix()
tresorerie = ouvrir_tresorerie()

st.header("La Tresorerie")
st.metric(label="Montant disponible", value=f"{tresorerie:.2f} $")

st.header("inventaire")
st.table(inventaire)
