import streamlit as st
import pandas as pd

# Título de la página
st.title("Carga de archivo CSV en Streamlit")

# Componente para cargar el archivo CSV
uploaded_file = st.file_uploader("Selecciona un archivo CSV", type=["csv"])

# Verificar si se cargó un archivo
if uploaded_file is not None:
    # Leer el archivo CSV y cargarlo en un DataFrame
    df = pd.read_csv(uploaded_file)

    # Mostrar el DataFrame
    st.write(df)
