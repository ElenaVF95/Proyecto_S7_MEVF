import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv('datos/vehicles_us.csv')

st.header('¡Mi primer producto de datos!')

boton = st.checkbox('Mostrar histograma')

if boton:

    st.write('Este histograma muestra la distribución del kilometraje de autos en venta')

    grafico = px.histogram(df, x='odometer')

    st.plotly_chart(grafico)