import streamlit as st
import pandas as pd
import snowflake.connector

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.header("Arquitectura")
st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/diagrama_arq.png')
st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/5puntos.jpg')

st.header("Tecnologías usadas")
f1,f2,f3,f4=st.columns(4)
with f1:
    st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/Python_logo_and_wordmark.png', width=100)
with f2:
    st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/Snowflake_Logo.png', width=100)
with f3:
    st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/Pandas_logo.png', width=100)
with f4:
    st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/GitHub_logo.png', width=100)
g1,g2,g3,g4=st.columns(4)
with g1:
    st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/Streamlit.png', width=100)
with g2:
    st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/project.png', width=100)
with g3:
    st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/Mysql.png', width=100)
with g4:
    st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/airflow.png', width=100)

st.write('***')


# Initialize connection.
# Uses st.experimental_singleton to only run once.

cnn = snowflake.connector.connect(st.secrets["snowflake"])



sql ="""SELECT p.NOMBRE, e.VALOR  
            FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS)      
            WHERE e.ID_INDICADOR=28 AND e.ANIO=2020 AND e.ID_CONTINENTE=1
            ORDER BY e.VALOR DESC"""


st.write("snow username:", st.secrets["snowflake"])