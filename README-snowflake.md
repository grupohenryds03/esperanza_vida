# Proyecto Final -Data 03- Soy Henry
## Jhovany Lara, Rodrigo Ruiz, Pablo Poletti ,José María Toledo

### Consigna: Desarrollo de un proyecto

- Para este proyecto final, se elegio la Esperanza de Vida al Nacer.


### Ejecución

- Para la ingesta de dataset se realizará un data warehouse con base de datos relacional en snowflake, con almacenamiento el cloud de AWS. 
- Para la creación del dashboard se utiliza streamlit. https://grupohenryds03-esperanza-vida-streamlitstreamlit-app-kni98s.streamlitapp.com/
- Para el deploy del dashboard se utuliza la herramienta del deply de streamlit.
- Para relaizar el trabajo colaborativo , se establece la conexión desde visual studio code local (en revison- mediante un container en Docker con databrick-conection).

<img src="/imagenes/engineering snowflake2.png" width="400" height="250"/>



### Descripción de los pasos para el trabajo colaborativo sin container docker:

1. en terminal se crea el entorno de trabajo:
- descargar conda
- creacion del entorno: conda create -n dbconnect python=3.8.12 # pse crea el entorno para realizar la conexión en visual studio code con phyton y snowflake (dbconnect es el nombre del entorno), no cambiar la versión ya que puede generar problema con el conector de snowflake
- activar el entorno: conda activate dbconnect
- instalar el conector con snowflake: pip install snowflake-connector-python[pandas] # no cambiar la versión ya que puede generar problema con la versión de phyton instalada para el entorno en cuestión
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

### Descripción de los pasos para el trabajo colaborativo con container docker:

1. conar este repo: git clone https://github.com/grupohenryds03/esperanza_vida

dentro de la carpeta container:

- *.devcontainer*->carpepeta para realizar el container en Visual Studio Code (VSC)

- *Dockerfile*-> archivo docker para la cracion del container

- *.databricks-connect.template* ->archivo con datos en formato .json para la conección con databricks

- *devcontainer.json*->archivo .json con especificaciones del entorno para la conexión 

- para la creacion del container en VSC, se va a From Remote-Containers: Reopen in Container y se eleje la carpeta *.devcontainer*


### Documentación Paises elegidos

- Se selecciono una muestra de países teniendo en cuenta incluir estados de los 5 continentes que sean representativos, tengan buena calidad en la información histórica recolectada por el World Bank para la confección de sus indicadores.
-  Inicialmente se utilizó como filtro para diferenciar la muestra por continentes, el status de países “desarrollados” vs “en desarrollo”, pero tomando en cuenta la clasificación que realiza las naciones unidas se observo que tanto en América Latina, África como en Medio Oriente, se necesitaba incluir otro nivel de clasificación para mejorar la diferenciación; por lo cual se decidió utilizar la clasificación por nivel de ingresos que realiza el World Bank mediante el “GNI (Ingreso Bruto Nacional)  per cápita” y así poder mejorar la diferenciación de los efectos de las diferentes variables sobre la esperanza de vida, según el país o continente en estudio.


|      PAIS      | GNI PER CAPITA (SIMIL GDP PER CAPITA | ID WBGAPI | CONTINENTE |
|:--------------:|:------------------------------------:|:---------:|:----------:|
| USA            |                   H                  |    USA    |   AMERICA  |
| CANADA         |                   H                  |    CAN    |            |
| MEXICO         |                   M                  |    MEX    |            |
| COSTA RICA     |                   M                  |    CRI    |            |
| PANAMA         |                   H                  |    PAN    |            |
| BRASIL         |                   M                  |    BRA    |            |
| ARGENTINA      |                   M                  |    ARG    |            |
| CHILE          |                   H                  |    CHL    |            |
| URUGUAY        |                   H                  |    URY    |            |
| BOLIVIA        |                  LM                  |    BOL    |            |
| PERU           |                   M                  |    PER    |            |
| EGIPTO         |                  LM                  |    EGY    |   AFRICA   |
| LIBIA          |                   M                  |    LBY    |            |
| SUDAFRICA      |                   M                  |    ZAF    |            |
| NIGERIA        |                  LM                  |    NGA    |            |
| MARRUECOS      |                  LM                  |    MAR    |            |
| AUSTRALIA      |                   H                  |    AUS    |   OCEANIA  |
| CHINA          |                   M                  |    CHN    |    ASIA    |
| INDIA          |                  LM                  |    IND    |            |
| TAILANDIA      |                   M                  |    THA    |            |
| JAPON          |                   H                  |    JPN    |            |
| COREA DEL SUR  |                   H                  |    KOR    |            |
| ISRAEL         |                   H                  |    ISR    |            |
| ARABIA SAUDITA |                   H                  |    SAU    |            |
| MALASIA        |                   M                  |    MYS    |            |
| INDONESIA      |                  LM                  |    IDN    |            |
| RUSIA          |                   M                  |    RUS    |   EUROPA   |
| TURQUIA        |                   M                  |    TUR    |            |
| ESPAÑA         |                   H                  |    ESP    |            |
| BULGARIA       |                   M                  |    BGR    |            |
| FRANCIA        |                   H                  |    FRA    |            |
| ITALIA         |                   H                  |    ITA    |            |
| ALEMANIA       |                   H                  |    DEU    |            |
| INGLATERRA     |                   H                  |    GBR    |            |
| NORUEGA        |                   H                  |    NOR    |            |
| SUECIA         |                   H                  |    SWE    |            |
| GRECIA         |                   H                  |    GRC    |            |


