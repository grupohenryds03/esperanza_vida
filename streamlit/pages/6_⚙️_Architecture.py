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

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

'# Data architecture'


'_The data arquitectura follows five principal steps: The fish one to studio and analice the data source. The second one implementing data extraction from source. The third one where the data is transform and cleaning. The fourth one where the data is incrementally load into relational tables. And the last one implementing queries to extract data for machine learning  (ML) algorithms and visualice with charts in a dashboard._'

'### Detail description:'

'''
1. Finding and studying data source: First we analice the data from the World Bank (WB), World Health Organization  (WHO) and scientific papers publications finding the way to access data relative for life expectancy.
2. Extraction data: we use two methods to access data using PANDAS library in Visual Studio Code with PYTHON lenguaje.  One method with WBGAPI library that provides modern, pythonic access to the World Bank's data API. Another way was importing csv files directly from the WHO website.
3. Transforming crude data: for cleaning data we made and extensive EDA using different method. The best implementation for missing data over a time series was using a machine learning method calls KNNImputer from SKLEARN library that impute to blanks data  using the mean value from nearest neighbors.
4. Incrementally load: ones the data is transform we put it into SNOWFLAKE database as compress csv file. For manage the first steps calls ETL we use AIRFLOW annually tasks that is deploy in a cloud  computer HEROKU: https://etl-latin-data.herokuapp.com/ .For Incrementally load to relational tables we use schedule task inside SNOWFLAKE.
5. ML and visualization: We use SQL querys to ingest data for ML training and predictions methods using PYCARET library. For the dashboard we implement STREAMLIT using PLOTLY library for charts.

'''
'### architecture with images'

tab1, tab2, tab3 , tab4, tab5= st.tabs(['Arquitecture Diagram',"Airflow ELT runing","Relational tables diagram","snowflake tasks", "Demo video"])
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

'- for collaborative grupo job we work on VISUAL STUDIO CODE (VSC) platform in local machine on a GTIHUB cloud clone repository: https://github.com/grupohenryds03 '


'### Apps Documentation'
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





