import streamlit as st
import pandas as pd
import snowflake.connector
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



sql =f"SELECT e.ID_PAIS, e.ANIO, e.VALOR, i.DESCRIPCION as INDICADOR FROM EV e JOIN INDICADOR i ON (e.ID_INDICADOR=i.ID_INDICADOR) WHERE e.ID_INDICADOR=28 AND e.ANIO>1960 AND e.ANIO<=2020 AND e.ID_PAIS='{option}'" 
df=pd.read_sql(sql,cnn)

st.dataframe(df)

cnn.close
