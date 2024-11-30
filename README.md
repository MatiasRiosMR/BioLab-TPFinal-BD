# BioLab: Análisis de Hipertensión Arterial
---
**Estudiante:** Rios Matias

**Carrera:** Licenciatura en Bioinformática 

**Institución:** Facultad de Ingenieria UNER 

---




Repositorio del Trabajo Integrador Final de la asignatura **Bases de Datos**. Este proyecto se centra en la implementación y análisis de una base de datos para el estudio de la **hipertensión arterial** a partir de datos clínicos recolectados en el laboratorio BioLab.

## Descripción

El objetivo principal de este trabajo es desarrollar una base de datos relacional que permita almacenar, consultar y analizar información relacionada con la hipertensión arterial. Además, se busca aplicar técnicas avanzadas de modelado, consultas complejas y visualización de datos para ofrecer insights significativos sobre los factores asociados a esta condición.

### Características principales:

- **Modelado relacional**: Diseño de tablas con restricciones adecuadas (claves primarias, claves foráneas, unicidad, valores no nulos y verificaciones).
- **Datos ficticios**: Inserción de datos representativos provenientes de un laboratorio clínico simulado.
- **Consultas**: Creación de consultas SQL para responder preguntas de investigación específicas.
- **Valor agregado**: Análisis complementarios y visualización de datos mediante herramientas externas como Python y Qt Designer.

## Estructura del Repositorio
- `scripts_utiles/`: Contiene scripts auxiliares para la generación de datos y otras tareas relacionadas
    - `generador_datos.py`: Script para generar datos de prueba que se insertan en la base de datos.
- `scripts_SQL/`:
    - `DATOS_PACIENTES.sql`: Contiene las instrucciones para insertar los datos iniciales en las tablas de la base de datos. 
    - `TABLAS_PACIENTES.sql`: Contiene las instrucciones para crear las tablas principales de la base de datos.
- `app.py`: Aplicación principal desarrollada con PyQt para la interacción con la base de datos, permitiendo realizar consultas y gestionar los datos relacionados con pacientes y exámenes.
- `graficas.py`: Contiene una colección de consultas avanzadas y generación de gráficos para el análisis de datos. Útil para visualizar resultados clave obtenidos de la base de datos. 
- `docs/`: Documentación técnica sobre el diseño de la base de datos, casos de uso y resultados.
  - `Informe_RiosMatias-BD.pdf`: Informe del trabajo realizado con desarrollo, resultados y conclusiones.
  - `Slides_RiosMatias_TPF-BD.pdf`: Diapositivas realizadas para la exposición,
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
   git clone https://github.com/MatiasRiosMR/BioLab-TPFinal-BD
   cd BioLab
   
2. Preparar el entorno: Asegúrate de tener instalado Python, PyQt, y un gestor de bases de datos compatible (MySQL, PostgreSQL, etc.).

3. Crear la base de datos:
    - Ejecuta primero `TABLAS_PACIENTES.sql` para crear la estructura de las tablas.
    - Luego, ejecuta `DATOS_PACIENTES.sql` para insertar los datos iniciales.

4. Ejecutar la aplicación: Usa `app.py`: para interactuar con la base de datos y realizar consultas o análisis.
