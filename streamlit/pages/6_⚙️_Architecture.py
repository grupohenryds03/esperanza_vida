import streamlit as st



st.set_page_config(
    page_title='Architecture',
    page_icon='⚙️',
)

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

'# Data arquitecture'


'_The data arquitectura follows five principal steps: The fish one to studio and analice the data source. The second one implementing data extraction from source. The third one where the data is transform and cleaning. The fourth one where the data is incrementally load into relational tables. And the last one implementing queries to extract data for machine learning  (ML) algorithms and visualice with charts in a dashboard._'

'## Detail description:'

'''
1. Finding and studying data source: First we analice the data from the World Bank (WB), World Health Organization  (WHO) and scientific papers publications finding the way to access data relative for life expectancy.
2. Extraction data: we use two methods to access data using PANDAS library in Visual Studio Code with PYTHON lenguaje.  One method with WBGAPI library that provides modern, pythonic access to the World Bank's data API. Another way was importing csv files directly from the WHO website.
3. Transforming crude data: for cleaning data we made and extensive EDA using different method. The best implementation for missing data over a time series was using a machine learning method calls KNNImputer from SKLEARN library that impute to blanks data  using the mean value from nearest neighbors.
'''
'## Diagram'

st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/diagrama_solo.jpg')


'4. Incrementally load: ones the data is transform we put it into SNOWFLAKE database as compress csv file. For manage the first steps calls ETL we use AIRFLOW annually tasks that is deploy in a cloud  computer HEROKU: https://etl-latin-data.herokuapp.com/ .For Incrementally load to relational tables we use schedule task inside SNOWFLAKE.'
st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/airflow_runing.png')
'5. ML and visualization: We use SQL querys to ingest data for ML training and predictions methods using PYCARET library. For the dashboard we implement STREAMLIT using PLOTLY library for charts.'
st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/diagrama_estrella.png')




# ------------------------- grafico comparativo de indicadores vs esperza vida -------------------

import pandas as pd
import snowflake.connector
from info import *
import plotly.graph_objects as go
from plotly.subplots import make_subplots



@st.experimental_singleton
def init_connection():
    return snowflake.connector.connect(
        user=st.secrets.snowflake.user,
    password=st.secrets.snowflake.password,
    account=st.secrets.snowflake.account,
    warehouse=st.secrets.snowflake.warehouse,
    database=st.secrets.snowflake.database, client_session_keep_alive=True
    )

conn = init_connection()

@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetch_pandas_all()


sql_ind="SELECT i.ID_INDICADOR , i.CODIGO, i.DESCRIPCION FROM INDICADOR i JOIN (SELECT DISTINCT ID_INDICADOR FROM EV) e ON e.ID_INDICADOR=i.ID_INDICADOR"
df_ind=run_query(sql_ind) # dataframe indicadores
sql_pais="SELECT p.ID_PAIS, p.CODIGO_PAIS, p.NOMBRE FROM PAIS p JOIN (SELECT DISTINCT ID_PAIS FROM EV) e ON e.ID_PAIS=p.ID_PAIS"
df_pais=run_query(sql_pais) # dataframe pais

col1,col2=st.columns(2)

with col1:
    option_pais = st.selectbox(
        'Elegir el país de la lista despleglable',
        df_pais.NOMBRE) 

with col2:
    option_ind = st.selectbox(
            'Elegir la variable de la lista despleglable',
            df_ind.DESCRIPCION) 

sql_esp =f"""SELECT ANIO, VALOR 
            FROM EV e
            JOIN (SELECT ID_PAIS FROM PAIS WHERE NOMBRE='{option_pais}') p
            ON e.ID_PAIS=p.ID_PAIS
            WHERE ID_INDICADOR=31 AND ANIO<=2020"""
df_esp=run_query(sql_esp) # dataframe esperanza vida

sql_ind =f"""SELECT ANIO, VALOR 
            FROM EV e
            JOIN (SELECT ID_INDICADOR FROM INDICADOR WHERE DESCRIPCION='{option_ind}') i
            ON e.ID_INDICADOR=i.ID_INDICADOR
            JOIN (SELECT ID_PAIS FROM PAIS WHERE NOMBRE='{option_pais}') p
            ON e.ID_PAIS=p.ID_PAIS
            WHERE e.ANIO<=2020"""
df_ind=run_query(sql_ind) # dataframe indicador elejido

titulo_grafico=f"Correlación entre espereanza de vida de {option_pais} contra {option_ind}"
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=df_esp.ANIO, 
                    y=df_esp.VALOR,
                    mode='lines',
                    marker_color='#FF0000',
                    name="esperanza de vida",
                    line=dict(width=0.8)),secondary_y=False)

fig.add_trace(go.Scatter(x=df_ind.ANIO, 
                    y=df_ind.VALOR,#option
                    mode='lines',
                    marker_color='#00FF00',
                    line=dict(width=0.8)),secondary_y=True)

fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
fig.update_yaxes(title_text="años", secondary_y=False)
fig.update_yaxes(secondary_y=True)
fig.update_layout(title=titulo_grafico)
st.plotly_chart(fig,use_container_width=True)



