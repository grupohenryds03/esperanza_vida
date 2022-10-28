import streamlit as st



st.set_page_config(
    page_title='Architecture',
    page_icon='⚙️',
)

page_style = """
            <style>
            [data-testid="stAppViewContainer"] {
            background-color: #d9e3fa;
            background-image: url("https://github.com/grupohenryds03/esperanza_vida/blob/main/imagenes/clock_background2.png?raw=true");
            background-size: cover;
            background-position: left;
            }
            [data-testid="stSidebar"]{
            background-image: url("https://github.com/grupohenryds03/esperanza_vida/blob/main/imagenes/life.jpg?raw=true");
            background-size: cover;
            background-position: right;
            }
            </style>
            """
st.markdown(page_style, unsafe_allow_html=True)
'# Data arquitecture'


'_The data architecture follows five main steps: the first one to study and analyze the data source. The second one implements data extraction from the source. The third one is where the data is transform and cleaned. The fourth one is where the data is incrementally load into relational tables. And, the last one implements queries to extract data for machine learning (ML) algorithms and visualizes it by charts in the dashboard._'
'### Detail description:'

'''
1. Finding and studying data source: First we analyze the data from the World Bank (WB), World Health Organization (WHO) and scientific papers publications finding the way to access relative data for life expectancy.
2. Extraction data: we use two methods to access data using PANDAS library in Visual Studio Code with PYTHON language. One method was with WBGAPI library that provides modern, pythonic__ access to the World Bank's data API. Another way was importing csv files directly from the WHO website.
3. Transforming crude data: to clean data we made an extensive EDA using different method. The best implementation for missing data over a time series was using a machine learning method called KNNImputer from SKLEARN library that imputes to blanks data using the mean value from the nearest neighbors.
4. Incrementally load: once the data is transformed, we uploaded it into SNOWFLAKE database as a compress csv file. To manage the first steps ETL calls, we use AIRFLOW´s annually tasks that is deployed in a computer cloud HEROKU: https://etl-latin-data.herokuapp.com/ .For the incrementally load to relational tables we used scheduled tasks inside SNOWFLAKE database.
5. ML and visualization: We use SQL queries to ingest data for ML training and predictions methods using PYCARET library. For the dashboard, we implemented STREAMLIT using PLOTLY library for charts.
'''
'### architecture with images'

tab1, tab2, tab3 , tab4, tab5= st.tabs(['Architecture Diagram',"Airflow ELT runing","Relational tables diagram","snowflake tasks", "Demo video"])
with tab1:
    st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/diagrama_solo.jpg', caption='Arquitecture Diagram')
with tab2:
    st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/airflow_runing.png',caption='Airflow ELT runing')
with tab3:
    st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/diagrama_estrella.png',caption='Star Diagram for relational tables in snowflake data warerhouse')
with tab4:
    st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/snow-tasks.png',caption='Incremetal load with snowflake tasks')
with tab5:
    'Demo for ETL and incremental load'
    st.video('https://youtu.be/iXmhOic_WME')


'### Collaborative group job'

'- for collaborative job grupo  we work on VISUAL STUDIO CODE (VSC) platform in local machine on a GTIHUB cloud clone repository: https://github.com/grupohenryds03 '


'### Apps Documents'
f1,f2=st.columns(2)
with f1:
    'AIRFLOW: https://airflow.apache.org/docs/'
    'PANDAS: https://pandas.pydata.org/docs/'
    'SNOWFLAKE: https://docs.snowflake.com/en/'
    'STREAMLIT:https://docs.streamlit.io/'
    'GITHUB: https://docs.github.com/es'
with f2:
    'PYCARET: https://pycaret.gitbook.io/docs/'
    'WBAPI:https://pypi.org/project/wbgapi/'
    'PLOTLY:https://plotly.com/python/'
    'SKLEARN: https://scikit-learn.org/stable/user_guide.html'

st.write('***')
st.subheader('Carga incremental')
'''
La ingesta de datos desde la API del banco mundial y la OMS se programan anualmente mediante airflow.
'''
st.video('https://youtu.be/iXmhOic_WME')



