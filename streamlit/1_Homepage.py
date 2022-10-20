# streamlit_app.py

import streamlit as st
import snowflake.connector
import pandas as pd
from PIL import Image



st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.image(Image.open('latin-data-logo.png'), width=100)

st.title("Main Page")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

conn = init_connection() # connect


cnn = snowflake.connector.connect(
    user='grupods03',
    password='Henry2022#',
    account='nr28668.sa-east-1.aws',
    warehouse='DW_EV',
    database="LAKE")


sql ="""SELECT p.NOMBRE, e.ANIO, e.VALOR, i.CODIGO as INDICADOR 
        FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS) 
                JOIN INDICADOR i ON (e.ID_INDICADOR=i.ID_INDICADOR)
        WHERE e.ID_INDICADOR=2"""
df=pd.read_sql(sql,cnn)

st.dataframe(df)

cnn.close
conn.close()