USE portal_db;

/* JSON API CHILE https://apis.digital.gob.cl/dpa/regiones */
CREATE TABLE region (
  id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  nombre VARCHAR(50) ,
  latitude  DECIMAL(9, 6),
  longitude DECIMAL(9, 6)
);

/* JSON API CHILE https://apis.digital.gob.cl/dpa/provincias */
CREATE TABLE provincia (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50),
  latitude DECIMAL(9, 6),
  longitude DECIMAL(9, 6),
  region_id INT,
  FOREIGN KEY (region_id) REFERENCES region(id)  
);

/* JSON API CHILE https://apis.digital.gob.cl/dpa/comunas */
CREATE TABLE comuna (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50),
  latitude DECIMAL(9, 6),
  longitude DECIMAL(9, 6),
  provincia_id INT,
  FOREIGN KEY (provincia_id) REFERENCES provincia(id) 
);

CREATE TABLE persona ( 
  id INT AUTO_INCREMENT PRIMARY KEY,
  rut VARCHAR (13),
  nombre VARCHAR(150),
  edad INT,
  genero VARCHAR (50)
);

CREATE TABLE emails (
  id INT AUTO_INCREMENT PRIMARY KEY,
  mail VARCHAR(150),
  persona_id INT,
  FOREIGN KEY (persona_id) REFERENCES persona(id) 
);

CREATE TABLE telefono (
  id INT AUTO_INCREMENT PRIMARY KEY,
  telefono VARCHAR(150),
  persona_id INT,
  FOREIGN KEY (persona_id) REFERENCES persona(id)   
);

CREATE TABLE direccion (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50),
  block VARCHAR(50),
  departamento VARCHAR(50),
  numero VARCHAR(10),
  comuna_id INT,
  FOREIGN KEY (comuna_id) REFERENCES comuna(id)
);

CREATE TABLE cliente (
  id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  persona_id INT,
  direccion_id INT,
  emails_id INT,
  telefono_id INT,
  FOREIGN KEY (persona_id) REFERENCES persona(id),
  FOREIGN KEY (direccion_id) REFERENCES direccion(id),
  FOREIGN KEY (emails_id) REFERENCES emails(id),
  FOREIGN KEY (telefono_id) REFERENCES telefono(id)
);

CREATE TABLE estudio (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(45),
  descripcion VARCHAR(45),
  direccion_id INT,
  FOREIGN KEY (direccion_id) REFERENCES direccion(id)
);

CREATE TABLE tatuador (
  id INT AUTO_INCREMENT PRIMARY KEY,
  persona_id INT,
  emails_id INT,
  telefono_id INT,
  estudio_id INT,
  FOREIGN KEY (persona_id) REFERENCES persona(id),
  FOREIGN KEY (emails_id) REFERENCES emails(id),
  FOREIGN KEY (telefono_id) REFERENCES telefono(id),
  FOREIGN KEY (estudio_id) REFERENCES estudio(id)
);

CREATE TABLE reseña (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR (45),
  cuerpo VARCHAR (200),
  calificacion INT,
  cliente_id INT,
  tatuador_id INT,
  FOREIGN KEY (cliente_id) REFERENCES cliente(id),
  FOREIGN KEY (tatuador_id) REFERENCES tatuador(id)
);

CREATE TABLE portafolio (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR (45),
  descripcion VARCHAR (200),
  foto VARCHAR (200),
  tatuador_id INT,
  FOREIGN KEY (tatuador_id) REFERENCES tatuador(id)
);

CREATE TABLE diseños (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR (45),
  descripcion VARCHAR (200),
  estilo VARCHAR (45),
  foto VARCHAR (200),
  tatuador_id INT,
  FOREIGN KEY (tatuador_id) REFERENCES tatuador(id)
);

CREATE TABLE materiales(
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR (45),
  cantidad INT,
  descripcion VARCHAR (100),
  tatuador_id INT,
  FOREIGN KEY (tatuador_id) REFERENCES tatuador(id)
);

CREATE TABLE cita (
  id INT AUTO_INCREMENT PRIMARY KEY,
  eventTitle VARCHAR(255),
  eventStartDate DATE,
  eventEndDate DATE,
  eventStartTime TIME,
  eventEndTime TIME,
  descripcion VARCHAR(45),
  tatuador_id INT,
  cliente_id INT,
  estudio_id INT,
  FOREIGN KEY (tatuador_id) REFERENCES tatuador(id),
  FOREIGN KEY (cliente_id) REFERENCES cliente(id),
  FOREIGN KEY (estudio_id) REFERENCES estudio(id)
);

CREATE TABLE factura (
  id INT AUTO_INCREMENT PRIMARY KEY,
  total INT,
  estado VARCHAR(45)
);

CREATE TABLE metodo_pago (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50),
  descripcion VARCHAR(150)
);

CREATE TABLE transacciones (
  id INT AUTO_INCREMENT PRIMARY KEY,
  monto INT,
  fecha DATETIME,
  metodo_pago_id INT,
  FOREIGN KEY (metodo_pago_id) REFERENCES metodo_pago(id)
);

CREATE TABLE detalle_factura (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nro_citas_pendientes INT,
  abono INT,
  cita_id INT,
  factura_id INT,
  transacciones_id INT,
  FOREIGN KEY (cita_id) REFERENCES cita(id),
  FOREIGN KEY (factura_id) REFERENCES factura(id),
  FOREIGN KEY (transacciones_id) REFERENCES transacciones(id)
);

CREATE TABLE contacto (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  apellido VARCHAR(100),
  email VARCHAR(100),
  fecha DATETIME,
  tatuador_id INT,
  mensaje VARCHAR(500),
  FOREIGN KEY (tatuador_id) REFERENCES tatuador(id)
);
