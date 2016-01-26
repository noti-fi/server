import sqlite3

conn = sqlite3.connect('notifi.db')

c = conn.cursor()

#Creacion tabla Universidad

c.execute('''CREATE TABLE `UNIVERSIDAD` (`idUni` varchar(10),
`Nombre` varchar(100),
primary key (`idUni`))''')

#Creacion tabla Departamento

c.execute('''CREATE TABLE `DEPARTAMENTO` (`idDep` varchar(15),
`Nombre` varchar(100),
primary key (`idDep`))''')

#Creacion tabla Escuela
c.execute('''CREATE TABLE `ESCUELA` (`idEscuela` varchar(15),
`Nombre` varchar(100),
`UNIVERSIDAD` varchar(10),
FOREIGN KEY(`UNIVERSIDAD`) REFERENCES `UNIVERSIDAD`(`idUni`),
primary key (`idEscuela`))''')


#Creacion tabla Asignatura

c.execute('''CREATE TABLE `ASIGNATURA` (`idAsig` int,
`Nombre` varchar(100),
`ESCUELA` varchar(15),
`DEPARTAMENTO` varchar(15),
FOREIGN KEY(`ESCUELA`) REFERENCES `ESCUELA`(`idEscuela`),
FOREIGN KEY(`DEPARTAMENTO`) REFERENCES `DEPARTAMENTO`(`idDep`),
primary key (`idAsig`))''')

#Creacion tabla Categoria

c.execute('''CREATE TABLE `CATEGORIA` (`idCat` int,
`Nombre` varchar(100),
primary key (`idCat`))''')

#Creacion tabla Cambio

c.execute('''CREATE TABLE `CAMBIO` (`idCambio` int,
`Titulo` varchar(250),
`Body` varchar(150),
`Fecha` DATETIME,
`ASIGNATURA` int,
FOREIGN KEY(`ASIGNATURA`) REFERENCES `ASIGNATURA`(`idAsig`),
primary key (`idCambio`))''')

conn.commit()

conn.close()

