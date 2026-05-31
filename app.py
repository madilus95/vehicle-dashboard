import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Panel de control - Anuncios de venta de coches')

car_data = pd.read_csv('vehicles_us.csv')

# Casillas de verificación
mostrar_histograma = st.checkbox('Mostrar histograma')
mostrar_dispersion = st.checkbox('Mostrar gráfico de dispersión')

if mostrar_histograma:
    st.write('Histograma de la columna "odometer"')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

if mostrar_dispersion:
    st.write('Gráfico de dispersión: odometer vs price')
    fig_scatter = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)