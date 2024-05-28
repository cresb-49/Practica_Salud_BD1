CREATE TABLE genero (
    id_genero INTEGER PRIMARY KEY NOT NULL,
    genero TEXT NOT NULL UNIQUE
);

CREATE TABLE departamento (
    id_departamento TEXT PRIMARY KEY NOT NULL,
    departamento TEXT NOT NULL UNIQUE    
);

CREATE TABLE municipio (
    id_municipio TEXT PRIMARY KEY NOT NULL,
    municipio TEXT NOT NULL,
    id_departamento TEXT NOT NULL,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento)
);

CREATE TABLE tipo_consulta (
    id_tipo_consulta INTEGER PRIMARY KEY NOT NULL,
    tipo_consulta TEXT NOT NULL UNIQUE    
);

CREATE TABLE enfermedades (
    codigo_cie TEXT PRIMARY KEY NOT NULL,
    descripcion TEXT NOT NULL,
    codigo_cie_padre TEXT,
    FOREIGN KEY (codigo_cie_padre) REFERENCES enfermedades(codigo_cie)    
);

CREATE TABLE condicion_egreso (
    id_condicion_egreso INTEGER PRIMARY KEY NOT NULL,
    condicion_egreso TEXT NOT NULL UNIQUE    
);

CREATE TABLE tratamiento (
    id_tratamiento INTEGER PRIMARY KEY NOT NULL,
    tratamiento TEXT NOT NULL UNIQUE    
);

CREATE TABLE tipo_servicios (
    id_tipo_servicios INTEGER PRIMARY KEY NOT NULL,
    tipo_servicios TEXT NOT NULL UNIQUE
);

CREATE TABLE atencion_por_rango_edad (
    id INTEGER PRIMARY KEY NOT NULL,
    lim_inf_rango INTEGER,
    lim_sup_rango INTEGER CHECK (lim_inf_rango < lim_sup_rango),
    id_codigo_cie TEXT NOT NULL,
    hombres INTEGER DEFAULT 0,
    mujeres INTEGER DEFAULT 0,
    ignorado INTEGER DEFAULT 0,
    id_tipo_servicio INTEGER NOT NULL,
    FOREIGN KEY (id_codigo_cie) REFERENCES enfermedades(codigo_cie),
    FOREIGN KEY (id_tipo_servicio) REFERENCES tipo_servicios(id_tipo_servicios)
);


CREATE TABLE atencion_por_departamento (
    id_atencion_por_departamento INTEGER PRIMARY KEY NOT NULL,
    id_departamento TEXT,
    codigo_cie TEXT NOT NULL,
    hombres INTEGER,
    mujeres INTEGER,
    ignorado INTEGER,
    id_tipo_servicios INTEGER NOT NULL ,
    FOREIGN KEY (id_tipo_servicios) REFERENCES tipo_servicios(id_tipo_servicios),
    FOREIGN KEY (codigo_cie) REFERENCES enfermedades(codigo_cie),
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento)
);

CREATE TABLE atencion_por_tipo_consulta (
    id_atencion_por_tipo_consulta INTEGER PRIMARY KEY NOT NULL,
    lim_inf_rango INTEGER,
    lim_sup_rango INTEGER,
    id_sexo INTEGER NOT NULL REFERENCES sexo(id_sexo),
    id_tipo_consulta INTEGER NOT NULL REFERENCES tipo_consulta(id_tipo_consulta),
    total INTEGER
);