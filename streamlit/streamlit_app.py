# streamlit_app.py

import streamlit as st
import snowflake.connector

Nation = ['United States', 'Canada','Mexico','Costa Rica','Panama','Brazil','Argentina','Chile','Uruguay','Bolivia','Peru','Egypt, Arab Rep.','Libya','South Africa','Nigeria','Morocco','Australia','China','India','Thailand','Japan','Korea, Rep.','Israel','Saudi Arabia','Malaysia','Indonesia','Russian Federation','Turkiye','Spain','Bulgaria','France','Italy','Germany','United Kingdom','Norway','Sweden','Greece']
Nation_code= ['USA','CAN','MEX','CRI','PAN','BRA','ARG','CHL','URY','BOL','PER','EGY','LBY','ZAF','NGA','MAR','AUS','CHN','IND','THA','JPN','KOR','ISR','SAU','MYS','IDN','RUS','TUR','ESP','BGR','FRA','ITA','DEU','GBR','NOR','SWE','GRC']
Indicador = ['Average precipitation in depth (mm per year)',
'emisiones de CO2 (kt)',
'crecimiento de la poblacion (% anual)',
'Educational attainment, at least completed primary, population 25+ years, female (%) (cumulative)',
'School enrollment, tertiary (% gross)',
'Tasa de alfabetizacion, total adultos (% de personas)',
'Hepatitis B (HepB3) immunization coverage among 1-year-olds (%)',
'Immunization, DPT (% of children ages 12-23 months)',
'Immunization, measles (% of children ages 12-23 months)',
'Incidence of HIV, all (per 1,000 uninfected population)',
'Mortality rate, under-5 (per 1,000 live births)',
'Number of deaths ages 5-9 years',
'Number of infant deaths (per 1,000 live births)',
'Polio (Pol3) immunization covergae among 1-year-olds (%)',
'prevalencia del consumo de tabaco, hombres',
'prevalencia del consumo de tabaco, mujeres',
'tasa de mortalidad materna (cada 100.000 nacidos vivos)',
'tasa de mortalidad menores de 5 años (por 1000nacidos vivos)',
'tasa de mortalidad, adultos hombres (por cada 1000 adultos)',
'tasa de mortalidad, adultos mujeres (por cada 1000 adultos)',
'Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age)',
'Access to clean fuels and technologies for cooking, rural (% of rural population)',
'Current education expenditure, primary (% of total expenditure in primary public institutions)',
'Current health expenditure (% of GDP)',
'desempleo total (% de la poblacion laboral)',
'esperanza de vida al nacer, hombres (años)',
'esperanza de vida al nacer, muejres (años)',
'esperanza de vida al nacer, Total (años)',
'gasto publico (% del pib)',
'gasto publico en educación, total (% del pbi)',
'GDP per capita (constant 2015 US$)',
'poblacion que vive en barrios marginales (% de la poblacion urbana)',
'Población Rural (% de la poblacion total)',
'poblacion urbana (%poblacion total)',
'Research and development expenditure (% of GDP)',
'Researchers in R&D (per million people)',
'tasa de recuento de la pobreza, multidimensional (%de la poblacion total)',
'Trade in services (% of GDP)'
]
Indicador_code = ['AG.LND.PRCP.MM',
'EN.ATM.CO2E.KT',
'SP.POP.GROW',
'SE.PRM.CUAT.FE.ZS',
'SE.TER.ENRR',
'SE.ADT.LITR.ZS',
'CSV from WHO',
'SH.IMM.IDPT',
'SH.IMM.MEAS',
'SH.HIV.INCD.TL.P3',
'SH.DYN.MORT',
'SH.DTH.0509',
'SH.DTH.IMRT.IN',
'CSV from WHO',
'SH.PRV.SMOK.MA',
'SH.PRV.SMOK.FE',
'SH.STA.MMRT',
'SH.DYN.MORT',
'SP.DYN.AMRT.MA',
'SP.DYN.AMRT.FE',
'SH.ALC.PCAP.LI',
'EG.CFT.ACCS.RU.ZS',
'SE.XPD.CPRM.ZS',
'SH.XPD.CHEX.GD.ZS',
'SL.UEM.TOTL.NE.ZS',
'SP.DYN.LE00.MA.IN',
'SP.DYN.LE00.FE.IN',
'SP.DYN.LE00.IN',
'GC.XPN.TOTL.GD.ZS',
'SE.XPD.TOTL.GD.ZS',
'NY.GDP.PCAP.KD',
'EN.POP.SLUM.UR.ZS',
'SP.RUR.TOTL.ZS',
'SP.URB.TOTL.IN.ZS',
'GB.XPD.RSDV.GD.ZS',
'SP.POP.SCIE.RD.P6',
'SI.POV.MDIM',
'BG.GSR.NFSV.GD.ZS'
]

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

conn = init_connection() # conect

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

run_query("Use database PRUEBA;")
rows = run_query("SELECT * from COSTUMERS;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")