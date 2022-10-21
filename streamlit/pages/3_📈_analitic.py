import streamlit as st
import pandas as pd
import snowflake.connector
import plotly.graph_objects as go
from info import *

cnn = snowflake.connector.connect(
    user='grupods03',
    password='Henry2022#',
    account='nr28668.sa-east-1.aws',
    warehouse='DW_EV',
    database="LAKE")


'''
# This is the document title

_This is some markdown_
'''



option = st.selectbox(
    'Elejir el país de la lista despleglable',
    id_pais)

df=pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/Prediccion_EV_10.csv')
df.drop('Unnamed: 0',inplace=True, axis=1)
YEAR=pd.DataFrame([2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030], columns=['YEAR'])
df_prediccion=pd.concat([YEAR,df], axis=1)
df_final=pd.concat([df_prediccion.YEAR,df_prediccion[option]], axis=1)

sql =f"SELECT ANIO, ID_PAIS, VALOR FROM EV WHERE ID_INDICADOR=28 e.ANIO>1960 AND e.ANIO<=2020 AND ID_PAIS='{option}'"
df_anterior=pd.read_sql(sql,cnn)


# se crean las tabs para mostrar las tablas, caluculadora y gráficos

tab1, tab2, tab3 , tab4= st.tabs(['tendecia predicion',"mapa georeferenciado","mapa calor","Tabla Predicciones"])
with tab1:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_anterior.ANIO, 
                        y=df_anterior.VALOR,
                        mode='lines',
                        marker_color='#FF0000',
                        name=option,
                        line=dict(width=0.8)))

    fig.add_trace(go.Scatter(x=df_final.YEAR, 
                        y=df_final[option],
                        mode='lines',
                        marker_color='#00FF00',
                        name='predicción esperanza de vida',
                        line=dict(width=0.8)))

    fig.update_xaxes(showgrid=False)
    st.plotly_chart(fig,use_container_width=True)

with tab2:
    'HOLA'
with tab3:
    'HOLA'
with tab4:
    st.dataframe(df_prediccion)



