import streamlit as st
import pandas as pd
import snowflake.connector
import plotly.graph_objects as go
import plotly.express as px
from info import *

st.set_page_config(
    page_title="Multipage App",
    page_icon="📈",
)

cnn = snowflake.connector.connect(
    user='grupods03',
    password='Henry2022#',
    account='nr28668.sa-east-1.aws',
    warehouse='DW_EV',
    database="LAKE")

st.set_page_config(
    page_title="Multipage App",
    page_icon="💡",
)

'''
# Análisis de las predicción de esperanza de vida

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

sql =f"SELECT ANIO, ID_PAIS, VALOR FROM EV WHERE ID_INDICADOR=28 AND ANIO<=2020 AND ID_PAIS='{option}'"
df_anterior=pd.read_sql(sql,cnn)

sql ="""SELECT e.ID_PAIS, e.ANIO, e.VALOR, 
        i.DESCRIPCION as INDICADOR FROM EV e JOIN INDICADOR i ON (e.ID_INDICADOR=i.ID_INDICADOR) 
        WHERE e.ID_INDICADOR=28 AND e.ANIO>1960 AND e.ANIO<=2020 """ 
EV_todos=pd.read_sql(sql,cnn)


# se crean las tabs para mostrar las tablas, caluculadora y gráficos

tab1, tab2, tab3 , tab4= st.tabs(['tendecia predicion',"mapa georeferenciado","mapa calor","Tabla Predicciones"])
with tab1:
    'El análisis de las prediciones de la esperanza de visa se utilizaron modelos predictivos.....'
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
    
    'mapa geo referenciado del promedio por año de la esperanza de vida por pais......'
    fig2 = px.choropleth(
                        EV_todos,
                        locations="ID_PAIS",
                        color="VALOR",
                        hover_name="ID_PAIS",
                        animation_frame="ANIO",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        projection="natural earth",
                        title='Esperanza de Vida')
    fig2.update_layout(margin={"r":10,"t":50,"l":10,"b":10},width=900, 
                  height=600) 
    st.plotly_chart(fig2,use_container_width=True)
with tab3:
    'mapa de calor del promedio por año de la esperanza de vida por pais......'
    fig3 = px.scatter_geo(EV_todos,
                            locations='ID_PAIS',
                            color='ID_PAIS',
                            hover_name='ID_PAIS',
                            size=EV_todos['VALOR'],
                            animation_frame='ANIO',
                            projection='natural earth',
                            title='Esperanza de Vida',
                            template='simple_white')
    fig3.update_layout(margin={"r":10,"t":50,"l":10,"b":10},width=900, 
                  height=600)
    st.plotly_chart(fig3,use_container_width=True)
with tab4:
    st.dataframe(df_prediccion)



