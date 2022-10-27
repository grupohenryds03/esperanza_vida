import streamlit as st
import pandas as pd
import snowflake.connector
import plotly.graph_objects as go
import plotly.express as px
from info import *

st.set_page_config(
    page_title="Forecast",
    page_icon="📶",
)

cnn = snowflake.connector.connect(
    user=st.secrets.snowflake.user,
    password=st.secrets.snowflake.password,
    account=st.secrets.snowflake.account,
    warehouse=st.secrets.snowflake.warehouse,
    database=st.secrets.snowflake.database)


'''
## Forecast and Analysis of the Target Varible

_Se realizó una predicción de la Esperanza de Vida Promedio Anual utilizando como metodologia
una estimacion de series de tiempo univariada SIN variables Exógenas Automatizada para todos los paises de 
la Muestra_
'''


tab1, tab2= st.tabs(['FORECAST - Life Expectancy',"Prediction Table"])
with tab1:
    option = st.selectbox(
    'Elegir el país de la lista despleglable',
    pais) #lista_codigo_pais

    a=dic_pais.get(option)
    'La selección fue:', option #dic_pais2[option]
    
    id_pais=dic_id_pais[a] #option

    df=pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/Prediccion_EV_10.csv')
    df.drop('Unnamed: 0',inplace=True, axis=1)
    YEAR=pd.DataFrame([2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029,2030], columns=['YEAR'])
    df_prediccion=pd.concat([YEAR,df], axis=1)
    df_final=pd.concat([df_prediccion.YEAR,df_prediccion[a]], axis=1) #option

    sql =f"SELECT ANIO, ID_PAIS, VALOR FROM EV WHERE ID_INDICADOR=31 AND ANIO<=2020 AND ID_PAIS='{id_pais}'"
    df_anterior=pd.read_sql(sql,cnn)

    'Predicciones de la Esperanza de Vida Promedio Anual para los Proximos 10 Años'
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_anterior.ANIO, 
                        y=df_anterior.VALOR,
                        mode='lines',
                        marker_color='#FF0000',
                        name=a,#option
                        line=dict(width=2)))

    fig.add_trace(go.Scatter(x=df_final.YEAR, 
                        y=df_final[a],#option
                        mode='lines',
                        marker_color='#00FF00',
                        name='Predicción Esperanza de Vida',
                        line=dict(width=2)))

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, griddash='dot', gridwidth=0.5, gridcolor='White')
    fig.update_yaxes(title_text="años")
    st.plotly_chart(fig,use_container_width=True)

sql ="""SELECT p.CODIGO_PAIS, e.ANIO, e.VALOR, i.DESCRIPCION as INDICADOR 
        FROM EV e 
        JOIN INDICADOR i 
        ON (e.ID_INDICADOR=i.ID_INDICADOR)
        JOIN PAIS p
        on (e.ID_PAIS=p.ID_PAIS)
        WHERE e.ID_INDICADOR=31 AND e.ANIO>1960 AND e.ANIO<=2020 """ 
EV_todos=pd.read_sql(sql,cnn)

with tab2:
    st.dataframe(df_prediccion)

df_models=pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/Pycaret_Models.csv')

st.dataframe(df_models)