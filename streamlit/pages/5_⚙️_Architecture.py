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

'''
1. busqueda de data y análisis para data cruda_.
2. Ingesta data cruda, limpieza y carga (ETL)_.
3. Tareas para la carga incremental_.
4.  Ingesta de data a base de datos relacional_.
5. Acceso a base de datos para modelar progreciones en machine lerning y visualización en dasboard_.
'''
st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/diagrama_solo.jpg')


'''
- La arquitectura sigue cinco pasos principales: el primero para analizar las fuentes de datos, el segundo para la Extracción, Trasformación (limpieza) y Carga (Load) llamado por sus siglas ETL. El tercer paso donde se realiza la carga incremental a la base de datos relacional, el cuarto la carga incremental y el último paso donde se realizan las consultas necesarias para ser utilizada en modelos de ML y visualización en dashboard.
- El entorno de trabajo para el ETL se desarrola en AIRFLOW dentro de una cloud maching de HEROKU. Acceso a la api: https://etl-latin-data.herokuapp.com/
- Para el armado del datalake se ingestan los datos en el entorno STAGE de SNOWFLAKE en formato .csv comprimido en .gz (pueden ser tambien json, parquet, xlsx).
- En el caso de la base de datos relacional se utiliza SNOWFLAKE con la creación de un warehouse para su mantenimiento e ingesta incremental.
- para el modelado en ML y visualización de datos se realiza querys según los requerimientos del cliente.
'''





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



col1,col2=st.columns(2)

with col1:
    option_pais = st.selectbox(
        'Elegir el país de la lista despleglable',
        lista_codigo_pais) #lista_codigo_pais

    eleccion_pais=dic_pais2[option_pais]
    id_pais=dic_id_pais[option_pais] #option

    'La selección fue:', eleccion_pais #dic_pais2[option]

with col2:
    option_var = st.selectbox(
            'Elegir la variable de la lista despleglable',
            code_indicador) #lista_codigo_pais

    
    dict_keys=list(dic_indicador.keys())
    dict_values=list(dic_indicador.values())
    val_index=dict_values.index(option_var)
    id_var=dict_keys[val_index]

sql_esp =f"SELECT ANIO, VALOR FROM EV WHERE ID_INDICADOR=31 AND ANIO<=2020 AND ID_PAIS='{id_pais}'"
df_esp=run_query(sql_esp)

sql_var =f"SELECT ANIO, VALOR FROM EV WHERE ID_INDICADOR='{id_var}' AND ANIO<=2020 AND ID_PAIS='{id_pais}'"
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


fig.update_yaxes(title_text="<b>primary</b> yaxis title", secondary_y=False)
fig.update_yaxes(title_text="<b>secondary</b> yaxis title", secondary_y=True)
st.plotly_chart(fig,use_container_width=True)

