import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Cargar el dataset
df = pd.read_csv('vehicles_us.csv')

# Título principal
st.header('Análisis de Anuncios de Vehículos Usados en EE.UU.')

# Botón para mostrar histograma
if st.button('Mostrar histograma del odómetro'):
    st.write('Histograma de la columna "odometer"')

    fig = go.Figure(data=[
        go.Histogram(x=df['odometer'])
    ])
    fig.update_layout(
        title='Distribución del Odómetro',
        xaxis_title='Odómetro',
        yaxis_title='Frecuencia'
    )
    st.plotly_chart(fig, use_container_width=True)

# Botón para mostrar gráfico de dispersión
if st.button('Mostrar gráfico de dispersión (odómetro vs precio)'):
    st.write('Relación entre el odómetro y el precio del vehículo')

    fig = go.Figure(data=[
        go.Scatter(
            x=df['odometer'],
            y=df['price'],
            mode='markers'
        )
    ])
    fig.update_layout(
        title='Relación entre Odómetro y Precio',
        xaxis_title='Odómetro',
        yaxis_title='Precio'
    )
    st.plotly_chart(fig, use_container_width=True)
