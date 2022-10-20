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
    Nation)

st.write('You selected:', option)




sql ="""SELECT p.NOMBRE, e.ANIO, e.VALOR, i.CODIGO as INDICADOR 
        FROM EV e 
        JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS) 
                JOIN INDICADOR i ON (e.ID_INDICADOR=i.ID_INDICADOR)
        WHERE e.ID_INDICADOR=2"""
df=pd.read_sql(sql,cnn)

st.dataframe(df)

cnn.close
conn.close()