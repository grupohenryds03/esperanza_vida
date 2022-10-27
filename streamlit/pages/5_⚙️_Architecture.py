import streamlit as st
import pandas as pd
import snowflake.connector

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



'## Arquitectura'


'1. busqueda de data y análisis para data cruda'
'2. Ingesta data cruda, limpieza y carga (ETL)'
'3. Tareas para la carga incremental'
'4.  Ingesta de data a base de datos relacional'
'5. Acceso a base de datos para modelar progreciones en machine lerning y visualización en dasboard'

st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/diagrama_solo.jpg')

'''
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
'''

# Initialize connection.
# Uses st.experimental_singleton to only run once.
cnn = snowflake.connector.connect(
    user=st.secrets.snowflake.user,
    password=st.secrets.snowflake.password,
    account=st.secrets.snowflake.account,
    warehouse=st.secrets.snowflake.warehouse,
    database=st.secrets.snowflake.database)


sql ="""SELECT p.NOMBRE, e.VALOR  
            FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS)      
            WHERE e.ID_INDICADOR=28 AND e.ANIO=2020 AND e.ID_CONTINENTE=1
            ORDER BY e.VALOR DESC"""

df=pd.read_sql(sql,cnn)

st.dataframe(df)


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

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetch_pandas_all()

df2=run_query(sql)
st.dataframe(df2)