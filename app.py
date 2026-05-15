import streamlit as st
import pandas as pd
import plotly.express as px

df_cars=pd.read_csv('datos/vehicles_us.csv')

st.header('Registro de autos publicados para su venta')

boton_hist = st.checkbox('Mostrar histograma')

if boton_hist:

    st.write('Este histograma muestra la distribución del kilometraje de los autos en venta')

    grafico = px.histogram(
        df_cars, 
        x='odometer',
        title= 'Distribución de kilometraje (Odómetro)', labels= {'odometer': 'Lectura odómetro'}, color_discrete_sequence=['mediumpurple']
    )

    st.plotly_chart(grafico)

boton_disp = st.checkbox('Mostrar gráfico de dispersión')

if boton_disp:

    st.write('Este gráfico de dispersión muestra la relación entre el odómetro y el precio de los autos en venta')

    dispersion = px.scatter(df_cars, x='odometer', y='price',
                            title= 'Relación Odómetro vs Precio', labels= {'odometer': 'Lectura odómetro', 'price': 'Precio'}, color_discrete_sequence=['mediumpurple']
    ))

    st.plotly_chart(dispersion)