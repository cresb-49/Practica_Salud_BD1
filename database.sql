CREATE DATABASE IF NOT EXISTS salud_guatemala;
USE salud_guatemala;

-- DROP TABLE IF EXISTS genero;
CREATE TABLE IF NOT EXISTS genero(
    id_genero INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    genero VARCHAR(20) NOT NULL UNIQUE
);

-- DROP TABLE IF EXISTS departamento;
CREATE TABLE IF NOT EXISTS departamento(
    id_departamento VARCHAR(2) PRIMARY KEY NOT NULL,
    departamento VARCHAR(100) NOT NULL UNIQUE
);

-- DROP TABLE IF EXISTS municipio;
CREATE TABLE IF NOT EXISTS municipio(
    id_municipio VARCHAR(4) PRIMARY KEY NOT NULL,
    municipio VARCHAR(100) NOT NULL,
    id_departamento VARCHAR(2) NOT NULL,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento)
);

-- DROP TABLE IF EXISTS tipo_consulta;
CREATE TABLE IF NOT EXISTS tipo_consulta(
    id_tipo_consulta INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    tipo_consulta VARCHAR(100) NOT NULL UNIQUE
);

-- DROP TABLE IF EXISTS enfermedades;
CREATE TABLE IF NOT EXISTS enfermedades(
    codigo_cie VARCHAR(10) PRIMARY KEY NOT NULL,
    descripcion TEXT NOT NULL,
    codigo_cie_padre VARCHAR(10),
    FOREIGN KEY (codigo_cie_padre) REFERENCES enfermedades(codigo_cie)
);

-- DROP TABLE IF EXISTS condicion_egreso;
CREATE TABLE IF NOT EXISTS condicion_egreso(
    id_condicion_egreso INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    condicion_egreso VARCHAR(100) NOT NULL UNIQUE
);

-- DROP TABLE IF EXISTS tratamiento;
CREATE TABLE IF NOT EXISTS tratamiento(
    id_tratamiento INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    tratamiento VARCHAR(100) NOT NULL UNIQUE
);

-- DROP TABLE IF EXISTS tipo_servicio;
CREATE TABLE IF NOT EXISTS tipo_servicio(
    id_tipo_servicio INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    tipo_servicio VARCHAR(100) NOT NULL UNIQUE
);

-- DROP TABLE IF EXISTS rangos_edad;
CREATE TABLE IF NOT EXISTS rangos_edad(
    id_rango_edad INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    lim_inf_rango INT,
    lim_sup_rango INT CHECK (lim_inf_rango < lim_sup_rango)
);

-- DROP TABLE IF EXISTS atencion_por_rango_edad;
CREATE TABLE IF NOT EXISTS atencion_por_rango_edad(
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    id_rango_edad INT NOT NULL,
    id_codigo_cie VARCHAR(10) NOT NULL,
    id_tipo_servicio INT NOT NULL,
    FOREIGN KEY (id_codigo_cie) REFERENCES enfermedades(codigo_cie),
    FOREIGN KEY (id_tipo_servicio) REFERENCES tipo_servicio(id_tipo_servicio)
);

-- DROP TABLE IF EXISTS valor_atencion_por_rango_edad;
CREATE TABLE IF NOT EXISTS valor_atencion_por_rango_edad(
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    id_atencion_por_rango_edad INT NOT NULL,
    id_genero INT NOT NULL,
    valor INT NOT NULL,
    FOREIGN KEY (id_genero) REFERENCES genero(id_genero),
    FOREIGN KEY (id_atencion_por_rango_edad) REFERENCES atención_por_rango_edad(id)
);

-- DROP TABLE IF EXISTS atencion_por_departamento;
CREATE TABLE IF NOT EXISTS atencion_por_departamento(
    id_atencion_por_departamento INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    id_departamento VARCHAR(2) NOT NULL,
    codigo_cie VARCHAR(10) NOT NULL,
    id_tipo_servicio INT NOT NULL,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento),
    FOREIGN KEY (codigo_cie) REFERENCES enfermedades(codigo_cie),
    FOREIGN KEY (id_tipo_servicio) REFERENCES tipo_servicio(id_tipo_servicio)
);

-- DROP TABLE IF EXISTS valor_atencion_por_departamento;
CREATE TABLE IF NOT EXISTS valor_atencion_por_departamento(
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    id_atencion_por_departamento INT NOT NULL,
    id_genero INT NOT NULL,
    valor INT NOT NULL,
    FOREIGN KEY (id_genero) REFERENCES genero(id_genero),
    FOREIGN KEY (id_atencion_por_departamento) REFERENCES atencion_por_departamento(id_atencion_por_departamento)
);

-- DROP TABLE IF EXISTS atencion_por_municipio;
CREATE TABLE IF NOT EXISTS atencion_por_tipo_consulta(
    id_atencion_por_tipo_consulta INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    id_rango_edad INT NOT NULL,
    id_genero INT NOT NULL,
    id_tipo_consulta INT NOT NULL,
    total_atenciones INT NOT NULL,
    FOREIGN KEY (id_rango_edad) REFERENCES rangos_edad(id_rango_edad),
    FOREIGN KEY (id_genero) REFERENCES genero(id_genero),
    FOREIGN KEY (id_tipo_consulta) REFERENCES tipo_consulta(id_tipo_consulta)
);

CREATE TABLE IF NOT EXISTS condicion_egreso_segun_sexo(
    id_condicion_egreso_segun_sexo INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    id_genero INT NOT NULL,
    id_condicion_egreso INT NOT NULL,
    total INT NOT NULL,
    FOREIGN KEY (id_genero) REFERENCES genero(id_genero),
    FOREIGN KEY (id_condicion_egreso) REFERENCES condicion_egreso(id_condicion_egreso)
);

CREATE TABLE IF NOT EXISTS tratamiento_servicios_internos(
    id_tratamiento_servicios_internos INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    id_genero INT NOT NULL,
    id_tratamiento INT NOT NULL,
    total INT NOT NULL,
    FOREIGN KEY (id_genero) REFERENCES genero(id_genero),
    FOREIGN KEY (id_tratamiento) REFERENCES tratamiento(id_tratamiento)
);

CREATE TABLE IF NOT EXISTS promedio_estancia_egresados(
    id_promedio_estancia_egresados INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    id_departamento VARCHAR(2) NOT NULL,
    total_egresados INT NOT NULL,
    promedio_estancia INT NOT NULL,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento)
);

CREATE TABLE IF NOT EXISTS numero_dosis(
    id_numero_dosis INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    numero_dosis VARCHAR(5) NOT NULL UNIQUE,
    descripcion VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS vacuna(
    id_vacuna INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    vacuna VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS area_salud(
    id_area_salud INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    area_salud VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS atencion_por_vacuna(
    id_atencion_por_vacuna INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    anio INT NOT NULL,
    id_area_salud INT NOT NULL,
    id_departamento VARCHAR(2) NOT NULL,
    id_municipio VARCHAR(4) NOT NULL,
    edad INT NOT NULL,
    id_vacuna INT NOT NULL,
    id_numero_dosis INT NOT NULL,
    n_vacunados INT NOT NULL,
    poblacion INT NOT NULL,
    FOREIGN KEY (id_area_salud) REFERENCES area_salud(id_area_salud),
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento),
    FOREIGN KEY (id_municipio) REFERENCES municipio(id_municipio),
    FOREIGN KEY (id_vacuna) REFERENCES vacuna(id_vacuna),
    FOREIGN KEY (id_numero_dosis) REFERENCES numero_dosis(id_numero_dosis)
);

CREATE TABLE IF NOT EXISTS atencion_por_vacuna_vph(
    id_atencion_por_vacuna_vph INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    anio INT NOT NULL,
    id_area_salud INT NOT NULL,
    id_departamento VARCHAR(2) NOT NULL,
    id_municipio VARCHAR(4) NOT NULL,
    id_numero_dosis INT NOT NULL,
    id_genero INT NOT NULL,
    n_vacunados INT NOT NULL,
    poblacion INT NOT NULL,
    FOREIGN KEY (id_area_salud) REFERENCES area_salud(id_area_salud),
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento),
    FOREIGN KEY (id_municipio) REFERENCES municipio(id_municipio),
    FOREIGN KEY (id_numero_dosis) REFERENCES numero_dosis(id_numero_dosis),
    FOREIGN KEY (id_genero) REFERENCES genero(id_genero)
);