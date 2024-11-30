import random

# Función para generar datos aleatorios para la tabla Paciente
def generar_datos_paciente(folio_id):
    sexo = random.choice(['M', 'F'])
    edad = random.randint(18, 80)
    peso = round(random.uniform(50, 100), 2)
    estatura = round(random.uniform(1.50, 1.90), 2)
    medida_cintura = round(random.uniform(60, 120), 2)
    segundamedicion_peso = round(peso + random.uniform(-3, 3), 2)
    segundamedicion_estatura = round(estatura + random.uniform(-0.03, 0.03), 2)
    segundamedicion_cintura = round(medida_cintura + random.uniform(-3, 3), 2)
    tension_arterial = f"{random.randint(110, 140)}/{random.randint(70, 90)}"
    sueno_horas = round(random.uniform(5, 9), 1)
    masa_corporal = round(peso / (estatura ** 2), 2)
    actividad_total = round(random.uniform(100, 200), 2)
    
    return (folio_id, sexo, edad, peso, estatura, medida_cintura, segundamedicion_peso, 
            segundamedicion_estatura, segundamedicion_cintura, tension_arterial, 
            sueno_horas, masa_corporal, actividad_total)

# Función para generar datos aleatorios para la tabla Examen_clinico
def generar_datos_examen_clinico(folio_id, examen_id):
    fecha_examen = f"{random.randint(2020, 2023)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
    temperatura_ambiente = round(random.uniform(20, 30), 1)
    riesgo_hipertension = random.choice([True, False])
    
    return (examen_id, folio_id, fecha_examen, temperatura_ambiente, riesgo_hipertension)

# Función para generar datos aleatorios para la tabla Prueba_sangre
def generar_datos_prueba_sangre(examen_id):
    concentracion_hemoglobina = round(random.uniform(12, 18), 2)
    valor_acido_urico = round(random.uniform(3.4, 7.0), 2)
    valor_albumina = round(random.uniform(3.5, 5.5), 2)
    valor_creatina = round(random.uniform(0.6, 1.3), 2)
    valor_glucosa = round(random.uniform(70, 110), 2)
    valor_insulina = round(random.uniform(2.6, 24.9), 2)
    valor_trigliceridos = round(random.uniform(50, 150), 2)
    valor_hemoglobina_glucosilada = round(random.uniform(4.0, 6.0), 2)
    
    return (examen_id, concentracion_hemoglobina, valor_acido_urico, valor_albumina, valor_creatina, 
            valor_glucosa, valor_insulina, valor_trigliceridos, valor_hemoglobina_glucosilada)

# Función para generar datos aleatorios para la tabla Perfil_lipidico
def generar_datos_perfil_lipidico(examen_id):
    colesterol_hdl = round(random.uniform(40, 60), 2)
    colesterol_ldl = round(random.uniform(70, 130), 2)
    colesterol_total = round(random.uniform(150, 200), 2)
    
    return (examen_id, colesterol_hdl, colesterol_ldl, colesterol_total)

# Función para generar datos aleatorios para la tabla Marcadores_nutricionales
def generar_datos_marcadores_nutricionales(examen_id):
    valor_ferritina = round(random.uniform(30, 300), 2)
    valor_folato = round(random.uniform(3.1, 17.5), 2)
    valor_vitamina_b12 = round(random.uniform(200, 900), 2)
    valor_vitamina_d = round(random.uniform(20, 50), 2)
    
    return (examen_id, valor_ferritina, valor_folato, valor_vitamina_b12, valor_vitamina_d)

# Función para generar datos aleatorios para la tabla Marcadores_inflamatorios
def generar_datos_marcadores_inflamatorios(examen_id):
    valor_proteinac_reactiva = round(random.uniform(0, 10), 2)
    valor_homocisteina = round(random.uniform(4, 15), 2)
    valor_transferrina = round(random.uniform(200, 360), 2)
    
    return (examen_id, valor_proteinac_reactiva, valor_homocisteina, valor_transferrina)

# Función para generar datos aleatorios para la tabla Mediciones_fisicas
def generar_datos_mediciones_fisicas(folio_id):
    distancia_rodilla_talon = round(random.uniform(30, 50), 2)
    circunferencia_pantorrilla = round(random.uniform(30, 45), 2)
    
    return (folio_id, distancia_rodilla_talon, circunferencia_pantorrilla)

# Crear el archivo SQL con los registros generados para todas las tablas
def generar_script_sql(filename, num_registros):
    with open(filename, 'w') as file:
        # Inserciones en la tabla Paciente
        file.write("-- Inserta registros en la tabla Paciente\n")
        file.write("INSERT INTO Paciente (folio_id, sexo, edad, peso, estatura, medida_cintura, "
                   "segundamedicion_peso, segundamedicion_estatura, segundamedicion_cintura, "
                   "tension_arterial, sueno_horas, masa_corporal, actividad_total) VALUES\n")
        
        for i in range(num_registros):
            paciente = generar_datos_paciente(str(1000 + i))
            file.write(f"('{paciente[0]}', '{paciente[1]}', {paciente[2]}, {paciente[3]}, {paciente[4]}, "
                       f"{paciente[5]}, {paciente[6]}, {paciente[7]}, {paciente[8]}, '{paciente[9]}', "
                       f"{paciente[10]}, {paciente[11]}, {paciente[12]})")
            file.write(",\n" if i < num_registros - 1 else ";\n")
        
        # Inserciones en la tabla Examen_clinico
        file.write("\n-- Inserta registros en la tabla Examen_clinico\n")
        file.write("INSERT INTO Examen_clinico (examen_id, folio_id, fecha_examen, "
                   "temperatura_ambiente, riesgo_hipertension) VALUES\n")
        
        for i in range(num_registros):
            examen = generar_datos_examen_clinico(str(1000 + i), i + 1)
            file.write(f"({examen[0]}, '{examen[1]}', '{examen[2]}', {examen[3]}, {examen[4]})")
            file.write(",\n" if i < num_registros - 1 else ";\n")
        
        # Inserciones en la tabla Prueba_sangre
        file.write("\n-- Inserta registros en la tabla Prueba_sangre\n")
        file.write("INSERT INTO Prueba_sangre (examen_id, concentracion_hemoglobina, valor_acido_urico, "
                   "valor_albumina, valor_creatina, valor_glucosa, valor_insulina, valor_trigliceridos, "
                   "valor_hemoglobina_glucosilada) VALUES\n")
        
        for i in range(num_registros):
            prueba = generar_datos_prueba_sangre(i + 1)
            file.write(f"({prueba[0]}, {prueba[1]}, {prueba[2]}, {prueba[3]}, {prueba[4]}, {prueba[5]}, "
                       f"{prueba[6]}, {prueba[7]}, {prueba[8]})")
            file.write(",\n" if i < num_registros - 1 else ";\n")
        
        # Inserciones en la tabla Perfil_lipidico
        file.write("\n-- Inserta registros en la tabla Perfil_lipidico\n")
        file.write("INSERT INTO Perfil_lipidico (examen_id, colesterol_hdl, colesterol_ldl, colesterol_total) VALUES\n")
        
        for i in range(num_registros):
            perfil = generar_datos_perfil_lipidico(i + 1)
            file.write(f"({perfil[0]}, {perfil[1]}, {perfil[2]}, {perfil[3]})")
            file.write(",\n" if i < num_registros - 1 else ";\n")
        
        # Inserciones en la tabla Marcadores_nutricionales
        file.write("\n-- Inserta registros en la tabla Marcadores_nutricionales\n")
        file.write("INSERT INTO Marcadores_nutricionales (examen_id, valor_ferritina, valor_folato, valor_vitamina_b12, valor_vitamina_d) VALUES\n")
        
        for i in range(num_registros):
            marcador_nutricional = generar_datos_marcadores_nutricionales(i + 1)
            file.write(f"({marcador_nutricional[0]}, {marcador_nutricional[1]}, {marcador_nutricional[2]}, "
                       f"{marcador_nutricional[3]}, {marcador_nutricional[4]})")
            file.write(",\n" if i < num_registros - 1 else ";\n")
        
        # Inserciones en la tabla Marcadores_inflamatorios
        file.write("\n-- Inserta registros en la tabla Marcadores_inflamatorios\n")
        file.write("INSERT INTO Marcadores_inflamatorios (examen_id, valor_proteinac_reactiva, valor_homocisteina, valor_transferrina) VALUES\n")
        
        for i in range(num_registros):
            marcador_inflamatorio = generar_datos_marcadores_inflamatorios(i + 1)
            file.write(f"({marcador_inflamatorio[0]}, {marcador_inflamatorio[1]}, {marcador_inflamatorio[2]}, {marcador_inflamatorio[3]})")
            file.write(",\n" if i < num_registros - 1 else ";\n")
        
        # Inserciones en la tabla Mediciones_fisicas
        file.write("\n-- Inserta registros en la tabla Mediciones_fisicas\n")
        file.write("INSERT INTO Mediciones_fisicas (folio_id, distancia_rodilla_talon, circunferencia_pantorrilla) VALUES\n")
        
        for i in range(num_registros):
            medicion = generar_datos_mediciones_fisicas(str(1000 + i))
            file.write(f"('{medicion[0]}', {medicion[1]}, {medicion[2]})")
            file.write(",\n" if i < num_registros - 1 else ";\n")

# Generar archivo SQL con datos de ejemplo
generar_script_sql('DATOS_PACIENTES.sql', 6000)
