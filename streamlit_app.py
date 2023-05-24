import streamlit as st 
import pandas as pd 
import numpy as np                  # Para crear vectores y matrices n dimensionales
import matplotlib.pyplot as plt     # Para la generación de gráficas a partir de los datos
from apyori import apriori

image = Image.open('img/IA_salud')
st.image(image, use_column_width = True)
