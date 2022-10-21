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
    st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/LDlogo.png', width=200)


st.title("ANÁLISIS DE ESPERANZA DE VIDA")

with st.sidebar:    
    st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/LDlogo.png', width=100)

#st.sidebar.success('')



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

Aunque en países más desarrollados se ha visto que la EV depende de otros factores, como el consumo de tabaco, 
el sobrepeso en menores de 5 años, la contaminación del aire. Por lo que es un tema multifactorial que depende de la economía propia de cada país.

Estudios de diferentes entidades demuestran que la esperanza de vida al nacer viene en
aumento año tras año. Diferentes factores son claves para descifrar el por qué del 
aumento de la esperanza de vida al nacer.
Desde la revolucón industrial en adelante se demostró que no solo afectan la EV los
facotres biológicos propianente dichos, sinó que también los factores socioeconómicos
fueron ganando terreno en la relevancia para la construcción de este índice.
'''

st.write('***')

a1,a2,a3=st.columns(3)
with a1:
    st.caption('1100 millones')
    '''
    de personas fuman tabaco'''
with a2:
    st.caption('156 millones')
    '''de menores de 5 años sufren retraso del crecimiento'''
with a3:
    st.caption('42 millones')
    '''de menores de 5 años tienen sobrepeso'''
st.write('***')
b1,b2,b3=st.columns(3)
with b1:
    st.caption('1800 millones')
    '''
    de personas beben agua contaminada '''
with b2:
    st.caption('946 millones')
    '''de personas defecan al aire libre'''
with b3:
    st.caption('3100 millones')
    '''de personas cocinan con combustibles contaminantes'''

st.write('***')
st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/paso_vida.jpeg')
c1,c2,c3=st.columns(3)
with c2:
    st.header("Objetivos")

'''
- Brindar asesoramiento a entidades públicas y privadas acerca de los posibles factores socioeconómicos y de salud más relevantes en las incidencia de la esperanza de vida al nacer.

- Ayudar a las distintas regiones o países a implementar políticas de estado, brindandoles las posibles causas que estan afectando la esperanza de vida al nacer.

- Aportar para lograr una mejor calidad de vida a partir de un cambio en los indicadores por región.
'''

d1,d2=st.columns(2)
with d1:
    st.subheader("Alcance")
    '''Ingesta de diferentes datasets con registros a partir del año 1960 para transformar estos datos en información de valor que permitan realizar consultas sobre la esperanza de vida al nacer en un período de tiempo específico o realizar predicciones a través de algoritmos de machine learning.'''
with d2:
    st.subheader("Fuera de alcance")
    '''El análisis y las predicciones proporcionadas no seran anteriores al año 1960.
    Las consultas no incluirán factores biológicos.
    La carga de datos será por lotes en diferentes formatos.'''
st.write('***')
e1,e2,e3=st.columns(3)
with e2:
    st.header("Arquitectura")
st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/diagrama_arq.png')

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