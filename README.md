# BioLab: Análisis de Hipertensión Arterial

Repositorio del Trabajo Integrador Final de la asignatura **Bases de Datos**. Este proyecto se centra en la implementación y análisis de una base de datos para el estudio de la **hipertensión arterial** a partir de datos clínicos recolectados en el laboratorio BioLab.

## Descripción

El objetivo principal de este trabajo es desarrollar una base de datos relacional que permita almacenar, consultar y analizar información relacionada con la hipertensión arterial. Además, se busca aplicar técnicas avanzadas de modelado, consultas complejas y visualización de datos para ofrecer insights significativos sobre los factores asociados a esta condición.

### Características principales:

- **Modelado relacional**: Diseño de tablas con restricciones adecuadas (claves primarias, claves foráneas, unicidad, valores no nulos y verificaciones).
- **Datos ficticios**: Inserción de datos representativos provenientes de un laboratorio clínico simulado.
- **Consultas**: Creación de consultas SQL para responder preguntas de investigación específicas.
- **Valor agregado**: Análisis complementarios y visualización de datos mediante herramientas externas como Python y Qt Designer.

## Estructura del Repositorio
- `Herramientas generadoras`:
    - `generador_datos.py`:
    - 
- `SQL`:
    - `DATOS_PACIENTES.sql`
    - `TABLAS_PACIENTES.sql`
- `app.py`
- `graficas.py`: Colección de consultas avanzadas desarrolladas para el análisis de datos.
- `docs/`: Documentación técnica sobre el diseño de la base de datos, casos de uso y resultados.
- `README.md`: Este archivo.

## Requisitos

Para utilizar este proyecto, es necesario contar con las siguientes herramientas instaladas:

- [PostgreSQL](https://www.postgresql.org/) (versión 12 o superior).
- [DBeaver](https://dbeaver.io/) u otro cliente SQL para ejecutar los scripts.
- [Python](https://www.python.org/) (versión 3.8 o superior) con las siguientes librerías:
  - [matplotlib](https://matplotlib.org/): Para la generación de gráficos a partir de los datos analizados.
  - [pandas](https://pandas.pydata.org/): Para manipulación y análisis de datos.
- [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html): Para el diseño de interfaces gráficas que complementen el análisis.

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/usuario/BioLab.git
   cd BioLab
