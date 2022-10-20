# streamlit_app.py

import streamlit as st
import snowflake.connector
import pandas as pd


st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

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

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
#@st.experimental_memo(ttl=600)
#def run_query(query):
#    with conn.cursor() as cur:
#        cur.execute(query)
#        return cur.fetchall()

def execute_query(connection, query):
    cursor = connection.cursor() # se inicializa la conexión Creates a cursor object. Each statement will be executed in a new cursor object.
    cursor.execute(query)
    cursor.close()

query = "Use database LAKE" # se inicializa database
execute_query(conn, query)

query1 = "Use warehouse DW_EV" # se inicializa datawarehouse
execute_query(conn, query1)


# Create a cursor object.
cur = conn.cursor()

sql ="SELECT p.NOMBRE, e.ANIO, e.VALOR, i.CODIGO as INDICADOR FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS) JOIN INDICADOR i ON (e.ID_INDICADOR=i.ID_INDICADOR)WHERE e.ID_INDICADOR=2"
#df=pd.read_sql(sql,conn)

# Execute a statement that will generate a result set.

cur.execute(sql)
# Fetch the result set from the cursor and deliver it as the Pandas DataFrame.
df = cur.fetch_pandas_all()
st.dataframe(df)

cur.close()
conn.close()