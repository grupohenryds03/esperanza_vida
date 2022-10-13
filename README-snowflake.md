# Proyecto Final -Data 03- Soy Henry
## Jhovany Lara, Rodrigo Ruiz, Pablo Poletti ,José María Toledo

### Consigna: Desarrollo de un proyecto

- Para este proyecto final, se elegio la Esperanza de Vida al Nacer.


### Arquitectura (Ingesta data lake -> Armado Pipeline -> Ingesta data data warehouse)

- La arquitectura esta basada en el entorno de trabajo de snowflake, donde se ingestaran los datasets, se realiza el pipline del EDA, se trajara con modelos de ML y se visualizará en un dashboard de stremlit de acuerdo a los requerimientos del cliente.

<img src="/imagenes/engineering snowflake2.png" width="400" height="250"/>

- Para la ingesta de dataset se realizará un datalake, en un storage de S3 AWS con los archivos crudos en formato csv (tmb json, parquet , avro) comprimidos de la api del Banco Mundial y la Organización Mundial de la salud.

| archivo                              | external storage | tipo de compresión |
|--------------------------------------|------------------|--------------------|
| banco mundial.csv                    | AWS S3 bucket    | .gz                |
| organización mundial de la salud.csv | AWS S3 bucket    | .gz                |

- Luego de la ingesta de archivos se realiza un pipline para su EDA
- Para el armado del data warehouse se crean las tablas relacionales de hecho y dimensión con sus respectivos Id´s, primary keys y foreign key.

- tabla de hecho
| col    | tipo   | key | 
|--------|--------|-----|
| idPais | int    | PK  |
| pais   | string | -   |
| año    | int    | -   |
| var1   | float  | -   |
| ..     | ..     | -   |
| var37  | float  | -   |

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


- Para la creación del dashboard se utiliza streamlit. https://grupohenryds03-esperanza-vida-streamlitstreamlit-app-kni98s.streamlitapp.com/

- Para el deploy del dashboard se uttlizará la herramienta del deploy de streamlit

### Descripción de los pasos para el trabajo colaborativo sin container docker:

- Para relaizar el trabajo colaborativo , se establece la conexión desde visual studio code local

- en terminal se crea el entorno de trabajo:
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

| PAIS           | GNI PER CAPITA (SIMIL GDP PER CAPITA | ID WBGAPI | CONTINENTE |
|----------------|--------------------------------------|-----------|------------|
| USA            | H                                    | USA       | AMERICA    |
| CANADA         | H                                    | CAN       | AMERICA    |
| MEXICO         | M                                    | MEX       | AMERICA    |
| COSTA RICA     | M                                    | CRI       | AMERICA    |
| PANAMA         | H                                    | PAN       | AMERICA    |
| BRASIL         | M                                    | BRA       | AMERICA    |
| ARGENTINA      | M                                    | ARG       | AMERICA    |
| CHILE          | H                                    | CHL       | AMERICA    |
| URUGUAY        | H                                    | URY       | AMERICA    |
| BOLIVIA        | LM                                   | BOL       | AMERICA    |
| PERU           | M                                    | PER       | AMERICA    |
| EGIPTO         | LM                                   | EGY       | AFRICA     |
| LIBIA          | M                                    | LBY       | AFRICA     |
| SUDAFRICA      | M                                    | ZAF       | AFRICA     |
| NIGERIA        | LM                                   | NGA       | AFRICA     |
| MARRUECOS      | LM                                   | MAR       | AFRICA     |
| AUSTRALIA      | H                                    | AUS       | OCEANIA    |
| CHINA          | M                                    | CHN       | ASIA       |
| INDIA          | LM                                   | IND       | ASIA       |
| TAILANDIA      | M                                    | THA       | ASIA       |
| JAPON          | H                                    | JPN       | ASIA       |
| COREA DEL SUR  | H                                    | KOR       | ASIA       |
| ISRAEL         | H                                    | ISR       | ASIA       |
| ARABIA SAUDITA | H                                    | SAU       | ASIA       |
| MALASIA        | M                                    | MYS       | ASIA       |
| INDONESIA      | LM                                   | IDN       | ASIA       |
| RUSIA          | M                                    | RUS       | EUROPA     |
| TURQUIA        | M                                    | TUR       | EUROPA     |
| ESPAÑA         | H                                    | ESP       | EUROPA     |
| BULGARIA       | M                                    | BGR       | EUROPA     |
| FRANCIA        | H                                    | FRA       | EUROPA     |
| ITALIA         | H                                    | ITA       | EUROPA     |
| ALEMANIA       | H                                    | DEU       | EUROPA     |
| INGLATERRA     | H                                    | GBR       | EUROPA     |
| NORUEGA        | H                                    | NOR       | EUROPA     |
| SUECIA         | H                                    | SWE       | EUROPA     |
| GRECIA         | H                                    | GRC       | EUROPA     |

