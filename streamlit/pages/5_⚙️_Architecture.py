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

'''
1. busqueda de data y análisis para data cruda
2. Ingesta data cruda, limpieza y carga (ETL)
3. Tareas para la carga incremental
4.  Ingesta de data a base de datos relacional
5. Acceso a base de datos para modelar progreciones en machine lerning y visualización en dasboard
'''
st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/diagrama_solo.jpg')


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


