-- Tabla: Paciente
CREATE TABLE Paciente (
    folio_id VARCHAR(15) PRIMARY KEY, -- Identificador único del paciente
    sexo VARCHAR(10) NOT NULL CHECK (sexo IN ('Masculino', 'Femenino')), -- Restricción para sexo
    edad INTEGER NOT NULL CHECK (edad >= 0), -- Restricción: edad no negativa
    peso NUMERIC(5,2) NOT NULL CHECK (peso >= 0), -- Restricción: peso no negativo
    estatura NUMERIC(5,2) NOT NULL CHECK (estatura >= 0), -- Restricción: estatura no negativa
    medida_cintura NUMERIC(5,2) NOT NULL CHECK (medida_cintura >= 0), -- Restricción: medida de cintura no negativa
    segundamedicion_peso NUMERIC(5,2) CHECK (segundamedicion_peso >= 0), -- Restricción opcional
    segundamedicion_estatura NUMERIC(5,2) CHECK (segundamedicion_estatura >= 0), -- Restricción opcional
    segundamedicion_cintura NUMERIC(5,2) CHECK (segundamedicion_cintura >= 0), -- Restricción opcional
    tension_arterial VARCHAR(15), -- Medición de la presión arterial
    sueno_horas NUMERIC(3,1) CHECK (sueno_horas >= 0), -- Restricción: horas de sueño no negativas
    masa_corporal NUMERIC(5,2), -- Índice de masa corporal
    actividad_total NUMERIC(5,2) CHECK (actividad_total >= 0) -- Restricción: actividad física no negativa
);

-- Tabla: Examen_clinico
CREATE TABLE Examen_clinico (
    examen_id SERIAL PRIMARY KEY, -- Identificador único del examen clínico
    folio_id VARCHAR(15) NOT NULL REFERENCES Paciente(folio_id) ON DELETE CASCADE, -- Relación con Paciente
    fecha_examen DATE NOT NULL, -- Fecha del examen
    temperatura_ambiente NUMERIC(4,1), -- Temperatura ambiental (opcional)
    riesgo_hipertension BOOLEAN DEFAULT false -- Por defecto, sin riesgo de hipertensión
);

-- Tabla: Prueba_sangre
CREATE TABLE Prueba_sangre (
    prueba_id SERIAL PRIMARY KEY, -- Identificador único de la prueba de sangre
    examen_id INT NOT NULL REFERENCES Examen_clinico(examen_id) ON DELETE CASCADE, -- Relación con Examen_clinico
    concentracion_hemoglobina NUMERIC(5,2) NOT NULL CHECK (concentracion_hemoglobina >= 0), -- Restricción: no negativa
    valor_acido_urico NUMERIC(5,2) NOT NULL CHECK (valor_acido_urico >= 0),
    valor_albumina NUMERIC(5,2) NOT NULL CHECK (valor_albumina >= 0),
    valor_creatina NUMERIC(5,2) NOT NULL CHECK (valor_creatina >= 0),
    valor_glucosa NUMERIC(5,2) NOT NULL CHECK (valor_glucosa >= 0),
    valor_insulina NUMERIC(5,2) NOT NULL CHECK (valor_insulina >= 0),
    valor_trigliceridos NUMERIC(5,2) NOT NULL CHECK (valor_trigliceridos >= 0),
    valor_hemoglobina_glucosilada NUMERIC(5,2) NOT NULL CHECK (valor_hemoglobina_glucosilada >= 0)
);

-- Tabla: Perfil_lipidico
CREATE TABLE Perfil_lipidico (
    perfil_id SERIAL PRIMARY KEY, -- Identificador único del perfil lipídico
    examen_id INT NOT NULL REFERENCES Examen_clinico(examen_id) ON DELETE CASCADE, -- Relación con Examen_clinico
    colesterol_hdl NUMERIC(5,2) NOT NULL CHECK (colesterol_hdl >= 0),
    colesterol_ldl NUMERIC(5,2) NOT NULL CHECK (colesterol_ldl >= 0),
    colesterol_total NUMERIC(5,2) NOT NULL CHECK (colesterol_total >= 0)
);

-- Tabla: Marcadores_nutricionales
CREATE TABLE Marcadores_nutricionales (
    marcador_id SERIAL PRIMARY KEY, -- Identificador único de los marcadores nutricionales
    examen_id INT NOT NULL REFERENCES Examen_clinico(examen_id) ON DELETE CASCADE, -- Relación con Examen_clinico
    valor_ferritina NUMERIC(5,2) NOT NULL CHECK (valor_ferritina >= 0),
    valor_folato NUMERIC(5,2) NOT NULL CHECK (valor_folato >= 0),
    valor_vitamina_b12 NUMERIC(5,2) NOT NULL CHECK (valor_vitamina_b12 >= 0),
    valor_vitamina_d NUMERIC(5,2) NOT NULL CHECK (valor_vitamina_d >= 0)
);

-- Tabla: Marcadores_inflamatorios
CREATE TABLE Marcadores_inflamatorios (
    marcador_inflam_id SERIAL PRIMARY KEY, -- Identificador único del marcador inflamatorio
    examen_id INT NOT NULL REFERENCES Examen_clinico(examen_id) ON DELETE CASCADE, -- Relación con Examen_clinico
    valor_proteinac_reactiva NUMERIC(5,2), -- Opcional
    valor_homocisteina NUMERIC(5,2), -- Opcional
    valor_transferrina NUMERIC(5,2) -- Opcional
);

-- Tabla: Mediciones_fisicas
CREATE TABLE Mediciones_fisicas (
    medicion_id SERIAL PRIMARY KEY, -- Identificador único de la medición física
    folio_id VARCHAR(15) NOT NULL REFERENCES Paciente(folio_id) ON DELETE CASCADE, -- Relación con Paciente
    distancia_rodilla_talon NUMERIC(5,2), -- Opcional
    circunferencia_pantorrilla NUMERIC(5,2) -- Opcional
);
