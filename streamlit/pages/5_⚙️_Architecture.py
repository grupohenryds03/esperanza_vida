import streamlit as st
import pandas as pd
import snowflake.connector
from info import *
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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

'La arquitectura sigue cinco pasos principales: el primero para analizar las fuentes de datos, el segundo para la Extracción, Trasformación (limpieza) y Carga (Load) llamado por sus siglas ETL. El tercer paso donde se realiza la carga incremental a la base de datos relacional, el cuarto la carga incremental y el último paso donde se realizan las consultas necesarias para ser utilizada en modelos de ML y visualización en dashboard.'
'''
1. Busqueda de data y análisis para data cruda.
2. Ingesta data cruda, limpieza y carga (ETL).
3. Tareas para la carga incremental.
4. Ingesta de data a base de datos relacional.
5. Acceso a base de datos para modelar progreciones en machine lerning y visualización en dasboard.

Diagrama de Arquitectura
'''
st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/diagrama_solo.jpg')



'- El entorno de trabajo para el ETL se desarrola en AIRFLOW dentro de una cloud maching de HEROKU. Acceso a la api: https://etl-latin-data.herokuapp.com/'
st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/airflow_runing.png')
'- Para el armado del datalake se ingestan los datos en el entorno STAGE de SNOWFLAKE en formato .csv comprimido en .gz (pueden ser tambien json, parquet, xlsx).'
'- En el caso de la base de datos relacional se utiliza SNOWFLAKE con la creación de un warehouse para su mantenimiento e ingesta incremental.'
st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/diagrama_estrella.png')
'- para el modelado en ML y visualización de datos se realiza querys según los requerimientos del cliente.'



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



sql_ind="SELECT * FROM INDICADOR i JOIN (SELECT DISTINCT ID_INDICADOR FROM EV) e ON e.ID_INDICADOR=i.ID_INDICADOR"
df_ind=run_query(sql_ind)
sql_pais="SELECT * FROM PAIS p JOIN (SELECT DISTINCT ID_PAIS FROM EV) e ON e.ID_PAIS=p.ID_PAIS"
df_pais=run_query(sql_pais)

col1,col2=st.columns(2)

with col1:
    option_pais = st.selectbox(
        'Elegir el país de la lista despleglable',
        df_pais.NOMBRE) #lista_codigo_pais

with col2:
    option_var = st.selectbox(
            'Elegir la variable de la lista despleglable',
            df_ind.DESCRIPCION) #lista_codigo_pais

sql_esp =f"""SELECT ANIO, VALOR 
            FROM EV e
            JOIN (SELECT ID_PAIS FROM PAIS WHERE NOMBRE='{option_pais}') p
            ON e.ID_PAIS=p.ID_PAIS
            WHERE ID_INDICADOR=31 AND ANIO<=2020;'"""
df_esp=run_query(sql_esp)

sql_var =f"""SELECT ANIO, VALOR 
            FROM EV e
            JOIN (SELECT ID_INDICADOR FROM INDICADOR WHERE DESCRIPCION='{option_var}') i
            ON e.ID_INDICADOR=i.ID_INDICADOR
            JOIN (SELECT ID_PAIS FROM PAIS WHERE NOMBRE='{option_pais}') p
            ON e.ID_PAIS=p.ID_PAIS
            WHERE e.ANIO<=2020;"""
df_var=run_query(sql_var)

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=df_esp.ANIO, 
                    y=df_esp.VALOR,
                    mode='lines',
                    marker_color='#FF0000',
                    name="esperanza de vida",
                    line=dict(width=0.8)),secondary_y=False)

fig.add_trace(go.Scatter(x=df_var.ANIO, 
                    y=df_var.VALOR,#option
                    mode='lines',
                    marker_color='#00FF00',
                    name=option_var,
                    line=dict(width=0.8)),secondary_y=True)

fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
fig.update_yaxes(title_text="años", secondary_y=False)
fig.update_yaxes(title_text="xxxx", secondary_y=True)
st.plotly_chart(fig,use_container_width=True)



