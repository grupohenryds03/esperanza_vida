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

page_style = """
            <style>
            
            [data-testid="stSidebar"]{
            background-image: url("https://github.com/grupohenryds03/esperanza_vida/blob/main/imagenes/life6.jpg?raw=true");
            background-size: cover;
            background-position: right;
            }
            </style>
            """
st.markdown(page_style, unsafe_allow_html=True)


cnn = snowflake.connector.connect(
    user=st.secrets.snowflake.user,
    password=st.secrets.snowflake.password,
    account=st.secrets.snowflake.account,
    warehouse=st.secrets.snowflake.warehouse,
    database=st.secrets.snowflake.database)


'''
## Forecast and analysis of target variable

_The prediction of the Annual Average Life Expectancy was made using an estimation of univariate time series WITHOUT automated exogenous 
variables as a methodology for all the countries of the Sample._
'''


tab1, tab2, tab3= st.tabs(['FORECAST - Life Expectancy',"Prediction Table",'Pycaret Forecast Models'])
with tab1:
    option = st.selectbox(
    'Choose the country from the Selectbox list',
    pais) #lista_codigo_pais

    a=dic_pais.get(option)
    'The Choose was:', option #dic_pais2[option]
    
    id_pais=dic_id_pais[a] #option

    df=pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/Prediccion_EV_10.csv')
    df.drop('Unnamed: 0',inplace=True, axis=1)
    YEAR=pd.DataFrame([2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029,2030], columns=['YEAR'])
    df_prediccion=pd.concat([YEAR,df], axis=1)
    df_final=pd.concat([df_prediccion.YEAR,df_prediccion[a]], axis=1) #option

    sql =f"SELECT ANIO, ID_PAIS, VALOR FROM EV WHERE ID_INDICADOR=31 AND ANIO<=2020 AND ID_PAIS='{id_pais}'"
    df_anterior=pd.read_sql(sql,cnn)

    'Annual Average Life Expectancy (LE) Predictions for the Next 10 Years'
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_anterior.ANIO, 
                        y=df_anterior.VALOR,
                        mode='lines',
                        marker_color='#FF0000',
                        name='Actual LE',#option
                        line=dict(width=2)))

    fig.add_trace(go.Scatter(x=df_final.YEAR, 
                        y=df_final[a],#option
                        mode='lines',
                        marker_color='#00FF00',
                        name='LE Forecast',
                        line=dict(width=2)))

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, griddash='dot', gridwidth=0.1, gridcolor='White')
    fig.update_yaxes(title_text="Years")
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

with tab3:
    '''
    ## Pycaret Forecast Models'''

    st.dataframe(df_models)