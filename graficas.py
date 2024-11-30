import psycopg2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuración de la base de datos
DB_CONFIG = {
    'dbname': 'BioLab',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5432'
}

def create_connection():
    return psycopg2.connect(**DB_CONFIG)

# 1. Distribución de IMC

def plot_bmi_distribution(ax):
    connection = create_connection()
    query = """
    SELECT masa_corporal AS bmi
    FROM Paciente
    WHERE masa_corporal IS NOT NULL
    """
    data = pd.read_sql_query(query, connection)
    connection.close()

    sns.histplot(data=data, x='bmi', kde=True, color="purple", bins=30, ax=ax)
    ax.set_title("Distribución de IMC")
    ax.set_xlabel("IMC")
    ax.set_ylabel("Frecuencia")

# 2. Relación entre horas de sueño y riesgo de hipertensión

def plot_sleep_vs_hypertension(ax):
    connection = create_connection()
    query = """
    SELECT sueno_horas, riesgo_hipertension
    FROM Paciente p
    JOIN Examen_clinico ec ON p.folio_id = ec.folio_id
    """
    data = pd.read_sql_query(query, connection)
    connection.close()

    sns.boxplot(data=data, x='riesgo_hipertension', y='sueno_horas', palette="Set2", ax=ax)
    ax.set_title('Horas de Sueño vs Riesgo de Hipertensión', fontsize=12)
    ax.set_xlabel('Riesgo de Hipertensión')
    ax.set_ylabel('Horas de Sueño')

# 3. Promedio de colesterol total por género

def plot_avg_total_cholesterol_by_gender(ax):
    connection = create_connection()
    query = """
    SELECT sexo, AVG(colesterol_total) AS colesterol_promedio
    FROM Paciente p
    JOIN Examen_clinico ec ON p.folio_id = ec.folio_id
    JOIN Perfil_lipidico pl ON ec.examen_id = pl.examen_id
    GROUP BY sexo
    """
    data = pd.read_sql_query(query, connection)
    connection.close()

    sns.barplot(data=data, x='sexo', y='colesterol_promedio', palette="Blues", ax=ax)
    ax.set_title('Promedio de Colesterol Total por Género', fontsize=12)
    ax.set_xlabel('Género')
    ax.set_ylabel('Colesterol Total Promedio (mg/dL)')

# 4. Distribución de triglicéridos

def plot_triglyceride_distribution(ax):
    connection = create_connection()
    query = """
    SELECT valor_trigliceridos AS trigliceridos
    FROM Prueba_sangre
    WHERE valor_trigliceridos IS NOT NULL
    """
    data = pd.read_sql_query(query, connection)
    connection.close()

    sns.histplot(data=data, x='trigliceridos', kde=True, color="orange", bins=30, ax=ax)
    ax.set_title('Distribución de Triglicéridos', fontsize=14)
    ax.set_xlabel('Triglicéridos (mg/dL)')
    ax.set_ylabel('Frecuencia')




# 6. Riesgo de hipertensión y colesterol total por rango de edad

def plot_hypertension_and_cholesterol_by_age(ax):
    connection = create_connection()
    query = """
    SELECT 
        CASE 
            WHEN edad BETWEEN 0 AND 10 THEN '0-10'
            WHEN edad BETWEEN 11 AND 20 THEN '11-20'
            WHEN edad BETWEEN 21 AND 30 THEN '21-30'
            WHEN edad BETWEEN 31 AND 40 THEN '31-40'
            WHEN edad BETWEEN 41 AND 50 THEN '41-50'
            ELSE '50+' 
        END AS rango_edad,
        AVG(riesgo_hipertension::INT) AS riesgo_promedio,
        AVG(colesterol_total) AS colesterol_promedio
    FROM Paciente p
    JOIN Examen_clinico ec ON p.folio_id = ec.folio_id
    JOIN Perfil_lipidico pl ON ec.examen_id = pl.examen_id
    GROUP BY rango_edad
    ORDER BY rango_edad
    """
    data = pd.read_sql_query(query, connection)
    connection.close()

    # Crear dos ejes superpuestos
    ax2 = ax.twinx()
    sns.barplot(data=data, x='rango_edad', y='riesgo_promedio', ax=ax, color='lightcoral', alpha=0.7)
    sns.lineplot(data=data, x='rango_edad', y='colesterol_promedio', ax=ax2, marker='o', color='blue')

    ax.set_ylabel('Riesgo Promedio de Hipertensión', color='red')
    ax2.set_ylabel('Colesterol Total Promedio (mg/dL)', color='blue')
    ax.set_xlabel('Rango de Edad')
    ax.set_title('Riesgo de Hipertensión y Colesterol por Rango de Edad', fontsize=14)

