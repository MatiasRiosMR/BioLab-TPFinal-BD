-- Creación de la tabla Paciente
CREATE TABLE Paciente (
    folio_id VARCHAR(15) PRIMARY KEY,
    sexo VARCHAR(10),
    edad INTEGER,
    peso NUMERIC(5,2),
    estatura NUMERIC(5,2),
    medida_cintura NUMERIC(5,2),
    segundamedicion_peso NUMERIC(5,2),
    segundamedicion_estatura NUMERIC(5,2),
    segundamedicion_cintura NUMERIC(5,2),
    tension_arterial VARCHAR(15),
    sueno_horas NUMERIC(3,1),
    masa_corporal NUMERIC(5,2),
    actividad_total NUMERIC(5,2)
);

-- Creación de la tabla Examen_clínico
CREATE TABLE Examen_clinico (
    examen_id SERIAL PRIMARY KEY,
    folio_id VARCHAR(15) REFERENCES Paciente(folio_id) ON DELETE CASCADE,
    fecha_examen DATE,
    temperatura_ambiente NUMERIC(4,1),
    riesgo_hipertension BOOLEAN
);

-- Creación de la tabla Prueba_sangre
CREATE TABLE Prueba_sangre (
    prueba_id SERIAL PRIMARY KEY,
    examen_id INT REFERENCES Examen_clinico(examen_id) ON DELETE CASCADE,
    concentracion_hemoglobina NUMERIC(5,2),
    valor_acido_urico NUMERIC(5,2),
    valor_albumina NUMERIC(5,2),
    valor_creatina NUMERIC(5,2),
    valor_glucosa NUMERIC(5,2),
    valor_insulina NUMERIC(5,2),
    valor_trigliceridos NUMERIC(5,2),
    valor_hemoglobina_glucosilada NUMERIC(5,2)
);

-- Creación de la tabla Perfil_lipidico
CREATE TABLE Perfil_lipidico (
    perfil_id SERIAL PRIMARY KEY,
    examen_id INT REFERENCES Examen_clinico(examen_id) ON DELETE CASCADE,
    colesterol_hdl NUMERIC(5,2),
    colesterol_ldl NUMERIC(5,2),
    colesterol_total NUMERIC(5,2)
);

-- Creación de la tabla Marcadores_nutricionales
CREATE TABLE Marcadores_nutricionales (
    marcador_id SERIAL PRIMARY KEY,
    examen_id INT REFERENCES Examen_clinico(examen_id) ON DELETE CASCADE,
    valor_ferritina NUMERIC(5,2),
    valor_folato NUMERIC(5,2),
    valor_vitamina_b12 NUMERIC(5,2),
    valor_vitamina_d NUMERIC(5,2)
);

-- Creación de la tabla Marcadores_inflamatorios
CREATE TABLE Marcadores_inflamatorios (
    marcador_inflam_id SERIAL PRIMARY KEY,
    examen_id INT REFERENCES Examen_clinico(examen_id) ON DELETE CASCADE,
    valor_proteinac_reactiva NUMERIC(5,2),
    valor_homocisteina NUMERIC(5,2),
    valor_transferrina NUMERIC(5,2)
);

-- Creación de la tabla Mediciones_fisicas
CREATE TABLE Mediciones_fisicas (
    medicion_id SERIAL PRIMARY KEY,
    folio_id VARCHAR(15) REFERENCES Paciente(folio_id) ON DELETE CASCADE,
    distancia_rodilla_talon NUMERIC(5,2),
    circunferencia_pantorrilla NUMERIC(5,2)
);
