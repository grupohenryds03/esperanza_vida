import streamlit as st
import pandas as pd
import snowflake.connector
import plotly.graph_objects as go
import plotly.express as px
from info import *

#st.set_page_config(page_title="Analitics",page_icon='📈')

cnn = snowflake.connector.connect(
    user='grupods03',
    password='Henry2022#',
    account='nr28668.sa-east-1.aws',
    warehouse='DW_EV',
    database="LAKE")


'''
## Análisis y Presentación de Variables

_Se realizó una predicción de la Esperanza de Vida Promedio Anual utilizando como metodologia
una estimacion de series de tiempo univariada SIN variables Exógenas Automatizada para todos los paises de 
la Muestra_
'''


# se crean las tabs para mostrar las tablas, caluculadora y gráficos

tab1, tab2, tab3 , tab4= st.tabs(['Tendecia y Predicción',"Mapa Geo-Referenciado(EV)","Mapa de Calor(GDP per Cap)","Tabla de Predicciones"])
with tab1:
    option = st.selectbox(
    'Elegir el país de la lista despleglable',
    pais) #lista_codigo_pais

    dic_pais.get(option) 
    'La selección fue:', pais #dic_pais2[option]

    id_pais=dic_id_pais[dic_pais] #option

    df=pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/Prediccion_EV_10.csv')
    df.drop('Unnamed: 0',inplace=True, axis=1)
    YEAR=pd.DataFrame([2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030], columns=['YEAR'])
    df_prediccion=pd.concat([YEAR,df], axis=1)
    df_final=pd.concat([df_prediccion.YEAR,df_prediccion[dic_pais]], axis=1) #option

    sql =f"SELECT ANIO, ID_PAIS, VALOR FROM EV WHERE ID_INDICADOR=28 AND ANIO<=2020 AND ID_PAIS='{id_pais}'"
    df_anterior=pd.read_sql(sql,cnn)

    'Predicciones de la Esperanza de Vida Promedio Anual para los Proximos 10 Años'
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_anterior.ANIO, 
                        y=df_anterior.VALOR,
                        mode='lines',
                        marker_color='#FF0000',
                        name=dic_pais,#option
                        line=dict(width=0.8)))

    fig.add_trace(go.Scatter(x=df_final.YEAR, 
                        y=df_final[dic_pais],#option
                        mode='lines',
                        marker_color='#00FF00',
                        name='Predicción Esperanza de Vida',
                        line=dict(width=0.8)))

    fig.update_xaxes(showgrid=False)
    st.plotly_chart(fig,use_container_width=True)

sql ="""SELECT p.CODIGO_PAIS, e.ANIO, e.VALOR, i.DESCRIPCION as INDICADOR 
        FROM EV e 
        JOIN INDICADOR i 
        ON (e.ID_INDICADOR=i.ID_INDICADOR)
        JOIN PAIS p
        on (e.ID_PAIS=p.ID_PAIS)
        WHERE e.ID_INDICADOR=28 AND e.ANIO>1960 AND e.ANIO<=2020 """ 
EV_todos=pd.read_sql(sql,cnn)

with tab2:
    
    'Mapa Geo-Referenciado de la Esperanza de Vida Promedio Anual por Pais'
    fig2 = px.choropleth(
                        EV_todos,
                        locations="CODIGO_PAIS",
                        color="VALOR",
                        hover_name="CODIGO_PAIS",
                        animation_frame="ANIO",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        projection="natural earth",
                        title='Esperanza de Vida')
    fig2.update_layout(margin={"r":10,"t":50,"l":10,"b":10},width=900, 
                  height=600) 
    st.plotly_chart(fig2,use_container_width=True)

sql ="""SELECT p.CODIGO_PAIS, e.ANIO, e.VALOR, i.DESCRIPCION as INDICADOR 
        FROM EV e 
        JOIN INDICADOR i 
        ON (e.ID_INDICADOR=i.ID_INDICADOR)
        JOIN PAIS p
        on (e.ID_PAIS=p.ID_PAIS)
        WHERE e.ID_INDICADOR=31 AND e.ANIO>1960 AND e.ANIO<=2020 """ 
GDP_todos=pd.read_sql(sql,cnn)

with tab3:
    'Mapa de Calor del GDP Per Capita promedio Anual (En U$S Constantes del 2015) por Pais'
    fig3 = px.scatter_geo(GDP_todos,
                            locations='CODIGO_PAIS',
                            color='CODIGO_PAIS',
                            hover_name='CODIGO_PAIS',
                            size=GDP_todos['VALOR'],
                            animation_frame='ANIO',
                            projection='natural earth',
                            title='GDP per Capita (constant 2015 US$)',
                            template='simple_white')
    fig3.update_layout(margin={"r":10,"t":50,"l":10,"b":10},width=900, 
                  height=600)
    st.plotly_chart(fig3,use_container_width=True)
with tab4:
    st.dataframe(df_prediccion)

st.write('***')
st.subheader('Carga incremental')
'''
La ingesta de datos desde la API del banco mundial y la OMS se programan anualmente mediante airflow.
'''
st.video('https://youtu.be/iXmhOic_WME')



