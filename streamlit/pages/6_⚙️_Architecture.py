import streamlit as st


st.set_page_config(
    page_title='Architecture',
    page_icon='⚙️',
)

page_style = """
            <style>
            [data-testid="stSidebar"]{
            background-image: url("https://github.com/grupohenryds03/esperanza_vida/blob/main/imagenes/life6.jpg?raw=true");
            background-size: cover;
            background-position: right;
            }
            </style>
            """
st.markdown(page_style, unsafe_allow_html=True)
'# Data architecture'


'_The data architecture follows five main steps: the first one is to study and analyze the data source. The second one extract particular data from the source. The third one is data transformation and cleaning. The fourth one is incremental load of data into the relational tables. Finally, the last step implements queries to extract data for machine learning (ML) algorithms and visualizes it by charts in the dashboard._'
'### Detail description:'

'''
1. Research and analyze the data sources: First we analyze the data from the World Bank (WB), World Health Organization (WHO) and scientific papers in order to find the way to access relative data related with life expectancy.
2. Extraction data: We use two methods to access data, using PANDAS library in Visual Studio Code with PYTHON language. One method was with WBGAPI library that provides modern, pythonic__ access to the World Bank's data API. The other way was importing csv files directly from the WHO website.
3. Transforming crude data: To clean data we made an extensive EDA, using different methods. The best implementation for missing data over a time series was using a machine learning method called: KNNImputer, from SKLEARN library. This method imputes data into blanks using the mean value from the nearest neighbors.
4. Incrementally load: once the data is transformed, we upload it into SNOWFLAKE database as a compressed csv file. To manage the first ETL steps  , we use AIRFLOW´s annually tasks, that is deployed in a HEROKU cloud computer  : https://etl-latin-data.herokuapp.com/ .For the incrementally load to relational tables we used scheduled tasks inside SNOWFLAKE database.
5. ML and visualization: We use SQL queries to ingest data for ML training and predictions methods using PYCARET library. For the dashboard, we implement STREAMLIT, using PLOTLY library for charts.
'''
'### Architecture with images'

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


'### Collaborative job'

'- For collaborative job we worked on VISUAL STUDIO CODE (VSC) platform in local machine, with notebooks connected toa  Github cloud clone repository: https://github.com/grupohenryds03 '
'- We also were sharing an excel sheet with google drive, where we collected the preliminar information for data analysis.'

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


