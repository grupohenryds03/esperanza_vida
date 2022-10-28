import streamlit as st
import pandas as pd
import snowflake.connector
import plotly.graph_objects as go
import plotly.express as px
from info import *

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
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


cnn = snowflake.connector.connect(
    user=st.secrets.snowflake.user,
    password=st.secrets.snowflake.password,
    account=st.secrets.snowflake.account,
    warehouse=st.secrets.snowflake.warehouse,
    database=st.secrets.snowflake.database)

st.header("Life expectancy by Continent")

'''
Our first approach was to divide the countries by continent, to have a better view of the trends marked for each region. 
The first thing to note is that all countries have drastically improved their life expectancy
in a short period of time compared to what our civilization has in existence. This change was marked since the industrial revolution.
'''


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
                                showlegend = False,
                                
                                # marker=['Argentina'],color ='#00FF00'
                                #marker=dict(color = df['VALOR'].tolist(),colorscale='viridis')
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
                                line=dict(width=2)))
            
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
                                showlegend = False,
                                #marker=dict(color =df['VALOR'].tolist(),colorscale='viridis')
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
                                line=dict(width=2)))
            
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
                                showlegend = False,
                                #marker=dict(color=df['VALOR'].tolist(),colorscale='viridis')
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
                                line=dict(width=2)))
            
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
                                showlegend = False,
                                #marker=dict(color=df['VALOR'].tolist(),colorscale='viridis')
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
                                line=dict(width=2)))
            
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
                                showlegend = False,
                                marker=dict(color=df['VALOR'].tolist(),colorscale='viridis'))

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
                                line=dict(width=2)))
            
            layout = go.Layout(                                    
                                        xaxis_title='Year',
                                        yaxis_title='Life Expectancy (years)'
                                    )
            #fig.update_xaxes(showgrid=False)
            st.plotly_chart(fig2,use_container_width=True)
        plot()

st.write('***')

st.header("Life expectancy by Income")

'''
Another way to categorize the data is by income level, in this case we selected developed countries as one group and the developing countries as another group.
This way is easier to look for differences between different types of economies. In this case we can se how the gap is getting smaller with the pass of time, buy maybe not as quick as we all want.
'''


tab1, tab2, tab3 = st.tabs(['Developed','Developing','Developed vs Developing'])
with tab1:
        sql ="""SELECT e.ANIO, e.VALOR, p.NOMBRE 
                    FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS) JOIN INCOME i ON (e.ID_INCOME=i.ID_INCOME)    
                    WHERE e.ID_INDICADOR=31 AND i.ID_INCOME=0 AND e.ANIO=2020 ORDER BY e.VALOR DESC"""
        df=pd.read_sql(sql,cnn)
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
        
        
with tab2:
        sql ="""SELECT e.ANIO, e.VALOR, p.NOMBRE 
                    FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS) JOIN INCOME i ON (e.ID_INCOME=i.ID_INCOME)    
                    WHERE e.ID_INDICADOR=31 AND e.ANIO=2020 AND (i.ID_INCOME=1 OR i.ID_INCOME=2) ORDER BY e.VALOR DESC"""
        df=pd.read_sql(sql,cnn)
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
with tab3:     
    import numpy as np
    import pandas as pd
    import altair as alt

    df3=pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/income_df.csv')
    income=df3.melt('Year', var_name='category', value_name='y')

    line_chart = alt.Chart(income).mark_line(interpolate='basis').encode(
        alt.X('Year', title='Year'),
        alt.Y('y', title='Life Expectancy'),
        color='category:N'
    ).properties(
        title='Developed vs Undeveloped'
    )

    st.altair_chart(line_chart,use_container_width=True)   
            
            
st.write('***')

'''
## Analysis of variables

_Maps were made with the selected economic indicators to be able to globally 
compare the changes over time in the selected countries.
With these maps you have the possibility to compare global development over time_
'''


# se crean las tabs para mostrar las tablas, caluculadora y gráficos

tab1, tab2, tab3= st.tabs(["Heat Map","Geo-Referenced map","Complete table"])
    

lista_Kpi =['Infant Mortality','CO2 Emission','Rural Population (%)','GDP Per Capita','Life Expectancy']
lista_Kpi2 =['Infant_Mortality','CO2_Emission','Rural_Population (%)','GDP_Per Capita','Life_Expectancy']

with tab1:
    
    eleccion = st.selectbox(
    'Select Variable:',
    (lista_Kpi))

    if eleccion=='Infant Mortality':

            sql ="""SELECT p.CODIGO_PAIS, e.ANIO, e.VALOR, i.DESCRIPCION as INDICADOR 
                    FROM EV e 
                    JOIN INDICADOR i 
                    ON (e.ID_INDICADOR=i.ID_INDICADOR)
                    JOIN PAIS p
                    on (e.ID_PAIS=p.ID_PAIS)
                    WHERE i.CODIGO='SH.DYN.MORT' AND e.ANIO>1960 AND e.ANIO<=2020
                    ORDER BY e.ANIO ASC """ 
            EV_todos=pd.read_sql(sql,cnn)
    elif eleccion=='CO2 Emission':
            sql ="""SELECT p.CODIGO_PAIS, e.ANIO, e.VALOR, i.DESCRIPCION as INDICADOR 
                    FROM EV e 
                    JOIN INDICADOR i 
                    ON (e.ID_INDICADOR=i.ID_INDICADOR)
                    JOIN PAIS p
                    on (e.ID_PAIS=p.ID_PAIS)
                    WHERE e.ID_INDICADOR=5 AND e.ANIO>1960 AND e.ANIO<=2020 """ 
            EV_todos=pd.read_sql(sql,cnn)
    
    elif eleccion=='Rural Population (%)':
            sql ="""SELECT p.CODIGO_PAIS, e.ANIO, e.VALOR, i.DESCRIPCION as INDICADOR 
                    FROM EV e 
                    JOIN INDICADOR i 
                    ON (e.ID_INDICADOR=i.ID_INDICADOR)
                    JOIN PAIS p
                    on (e.ID_PAIS=p.ID_PAIS)
                    WHERE e.ID_INDICADOR=35 AND e.ANIO>1960 AND e.ANIO<=2020 """ 
            EV_todos=pd.read_sql(sql,cnn)

    elif eleccion=='GDP Per Capita':
            sql ="""SELECT p.CODIGO_PAIS, e.ANIO, e.VALOR, i.DESCRIPCION as INDICADOR 
                    FROM EV e 
                    JOIN INDICADOR i 
                    ON (e.ID_INDICADOR=i.ID_INDICADOR)
                    JOIN PAIS p
                    on (e.ID_PAIS=p.ID_PAIS)
                    WHERE e.ID_INDICADOR=9 AND e.ANIO>1960 AND e.ANIO<=2020 """ 
            EV_todos=pd.read_sql(sql,cnn)

    elif eleccion=='Life Expectancy':
            sql ="""SELECT p.CODIGO_PAIS, e.ANIO, e.VALOR, i.DESCRIPCION as INDICADOR 
                    FROM EV e 
                    JOIN INDICADOR i 
                    ON (e.ID_INDICADOR=i.ID_INDICADOR)
                    JOIN PAIS p
                    on (e.ID_PAIS=p.ID_PAIS)
                    WHERE e.ID_INDICADOR=31 AND e.ANIO>1965 AND e.ANIO<=2020 """ 
            EV_todos=pd.read_sql(sql,cnn)
    

    
    fig2 = px.choropleth(
                        EV_todos,
                        locations="CODIGO_PAIS",
                        color="VALOR",
                        hover_name="CODIGO_PAIS",
                        animation_frame="ANIO",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        projection="natural earth",
                        title=eleccion)
    fig2.update_layout(margin={"r":10,"t":50,"l":10,"b":10},width=900, 
                  height=600) 
    st.plotly_chart(fig2,use_container_width=True)



with tab2:

    eleccion2 = st.selectbox(
    'Select Variable:',
    (lista_Kpi2))

    if eleccion2=='Infant_Mortality':

            sql ="""SELECT p.CODIGO_PAIS, e.ANIO, e.VALOR, i.DESCRIPCION as INDICADOR 
                    FROM EV e 
                    JOIN INDICADOR i 
                    ON (e.ID_INDICADOR=i.ID_INDICADOR)
                    JOIN PAIS p
                    on (e.ID_PAIS=p.ID_PAIS)
                    WHERE i.CODIGO='SH.DYN.MORT' AND e.ANIO>1960 AND e.ANIO<=2020
                    ORDER BY e.ANIO ASC """ 
            GDP_todos=pd.read_sql(sql,cnn)
    elif eleccion2=='CO2_Emission':
            sql ="""SELECT p.CODIGO_PAIS, e.ANIO, e.VALOR, i.DESCRIPCION as INDICADOR 
                    FROM EV e 
                    JOIN INDICADOR i 
                    ON (e.ID_INDICADOR=i.ID_INDICADOR)
                    JOIN PAIS p
                    on (e.ID_PAIS=p.ID_PAIS)
                    WHERE e.ID_INDICADOR=5 AND e.ANIO>1960 AND e.ANIO<=2020 """ 
            GDP_todos=pd.read_sql(sql,cnn)
    
    elif eleccion2=='Rural_Population (%)':
            sql ="""SELECT p.CODIGO_PAIS, e.ANIO, e.VALOR, i.DESCRIPCION as INDICADOR 
                    FROM EV e 
                    JOIN INDICADOR i 
                    ON (e.ID_INDICADOR=i.ID_INDICADOR)
                    JOIN PAIS p
                    on (e.ID_PAIS=p.ID_PAIS)
                    WHERE e.ID_INDICADOR=35 AND e.ANIO>1960 AND e.ANIO<=2020 """ 
            GDP_todos=pd.read_sql(sql,cnn)

    elif eleccion2=='GDP_Per Capita':
            sql ="""SELECT p.CODIGO_PAIS, e.ANIO, e.VALOR, i.DESCRIPCION as INDICADOR 
                    FROM EV e 
                    JOIN INDICADOR i 
                    ON (e.ID_INDICADOR=i.ID_INDICADOR)
                    JOIN PAIS p
                    on (e.ID_PAIS=p.ID_PAIS)
                    WHERE e.ID_INDICADOR=9 AND e.ANIO>1960 AND e.ANIO<=2020 """ 
            GDP_todos=pd.read_sql(sql,cnn)

    elif eleccion2=='Life_Expectancy':
            sql ="""SELECT p.CODIGO_PAIS, e.ANIO, e.VALOR, i.DESCRIPCION as INDICADOR 
                    FROM EV e 
                    JOIN INDICADOR i 
                    ON (e.ID_INDICADOR=i.ID_INDICADOR)
                    JOIN PAIS p
                    on (e.ID_PAIS=p.ID_PAIS)
                    WHERE e.ID_INDICADOR=31 AND e.ANIO>1965 AND e.ANIO<=2020 """ 
            GDP_todos=pd.read_sql(sql,cnn)

    
    fig3 = px.scatter_geo(GDP_todos,
                            locations='CODIGO_PAIS',
                            color='CODIGO_PAIS',
                            hover_name='CODIGO_PAIS',
                            size=GDP_todos['VALOR'],
                            animation_frame='ANIO',
                            projection='natural earth',
                            title=eleccion2,
                            template='simple_white')
    fig3.update_layout(margin={"r":10,"t":50,"l":10,"b":10},width=900, 
                  height=600)
    st.plotly_chart(fig3,use_container_width=True)



with tab3:
    st.dataframe(EV_todos)
st.write('***')

'''
## LE for every country
'''
def plot ():
            sql2 ="""SELECT p.NOMBRE, e.ANIO, e.VALOR  
                FROM EV e JOIN PAIS p ON (e.ID_PAIS=p.ID_PAIS)      
                WHERE e.ID_INDICADOR=31"""
                
            df2=pd.read_sql(sql2,cnn)
            clist=df2["NOMBRE"].unique().tolist()
            
            countries = st.multiselect('Select country',clist ,['United States', 'Mexico', 'Argentina'])
            
            dfs={country: df2[df2["NOMBRE"]==country] for country in countries}
            
            fig2 = go.Figure()

            for country, df2 in dfs.items():
                fig2=fig2.add_trace(go.Scatter(x=df2["ANIO"], 
                                y=df2["VALOR"],
                                mode='lines',
                                name=country,
                                line=dict(width=2)))
            
            layout = go.Layout(                                    
                                        xaxis_title='Year',
                                        yaxis_title='Life Expectancy (years)'
                                    )
            #fig.update_xaxes(showgrid=False)
            st.plotly_chart(fig2,use_container_width=True)
plot()
cnn.close()



