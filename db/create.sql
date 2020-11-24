CREATE TABLE datasets (
	id_archivo INT AUTO_INCREMENT PRIMARY KEY,
    id_proyecto INT NOT NULL,
    nombre_proyecto VARCHAR(100) NOT NULL,
    encargado VARCHAR(25) NOT NULL,
    tipo_archivo VARCHAR(25) NOT NULL,
    archivo_dir VARCHAR(50) NOT NULL,
    archivo_nombre VARCHAR(100) NOT NULL
)
