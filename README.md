# Latin-Data
## Proyecto Final -Data 03- Soy Henry
## Jhovany Lara, Rodrigo Ruiz, Pablo Poletti , José Toledo

<img src="/imagenes/Snowflake_Logo.png" width="300" height="100"/><img src="/imagenes/Pandas_logo.png" width="300" height="150"/><img src="/imagenes/Streamlit.png" width="300" height="150"/>

### Consigna: Desarrollo de un proyecto

- Para este proyecto final, se elegio la Esperanza de Vida al Nacer.


### Arquitectura: Ingesta data cruda, limpieza y carga (ETL) -> Armado de tareas para la carga incremental -> Ingesta de data a base de datos relacional -> Acceso a base de datos para modelar progreciones en machine lerning y visualización en dasboard

- La arquitectura sigue tres pasos principales: uno para la Extracción, Trasformación (limpieza) y Carga (Load) llamado por sus siglas ETL, un segundo paso donde se realiza la carga incremental a la base de datos relacional y el trecero donde se realizan las consltas necesarias para ser utilizada en modelos de ML.
- El entorno de trabajo para el ETL se desarrola en AIRFLOW dentro de una cloud maching de HEROKU.
- Para el armado del datalake se ingestan los datos en el entorno STAGE de SNOWFLAKE en formato .csv comprimido en .gz (pueden ser tambien json, parquet, xlsx).
- En el caso de la base de datos relacional se utiliza SNOWFLAKE con la creación de un warehouse para su mantenimiento e ingesta incremental.
- para el modelado en ML y visualización de datos se realiza querys según los requerimientos del cliente.

<img src="/imagenes/diagrama latin data.jpg"/>

| archivo                              | internal storage | tipo de compresión |
|--------------------------------------|------------------|--------------------|
| banco mundial.csv                    | snowflake        | .gz                |
| organización mundial de la salud.csv | snowflake        | .gz                |

- Para el armado del data warehouse se crean las tablas relacionales de hecho y dimensión con sus respectivos Id´s y primary keys.

- tabla de hecho

| col     | tipo   | key | 
|---------|--------|-----|
| Idpais  | int    | PK  |
| Codpais | string | -   |
| año     | int    | -   |
| income  | float  | -   |
| Idcont  | ..     | -   |
| IdVar   | float  | -   |

- tablas de dimesiones

- income

| col    | tipo   | key |
|--------|--------|-----|
| idPais | int    | PK  |
| pais   | string | -   |
| income | string | -   |

- geográfica

| col    | tipo   | key |
|--------|--------|-----|
| idPais | int    | PK  |
| pais   | string | -   |
| región | string | -   |


- Para la creación del dashboard se utiliza streamlit: https://latin-data.streamlitapp.com/

- Para el deploy del dashboard se utiliza la herramienta porpia streamlit.

### Descripción de los pasos para el trabajo colaborativo sin container docker:

- Para relaizar el trabajo colaborativo , se establece la conexión desde visual studio code local

- en terminal se crea el entorno de trabajo para realizar con la conexión con snowflake en visual studio code en maquina local con lenguaje phyton:

```python
 pip install conda #se descarga condas
 conda create -n dbconnect python=3.8 #creacion del entorno
 conda activate dbconnect #activar el entorno
 pip install snowflake-connector-python[pandas] #se instala el conector con snowflake
```

- para realizar la conexión a la base de datos de snowflake, se igresan lo siguientes comando en notebook de phyton:

```python
import snowflake.connector
conn = snowflake.connector.connect(
    user='xxxxx',
    password='xxxxxx',
    account='nrxxxx.sa-east-1.aws', # nombre de cuenta de snowflake con su región asgnada en cloud AWS
    role ='ACCOUNTADMIN', # tipo de rol
    )
```

### Documentación Paises elegidos

- Se selecciono una muestra de países teniendo en cuenta incluir estados de los 5 continentes que sean representativos, tengan buena calidad en la información histórica recolectada por el World Bank para la confección de sus indicadores.
-  Inicialmente se utilizó como filtro para diferenciar la muestra por continentes, el status de países “desarrollados” vs “en desarrollo”, pero tomando en cuenta la clasificación que realiza las naciones unidas se observo que tanto en América Latina, África como en Medio Oriente, se necesitaba incluir otro nivel de clasificación para mejorar la diferenciación; por lo cual se decidió utilizar la clasificación por nivel de ingresos que realiza el World Bank mediante el “GNI (Ingreso Bruto Nacional)  per cápita” y así poder mejorar la diferenciación de los efectos de las diferentes variables sobre la esperanza de vida, según el país o continente en estudio.

-tabla paises elejidos

| PAIS           | INCOME | CODE | CONTINENTE |
|----------------|--------|------|------------|
| USA            | H      | USA  | AMERICA    |
| CANADA         | H      | CAN  | AMERICA    |
| MEXICO         | M      | MEX  | AMERICA    |
| COSTA RICA     | M      | CRI  | AMERICA    |
| PANAMA         | H      | PAN  | AMERICA    |
| BRASIL         | M      | BRA  | AMERICA    |
| ARGENTINA      | M      | ARG  | AMERICA    |
| CHILE          | H      | CHL  | AMERICA    |
| URUGUAY        | H      | URY  | AMERICA    |
| BOLIVIA        | LM     | BOL  | AMERICA    |
| PERU           | M      | PER  | AMERICA    |
| EGIPTO         | LM     | EGY  | AFRICA     |
| LIBIA          | M      | LBY  | AFRICA     |
| SUDAFRICA      | M      | ZAF  | AFRICA     |
| NIGERIA        | LM     | NGA  | AFRICA     |
| MARRUECOS      | LM     | MAR  | AFRICA     |
| AUSTRALIA      | H      | AUS  | OCEANIA    |
| CHINA          | M      | CHN  | ASIA       |
| INDIA          | LM     | IND  | ASIA       |
| TAILANDIA      | M      | THA  | ASIA       |
| JAPON          | H      | JPN  | ASIA       |
| COREA DEL SUR  | H      | KOR  | ASIA       |
| ISRAEL         | H      | ISR  | ASIA       |
| ARABIA SAUDITA | H      | SAU  | ASIA       |
| MALASIA        | M      | MYS  | ASIA       |
| INDONESIA      | LM     | IDN  | ASIA       |
| RUSIA          | M      | RUS  | EUROPA     |
| TURQUIA        | M      | TUR  | EUROPA     |
| ESPAÑA         | H      | ESP  | EUROPA     |
| BULGARIA       | M      | BGR  | EUROPA     |
| FRANCIA        | H      | FRA  | EUROPA     |
| ITALIA         | H      | ITA  | EUROPA     |
| ALEMANIA       | H      | DEU  | EUROPA     |
| INGLATERRA     | H      | GBR  | EUROPA     |
| NORUEGA        | H      | NOR  | EUROPA     |
| SUECIA         | H      | SWE  | EUROPA     |
| GRECIA         | H      | GRC  | EUROPA     |

- tabla income

| TIPO INCOME | DESCRIPCIÓN         |
|-------------|---------------------|
| H           | HIGH INCOME         |
| M           | UPPER MEDIUM INCOME |
| LM          | LOW MEDIUM INCOME   |
| L           | LOW INCOME          |


### Documentación Paises variables elejidas

- de acuerdo a diferentes papers la seleccion de variables se separaron en salud y socio-económicas:
- papers realacionados

|                                                 Papers life expectancy                                                |                                   descripción                                   |
|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| http://www.scielo.org.pe/scielo.php?script=sci_arttext&pid=S1025-55832011000400006                                    |                                                                                 |
| https://ruc.udc.es/dspace/bitstream/handle/2183/16409/RodriguezRodriguez_David_TFG_2015.pdf?sequence=2                |                                                                                 |
| https://population.un.org/wpp/Publications/Files/WPP2022_Methodology.pdf                                              |                         Metodologia UN para proyecciones                        |
| https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/undesa_pd_2022_wpp_key-messages.pdf |                   Informe UN "World Population Prospects 2022"                  |
| https://www.kaggle.com/search?q=life+expectancy                                                                       |                                      KAGGLE                                     |
| https://www.kaggle.com/code/nilaychauhan/etl-pipelines-tutorial-world-bank-datasets                                   |                                                                                 |
| https://www.ucm.es/data/cont/docs/518-2016-09-15-Tema2_regresi%C3%B3n%20con%20series%20temporales.pdf                 |                  Analizar Correlacion Espuria (como filtrarla)                  |
| https://core.ac.uk/download/pdf/6264941.pdf                                                                           |              Correlacion Espuria (como filtrarla) Con cointegracion             |
| https://www.linkedin.com/pulse/la-correlaci%C3%B3n-de-todos-los-males-valent%C3%ADn-chab/?originalSubdomain=es        |                               Correlacion Espuria                               |
| https://statisticsbyjim.com/basics/spurious-correlation/                                                              |                                                                                 |
| https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6650812/                                                                 |                  A Causal Analysis of Life Expectancy at Birth.                 |
| https://hrcak.srce.hr/file/178666                                                                                     | Determinant Factors of Life Expectancy at Birth in the European Union Countries |
| https://rstudio-pubs-static.s3.amazonaws.com/180554_a412caa868c24939a873ca679d54bbde.html                             |                          8 variables a tener en cuenta                          |
| https://www.analyticslane.com/2019/11/18/test-de-causalidad-de-wiener-granger/                                        | granger causality test ejemplo en Python                                        |

- tabla de variables

|                                                                SERIE                                                                |       TIPO      |         ID        |
|:-----------------------------------------------------------------------------------------------------------------------------------:|:---------------:|:-----------------:|
| Population, total en millones no ratio (ver apartado)                                                                               |   Demografica   |    SP.POP.TOTL    |
| Number of under-five deaths                                                                                                         |      Salud      |    SH.DTH.MORT    |
| Prevalence of overweight, weight for height (% of children under 5)                                                                 |      Salud      |   SH.STA.OWGH.ZS  |
| Prevalence of wasting, weight for height (% of children under 5)                                                                    |      Salud      |   SH.STA.WAST.ZS  |
| CPIA policy and institutions for environmental sustainability rating (1=low to 6=high)                                              | Socio-Economica |   IQ.CPA.ENVR.XQ  |
| impuesto a las ganancias (% de las ganancias comerciales)                                                                           | Socio-Economica | GC.TAX.YPKG.RV.ZS |
| impuesto total y tasa de contribucion (% de la ganacia)                                                                             | Socio-Economica | IC.TAX.TOTL.CP.ZS |
| indice de capital humano (escala 0-1)                                                                                               | Socio-Economica |    HD.HCI.OVRL    |
| indice de pobreza multidimensional (escala 0-1)                                                                                     | Socio-Economica |   SI.POV.MDIM.XQ  |
| Primary income payments (BoP, current US$)                                                                                          | Socio-Economica |   BM.GSR.FCTY.CD  |
| Women participating in the three decisions (own health care, major household purchases, and visiting family) (% of women age 15-49) | Socio-Economica | SG.DMK.ALLD.FN.ZS |
| Total alcohol consumption per capita, female (liters of pure alcohol, projected estimates, female 15+ years of age)                 |      Salud      | SH.ALC.PCAP.FE.LI |
| Average precipitation in depth (mm per year)                                                                                        |    Climatica    |   AG.LND.PRCP.MM  |
| emisiones de CO2 (kt)                                                                                                               |    Climatica    |   EN.ATM.CO2E.KT  |
| crecimiento de la poblacion (% anual)                                                                                               |   Demografica   |    SP.POP.GROW    |
| Educational attainment, at least completed primary, population 25+ years, female (%) (cumulative)                                   |    Educacion    | SE.PRM.CUAT.FE.ZS |
| School enrollment, tertiary (% gross)                                                                                               |    Educacion    |    SE.TER.ENRR    |
| Tasa de alfabetizacion, total adultos (% de personas)                                                                               |    Educacion    |   SE.ADT.LITR.ZS  |
| Hepatitis B (HepB3) immunization coverage among 1-year-olds (%)                                                                     |      Salud      |    CSV from WHO   |
| Immunization, DPT (% of children ages 12-23 months)                                                                                 |      Salud      |    SH.IMM.IDPT    |
| Immunization, measles (% of children ages 12-23 months)                                                                             |      Salud      |    SH.IMM.MEAS    |
| Incidence of HIV, all (per 1,000 uninfected population)                                                                             |      Salud      | SH.HIV.INCD.TL.P3 |
| Mortality rate, under-5 (per 1,000 live births)                                                                                     |      Salud      |    SH.DYN.MORT    |
| Number of deaths ages 5-9 years                                                                                                     |      Salud      |    SH.DTH.0509    |
| Number of infant deaths (per 1,000 live births)                                                                                     |      Salud      |   SH.DTH.IMRT.IN  |
| Polio (Pol3) immunization covergae among 1-year-olds (%)                                                                            |      Salud      |    CSV from WHO   |
| prevalencia del consumo de tabaco, hombres                                                                                          |      Salud      |   SH.PRV.SMOK.MA  |
| prevalencia del consumo de tabaco, mujeres                                                                                          |      Salud      |   SH.PRV.SMOK.FE  |
| tasa de mortalidad materna (cada 100.000 nacidos vivos)                                                                             |      Salud      |    SH.STA.MMRT    |
| tasa de mortalidad menores de 5 años (por 1000nacidos vivos)                                                                        |      Salud      |    SH.DYN.MORT    |
| tasa de mortalidad, adultos hombres (por cada 1000 adultos)                                                                         |      Salud      |   SP.DYN.AMRT.MA  |
| tasa de mortalidad, adultos mujeres (por cada 1000 adultos)                                                                         |      Salud      |   SP.DYN.AMRT.FE  |
| Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age)                                |      Salud      |   SH.ALC.PCAP.LI  |
| Access to clean fuels and technologies for cooking, rural (% of rural population)                                                   | Socio-Economica | EG.CFT.ACCS.RU.ZS |
| Current education expenditure, primary (% of total expenditure in primary public institutions)                                      | Socio-Economica |   SE.XPD.CPRM.ZS  |
| Current health expenditure (% of GDP)                                                                                               | Socio-Economica | SH.XPD.CHEX.GD.ZS |
| desempleo total (% de la poblacion laboral)                                                                                         | Socio-Economica | SL.UEM.TOTL.NE.ZS |
| esperanza de vida al nacer, hombres (años)                                                                                          | Socio-Economica | SP.DYN.LE00.MA.IN |
| esperanza de vida al nacer, muejres (años)                                                                                          | Socio-Economica | SP.DYN.LE00.FE.IN |
| esperanza de vida al nacer, Total (años)                                                                                            | Socio-Economica |   SP.DYN.LE00.IN  |
| gasto publico (% del pib)                                                                                                           | Socio-Economica | GC.XPN.TOTL.GD.ZS |
| gasto publico en educación, total (% del pbi)                                                                                       | Socio-Economica | SE.XPD.TOTL.GD.ZS |
| GDP per capita (constant 2015 US$)                                                                                                  | Socio-Economica |   NY.GDP.PCAP.KD  |
| poblacion que vive en barrios marginales (% de la poblacion urbana)                                                                 | Socio-Economica | EN.POP.SLUM.UR.ZS |
| Población Rural (% de la poblacion total)                                                                                           | Socio-Economica |   SP.RUR.TOTL.ZS  |
| poblacion urbana (%poblacion total)                                                                                                 | Socio-Economica | SP.URB.TOTL.IN.ZS |
| Research and development expenditure (% of GDP)                                                                                     | Socio-Economica | GB.XPD.RSDV.GD.ZS |
| Researchers in R&D (per million people)                                                                                             | Socio-Economica | SP.POP.SCIE.RD.P6 |
| tasa de recuento de la pobreza, multidimensional (%de la poblacion total)                                                           | Socio-Economica |    SI.POV.MDIM    |
| Trade in services (% of GDP)                                                                                                        | Socio-Economica | BG.GSR.NFSV.GD.ZS |
