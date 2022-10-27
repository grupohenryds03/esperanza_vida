import streamlit as st
import pandas as pd
import snowflake.connector
import plotly.graph_objects as go
import plotly.express as px
from info import *

st.set_page_config(
    page_title="Analitic",
    page_icon="📈",
)
page_style = """
            <style>
            [data-testid="stAppViewContainer"] {
            
            background-image: url("https://github.com/grupohenryds03/esperanza_vida/blob/main/imagenes/background-image.png?raw=true");
            background-size: cover;
            background-position: right;
            }
            [data-testid="stSidebar"]{
            background-image: url("https://github.com/grupohenryds03/esperanza_vida/blob/main/imagenes/WallpaperRocky.jpg?raw=true");
            background-size: cover;
            background-position: right;
            }
            </style>
            """
#background-Color: blue;
            
st.markdown(page_style, unsafe_allow_html=True)

cnn = snowflake.connector.connect(
    user=st.secrets.snowflake.user,
    password=st.secrets.snowflake.password,
    account=st.secrets.snowflake.account,
    warehouse=st.secrets.snowflake.warehouse,
    database=st.secrets.snowflake.database)

st.header("Life expectancy by Continent")




tab1, tab2, tab3 , tab4, tab5= st.tabs(["America","Europe","Asia","Africa","Oceania"])
with tab1:
        sql ="""SELECT p.NOMBRE, e.VALOR  
            FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS)      
            WHERE e.ID_INDICADOR=31 AND e.ANIO=2020 AND e.ID_CONTINENTE=1
            ORDER BY e.VALOR DESC"""
        df=pd.read_sql(sql,cnn)
        df=df.drop_duplicates()
        trace  = go.Bar(
                                x=df['NOMBRE'].tolist(),
                                y=df['VALOR'].tolist(),
                                showlegend = False
                                )

        layout = go.Layout(                                    
                                    xaxis_title='Country',
                                    yaxis_title='Life Expectancy (years)'
                                )
        data = [trace]
        fig = go.Figure(data=data,layout = layout)
        st.plotly_chart(fig)
        
        #Multiselect plot
        def plot ():
            sql2 ="""SELECT p.NOMBRE, e.ANIO, e.VALOR  
                FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS)      
                WHERE e.ID_INDICADOR=31 AND e.ID_CONTINENTE=1"""
                
            df2=pd.read_sql(sql2,cnn)
            clist=df2["NOMBRE"].unique().tolist()
            
            countries = st.multiselect('Select country',clist ,['United States', 'Canada', 'Mexico', 'Argentina'])
            
            dfs={country: df2[df2["NOMBRE"]==country] for country in countries}
            
            fig2 = go.Figure()

            for country, df2 in dfs.items():
                fig2=fig2.add_trace(go.Scatter(x=df2["ANIO"], 
                                y=df2["VALOR"],
                                mode='lines',
                                name=country,
                                line=dict(width=0.8)))
            
            layout = go.Layout(                                    
                                        xaxis_title='Year',
                                        yaxis_title='Life Expectancy (years)'
                                    )
            #fig.update_xaxes(showgrid=False)
            st.plotly_chart(fig2,use_container_width=True)
        plot()
with tab2:
        sql ="""SELECT p.NOMBRE, e.VALOR  
            FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS)      
            WHERE e.ID_INDICADOR=31 AND e.ANIO=2020 AND e.ID_CONTINENTE=3
            ORDER BY e.VALOR DESC"""
        df=pd.read_sql(sql,cnn)
        df=df.drop_duplicates()

        trace  = go.Bar(
                                x=df['NOMBRE'].tolist(),
                                y=df['VALOR'].tolist(),
                                showlegend = False
                                )

        layout = go.Layout(
                                    #title = 'EV Europa',
                                    xaxis_title='Country',
                                    yaxis_title='Life Expectancy (years)'
                                )
        data = [trace]
        fig = go.Figure(data=data,layout = layout)
        st.plotly_chart(fig)

        #Multiselect plot
        def plot ():
            sql2 ="""SELECT p.NOMBRE, e.ANIO, e.VALOR  
                FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS)      
                WHERE e.ID_INDICADOR=31 AND e.ID_CONTINENTE=3"""
                
            df2=pd.read_sql(sql2,cnn)
            clist=df2["NOMBRE"].unique().tolist()
            
            countries = st.multiselect('Select country',clist, ['Germany','United Kingdom', 'Norway', 'Spain'])
            
            dfs={country: df2[df2["NOMBRE"]==country] for country in countries}
            
            fig2 = go.Figure()

            for country, df2 in dfs.items():
                fig2=fig2.add_trace(go.Scatter(x=df2["ANIO"], 
                                y=df2["VALOR"],
                                mode='lines',
                                name=country,
                                line=dict(width=0.8)))
            
            layout = go.Layout(                                    
                                        xaxis_title='Year',
                                        yaxis_title='Life Expectancy (years)'
                                    )
            #fig.update_xaxes(showgrid=False)
            st.plotly_chart(fig2,use_container_width=True)
        plot()

with tab3:
        sql ="""SELECT p.NOMBRE, e.VALOR  
            FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS)      
            WHERE e.ID_INDICADOR=31 AND e.ANIO=2020 AND e.ID_CONTINENTE=2
            ORDER BY e.VALOR DESC"""
        df=pd.read_sql(sql,cnn)
        df=df.drop_duplicates()

        trace  = go.Bar(
                                x=df['NOMBRE'].tolist(),
                                y=df['VALOR'].tolist(),
                                showlegend = False
                                )

        layout = go.Layout(
                                    #title = 'EV Asia',
                                    xaxis_title='Country',
                                    yaxis_title='Life Expectancy (years)'
                                )
        data = [trace]
        fig = go.Figure(data=data,layout = layout)
        st.plotly_chart(fig)

        #Multiselect plot
        def plot ():
            sql2 ="""SELECT p.NOMBRE, e.ANIO, e.VALOR  
                FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS)      
                WHERE e.ID_INDICADOR=31 AND e.ID_CONTINENTE=2"""
                
            df2=pd.read_sql(sql2,cnn)
            clist=df2["NOMBRE"].unique().tolist()
            
            countries = st.multiselect('Select country',clist, ['Japan', 'China', 'India'])
            
            dfs={country: df2[df2["NOMBRE"]==country] for country in countries}
            
            fig2 = go.Figure()

            for country, df2 in dfs.items():
                fig2=fig2.add_trace(go.Scatter(x=df2["ANIO"], 
                                y=df2["VALOR"],
                                mode='lines',
                                name=country,
                                line=dict(width=0.8)))
            
            layout = go.Layout(                                    
                                        xaxis_title='Year',
                                        yaxis_title='Life Expectancy (years)'
                                    )
            #fig.update_xaxes(showgrid=False)
            st.plotly_chart(fig2,use_container_width=True)
        plot()

with tab4:
        sql ="""SELECT p.NOMBRE, e.VALOR  
            FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS)      
            WHERE e.ID_INDICADOR=31 AND e.ANIO=2020 AND e.ID_CONTINENTE=0
            ORDER BY e.VALOR DESC"""
        df=pd.read_sql(sql,cnn)
        df=df.drop_duplicates()

        trace  = go.Bar(
                                x=df['NOMBRE'].tolist(),
                                y=df['VALOR'].tolist(),
                                showlegend = False
                                )

        layout = go.Layout(
                                    #title = 'EV Africa',
                                    xaxis_title='Country',
                                    yaxis_title='Life Expectancy (years)'
                                )
        data = [trace]
        fig = go.Figure(data=data,layout = layout)
        st.plotly_chart(fig)

        #Multiselect plot
        def plot ():
            sql2 ="""SELECT p.NOMBRE, e.ANIO, e.VALOR  
                FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS)      
                WHERE e.ID_INDICADOR=31 AND e.ID_CONTINENTE=0"""
                
            df2=pd.read_sql(sql2,cnn)
            clist=df2["NOMBRE"].unique().tolist()
            
            countries = st.multiselect('Select country',clist, ['Morocco', 'South Africa', 'Nigeria'])
            
            dfs={country: df2[df2["NOMBRE"]==country] for country in countries}
            
            fig2 = go.Figure()

            for country, df2 in dfs.items():
                fig2=fig2.add_trace(go.Scatter(x=df2["ANIO"], 
                                y=df2["VALOR"],
                                mode='lines',
                                name=country,
                                line=dict(width=0.8)))
            
            layout = go.Layout(                                    
                                        xaxis_title='Year',
                                        yaxis_title='Life Expectancy (years)'
                                    )
            #fig.update_xaxes(showgrid=False)
            st.plotly_chart(fig2,use_container_width=True)
        plot()

with tab5:
        sql ="""SELECT p.NOMBRE, e.VALOR  
            FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS)      
            WHERE e.ID_INDICADOR=31 AND e.ANIO=2020 AND e.ID_CONTINENTE=4
            ORDER BY e.VALOR DESC"""
        df=pd.read_sql(sql,cnn)
        df=df.drop_duplicates()

        trace  = go.Bar(
                                x=df['NOMBRE'].tolist(),
                                y=df['VALOR'].tolist(),
                                showlegend = False
                                )

        layout = go.Layout(
                                   #title = 'EV Oceania',
                                    xaxis_title='Country',
                                    yaxis_title='Life Expectancy (years)'
                                )
        data = [trace]
        fig = go.Figure(data=data,layout = layout)
        st.plotly_chart(fig)

        #Multiselect plot
        def plot ():
            sql2 ="""SELECT p.NOMBRE, e.ANIO, e.VALOR  
                FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS)      
                WHERE e.ID_INDICADOR=31 AND e.ID_CONTINENTE=4"""
                
            df2=pd.read_sql(sql2,cnn)
            clist=df2["NOMBRE"].unique().tolist()
            
            countries = st.multiselect('Select country',clist, ['Australia'])
            
            dfs={country: df2[df2["NOMBRE"]==country] for country in countries}
            
            fig2 = go.Figure()

            for country, df2 in dfs.items():
                fig2=fig2.add_trace(go.Scatter(x=df2["ANIO"], 
                                y=df2["VALOR"],
                                mode='lines',
                                name=country,
                                line=dict(width=0.8)))
            
            layout = go.Layout(                                    
                                        xaxis_title='Year',
                                        yaxis_title='Life Expectancy (years)'
                                    )
            #fig.update_xaxes(showgrid=False)
            st.plotly_chart(fig2,use_container_width=True)
        plot()

cnn.close()


'''
## Análisis y Presentación de Variables

_Se realizó una predicción de la Esperanza de Vida Promedio Anual utilizando como metodologia
una estimacion de series de tiempo univariada SIN variables Exógenas Automatizada para todos los paises de 
la Muestra_
'''


# se crean las tabs para mostrar las tablas, caluculadora y gráficos

tab1, tab2, tab3 , tab4= st.tabs(['GRAFICO A PONER',"Mapa de Calor(GDP per Cap)","Mapa Geo-Referenciado(EV)","TABLA A PONER"])
with tab1:
    option = st.selectbox(
    'Elegir el país de la lista despleglable',
    pais) #lista_codigo_pais

    a=dic_pais.get(option)
    'La selección fue:', option #dic_pais2[option]
    
    id_pais=dic_id_pais[a] #option

    df=pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/Prediccion_EV_10.csv')
    df.drop('Unnamed: 0',inplace=True, axis=1)
    YEAR=pd.DataFrame([2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029,2030], columns=['YEAR'])
    df_prediccion=pd.concat([YEAR,df], axis=1)
    df_final=pd.concat([df_prediccion.YEAR,df_prediccion[a]], axis=1) #option

    sql =f"SELECT ANIO, ID_PAIS, VALOR FROM EV WHERE ID_INDICADOR=31 AND ANIO<=2020 AND ID_PAIS='{id_pais}'"
    df_anterior=pd.read_sql(sql,cnn)

    'Predicciones de la Esperanza de Vida Promedio Anual para los Proximos 10 Años'
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_anterior.ANIO, 
                        y=df_anterior.VALOR,
                        mode='lines',
                        marker_color='#FF0000',
                        name=a,#option
                        line=dict(width=2)))

    fig.add_trace(go.Scatter(x=df_final.YEAR, 
                        y=df_final[a],#option
                        mode='lines',
                        marker_color='#00FF00',
                        name='Predicción Esperanza de Vida',
                        line=dict(width=2)))

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, griddash='dot', gridwidth=0.5, gridcolor='White')
    fig.update_yaxes(title_text="años")
    st.plotly_chart(fig,use_container_width=True)

sql ="""SELECT p.CODIGO_PAIS, e.ANIO, e.VALOR, i.DESCRIPCION as INDICADOR 
        FROM EV e 
        JOIN INDICADOR i 
        ON (e.ID_INDICADOR=i.ID_INDICADOR)
        JOIN PAIS p
        on (e.ID_PAIS=p.ID_PAIS)
        WHERE e.ID_INDICADOR=31 AND e.ANIO>1960 AND e.ANIO<=2020 """ 
EV_todos=pd.read_sql(sql,cnn)

with tab2:
    
    'Mapa Geo-Referenciado de la Esperanza de Vida Promedio Anual por Pais'
    fig2 = px.choropleth(
                        EV_todos,
                        locations="CODIGO_PAIS",
                        color="VALOR",
                        hover_name="CODIGO_PAIS",
                        animation_frame="ANIO",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        projection="natural earth",
                        title='Esperanza de Vida')
    fig2.update_layout(margin={"r":10,"t":50,"l":10,"b":10},width=900, 
                  height=600) 
    st.plotly_chart(fig2,use_container_width=True)

sql ="""SELECT p.CODIGO_PAIS, e.ANIO, e.VALOR, i.DESCRIPCION as INDICADOR 
        FROM EV e 
        JOIN INDICADOR i 
        ON (e.ID_INDICADOR=i.ID_INDICADOR)
        JOIN PAIS p
        on (e.ID_PAIS=p.ID_PAIS)
        WHERE e.ID_INDICADOR=9 AND e.ANIO>1960 AND e.ANIO<=2020 """ 
GDP_todos=pd.read_sql(sql,cnn)

with tab3:



    'Mapa de Calor del GDP Per Capita promedio Anual (En U$S Constantes del 2015) por Pais'
    fig3 = px.scatter_geo(GDP_todos,
                            locations='CODIGO_PAIS',
                            color='CODIGO_PAIS',
                            hover_name='CODIGO_PAIS',
                            size=GDP_todos['VALOR'],
                            animation_frame='ANIO',
                            projection='natural earth',
                            title='GDP per Capita (constant 2015 US$)',
                            template='simple_white')
    fig3.update_layout(margin={"r":10,"t":50,"l":10,"b":10},width=900, 
                  height=600)
    st.plotly_chart(fig3,use_container_width=True)



with tab4:
    st.dataframe(df_prediccion)

st.write('***')
st.subheader('Carga incremental')
'''
La ingesta de datos desde la API del banco mundial y la OMS se programan anualmente mediante airflow.
'''
st.video('https://youtu.be/iXmhOic_WME')
st.write('***')


