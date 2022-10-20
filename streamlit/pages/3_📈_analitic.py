import streamlit as st
import pandas as pd
# se importa el conector de snowflake
import snowflake.connector 
# se importa del modulo de swnoflake la herramienta de pandas para ingestar un dataframe a una tabla de snowflake
from snowflake.connector.pandas_tools import write_pandas 


st.title("Projects")

st.write("You have entered", st.session_state["my_input"])

#se crea conexión
cnn = snowflake.connector.connect(
    user='grupods03',
    password='Henry2022#',
    account='nr28668.sa-east-1.aws',
    warehouse='DW_EV',
    database="LAKE")

#Consulta todos los países con indicador 2 --> Se hizo doble JOIN <--
sql ="SELECT p.NOMBRE, e.ANIO, e.VALOR, i.CODIGO as INDICADOR FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS) JOIN INDICADOR i ON (e.ID_INDICADOR=i.ID_INDICADOR) WHERE e.ID_INDICADOR=2" 
Indicador2=pd.read_sql(sql,cnn)

st.dataframe(Indicador2)