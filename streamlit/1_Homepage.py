# streamlit_app.py

import streamlit as st
import snowflake.connector
import pandas as pd
from PIL import Image



st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

col1,col2,col3=st.columns(3)
with col2:
    st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/streamlit/LDlogo.png', width=200)


st.title("ANÁLISIS DE ESPERANZA DE VIDA")

st.sidebar.success("Select a page above.")

#if "my_input" not in st.session_state:
#    st.session_state["my_input"] = ""

#my_input = st.text_input("Input a text here", st.session_state["my_input"])
#submit = st.button("Submit")
#if submit:
#    st.session_state["my_input"] = my_input
#    st.write("You have entered: ", my_input)

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.header("La esperanza de vida difiere en función del lugar de nacimiento")
'''
Según datos de la Organización Mundial de la Salud (OMS), a escala mundial, la esperanza de vida de los niños 
nacidos en 2015 era de 71,4 años (73,8 años para las niñas y 69,1 para los niños), pero las perspectivas de 
cada niño en particular dependen del lugar de nacimiento. 

Señala que los recién nacidos en países de ingresos altos tienen una esperanza media de vida igual o superior a 80 años, 
mientras que los recién nacidos en países en el África subsahariana, tienen una esperanza de vida inferior a 60 años.

Las mujeres japonesas, cuya vida se prolonga de media 86,8 años, son las más longevas. En el caso de los hombres, 
es en Suiza donde más tiempo viven, con 81,3 años de media. La población de Sierra Leona tiene la esperanza de vida más 
baja de todo el mundo para ambos sexos: 50,8 años para las mujeres y 49,3 años para los hombres.
'''
st.subheader("¿Qué factores influyen en la Esperanza de Vida (EV)?")

'''
El mayor aumento en la EV se registró en la Región de África, en la que la 
esperanza de vida aumentó en 9,4 años hasta llegar a los 60 años, debido principalmente a las mejoras en la 
supervivencia infantil, los progresos en la lucha contra el paludismo y la ampliación del acceso a los 
antirretrovíricos para el tratamiento del VIH.

Aunque en países más desarrollados se ha visto que la EV depende de otros factores como consumo de tabaco, 
sobrepeso en menores de 5 años, contaminación del aire. Por lo que es un tema multifactorial que depende de la economía propia de cada país.

'''
a1,a2,a3=st.columns(3)
with a1:
    st.caption('1100')
    st.text("""
    millones de personas fuman tabaco""")
with a2:
    st.caption('156 millones')
    st.text('de menores de 5 años sufren retraso del crecimiento')
with a3:
    st.caption('42 millones')
    st.text('de menores de 5 años tienen sobrepeso')

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