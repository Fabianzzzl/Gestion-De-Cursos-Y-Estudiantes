# Sistema de Gestión de Cursos y Estudiantes — Backend

API REST para la gestión académica de una institución educativa. El backend permite administrar personas, distritos, alumnos, docentes, cursos y matrículas, además de proporcionar un historial de actividades del sistema.

El proyecto está desarrollado con Python, FastAPI y PostgreSQL y utiliza una arquitectura separada por routers, schemas, modelos y DAO.

# 1. Descripción

El backend proporciona los servicios necesarios para que el frontend pueda consultar y administrar la información académica.

Los módulos principales son:

·Personas
·Distritos
·Alumnos
·Docentes
·Cursos
·Matrículas
·Historial del sistema

La API expone operaciones CRUD mediante endpoints HTTP y utiliza Pydantic para validar los datos recibidos.

# 2. Tecnologías

·Python
·FastAPI
·Uvicorn
·PostgreSQL
·psycopg2-binary
·Pydantic

Dependencias actuales:

fastapi
uvicorn
psycopg2-binary
pydantic

Estas dependencias se encuentran en requirements.txt.

# 3. Arquitectura del proyecto

El backend está organizado de la siguiente manera:

Gestion-De-Cursos-Y-Estudiantes/
│
├── Dao/
│   ├── alumno_dao.py
│   ├── cursos_dao.py
│   ├── distrito_dao.py
│   ├── docente_dao.py
│   ├── matricula_dao.py
│   └── persona_dao.py
│
├── config/
│   ├── base_datos.py
│   ├── logger.py
│   └── sistema_config.py
│
├── models/
│   ├── alumno.py
│   ├── curso.py
│   ├── distrito.py
│   ├── docente.py
│   ├── matricula.py
│   └── persona.py
│
├── routers/
│   ├── alumnos.py
│   ├── cursos.py
│   ├── distritos.py
│   ├── docentes.py
│   ├── logs.py
│   ├── matriculas.py
│   └── personas.py
│
├── schemas/
│   ├── alumno_schema.py
│   ├── curso_schema.py
│   ├── distrito_schema.py
│   ├── docente_schema.py
│   ├── matricula_schema.py
│   └── persona_schema.py
│
├── view/
│   └── menu.py
│
├── main.py
├── requirements.txt
└── .gitignore

# 4. Función de cada capa

main.py

Es el punto de entrada de la API.

Aquí se:

·Crea la aplicación FastAPI.
·Configura CORS.
·Inicializa la base de datos.
·Registra los routers.
·Define el endpoint principal /.

routers/

Contiene los endpoints HTTP de cada módulo.

Los routers reciben las peticiones del cliente y utilizan los DAO para realizar las operaciones correspondientes.

schemas/

Contiene los modelos de Pydantic utilizados para:

·Recibir datos.
·Validar datos.
·Definir respuestas de la API.

Por ejemplo, PersonaCrear, PersonaActualizar y PersonaRespuesta.

models/

Contiene las clases que representan las entidades del sistema:

·Persona
·Distrito
·Alumno
·Docente
·Curso
·Matrícula

Dao/

Contiene las clases de acceso a datos.

Los DAO se encargan de realizar operaciones sobre PostgreSQL, como:

·Obtener registros.
·Buscar por ID.
·Insertar.
·Actualizar.
·Eliminar.

También contienen errores específicos para diferentes situaciones, como registros duplicados o registros relacionados.

config/

Contiene la configuración general del sistema.

base_datos.py

Gestiona la conexión con PostgreSQL y crea las tablas necesarias mediante CREATE TABLE IF NOT EXISTS.

logger.py

Implementa el historial de eventos del sistema mediante un Singleton.

Los eventos pueden tener los niveles:

INFO
WARNING
ERROR

sistema_config.py

Contiene la configuración general del sistema, como:

·Nombre.
·Versión.
·Empresa.
·Autor.

# 5. Base de datos

El backend utiliza PostgreSQL.

La base de datos configurada por defecto es:

db_gestion_cursos_estudiantes

La conexión utiliza los siguientes valores:

Host: localhost
Puerto: 5432
Base de datos: db_gestion_cursos_estudiantes
Usuario: postgres
Contraseña: configuración local

La configuración puede modificarse mediante variables de entorno.

Variables utilizadas

DB_HOST
DB_PORT
DB_NAME
DB_USER
DB_PASSWORD

Valores predeterminados definidos por el proyecto:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=db_gestion_cursos_estudiantes
DB_USER=postgres
DB_PASSWORD=

La base de datos PostgreSQL debe existir antes de iniciar la aplicación. Al iniciar el backend, base_datos.py crea las tablas que no existan.

# 6. Modelo de datos

El sistema utiliza las siguientes tablas:

distrito
persona
alumno
docente
curso
matricula

Relaciones principales:

DISTRITO
   │
   └── ALUMNO
          │
          └── MATRÍCULA ─── CURSO
                              │
                              └── DOCENTE
                                   │
                                   └── PERSONA

PERSONA
   │
   ├── ALUMNO
   │
   └── DOCENTE

# Distrito

Contiene los distritos disponibles.

Campos principales:

id_distrito
nombre

# Persona

Contiene la información personal.

Campos:

id_persona
dni
nombres
apellidos
telefono
correo
direccion

El DNI es único.

# Alumno

Relaciona una persona con un distrito.

Campos:

id_alumno
codigo_alumno
id_persona
id_distrito

El código del alumno es único.

# Docente

Relaciona una persona con una especialidad.

Campos:

id_docente
especialidad
id_persona

# Curso

Contiene la información académica del curso.

Campos:

id_curso
nombre
descripcion
creditos
ciclo
horas_semanales
id_docente

Los créditos y las horas semanales deben ser mayores que cero.

# Matrícula

Relaciona un alumno con un curso.

Campos:

id_matricula
fecha_matricula
estado
id_alumno
id_curso

Los estados permitidos son:

ACTIVO
RETIRADO
FINALIZADO

# 7. Instalación

Requisitos

Se necesita tener instalado:

·Python 3
·PostgreSQL
·pip

Comprobar Python:

python --version

Comprobar pip:

pip --version

# 8. Crear la base de datos

Crear en PostgreSQL la base de datos:

CREATE DATABASE db_gestion_cursos_estudiantes;

Después verificar que PostgreSQL esté ejecutándose.

El backend se encargará de crear las tablas al iniciar.

# 9. Crear entorno virtual

Desde la carpeta del backend:

Windows

python -m venv venv

Activar:

venv\Scripts\activate

Linux / macOS

python3 -m venv venv

Activar:

source venv/bin/activate

# 10. Instalar dependencias

Con el entorno virtual activado:

pip install -r requirements.txt

# 11. Configurar PostgreSQL

Si las credenciales locales no coinciden con los valores predeterminados, se pueden configurar variables de entorno.

Windows PowerShell

Ejemplo:

$env:DB_HOST="localhost"
$env:DB_PORT="5432"
$env:DB_NAME="db_gestion_cursos_estudiantes"
$env:DB_USER="postgres"
$env:DB_PASSWORD="TU_CONTRASEÑA"

Después iniciar el servidor en la misma terminal.

No subas contraseñas reales al repositorio.

# 12. Ejecutar la API

Desde la raíz del proyecto:

uvicorn main:app --reload

La API estará disponible normalmente en:

http://127.0.0.1:8000

También puede utilizarse:

http://localhost:8000

# 13. Documentación automática

FastAPI genera documentación automáticamente.

# Swagger UI

http://localhost:8000/docs

# ReDoc

http://localhost:8000/redoc

Estas páginas permiten consultar y probar los endpoints directamente desde el navegador.

# 14. Endpoint principal

# GET /

Comprueba que la API está funcionando.

Respuesta:

{
  "mensaje": "API del Sistema de Gestión de Cursos y Estudiantes funcionando correctamente"
}

# 15. Endpoints

# Personas

Base:

/personas

Método

Endpoint

Función

GET

/personas/

Listar personas

GET

/personas/{persona_id}

Obtener persona

POST

/personas/

Crear persona

PUT

/personas/{persona_id}

Actualizar persona

DELETE

/personas/{persona_id}

Eliminar persona

El DNI debe contener exactamente 8 dígitos numéricos.

# Distritos

Base:

/distritos

Método

Endpoint

Función

GET

/distritos/

Listar distritos

GET

/distritos/{distrito_id}

Obtener distrito

POST

/distritos/

Crear distrito

PUT

/distritos/{distrito_id}

Actualizar distrito

DELETE

/distritos/{distrito_id}

Eliminar distrito

# Alumnos

Base:

/alumnos

Método

Endpoint

Función

GET

/alumnos/

Listar alumnos

GET

/alumnos/{alumno_id}

Obtener alumno

POST

/alumnos/

Crear alumno

PUT

/alumnos/{alumno_id}

Actualizar alumno

DELETE

/alumnos/{alumno_id}

Eliminar alumno

Cada alumno requiere:

codigo_alumno
id_persona
id_distrito

El código del alumno debe ser único.

# Docentes

Base:

/docentes

Método

Endpoint

Función

GET

/docentes/

Listar docentes

GET

/docentes/{docente_id}

Obtener docente

POST

/docentes/

Crear docente

PUT

/docentes/{docente_id}

Actualizar docente

DELETE

/docentes/{docente_id}

Eliminar docente

Cada docente contiene:

especialidad
id_persona

# Cursos

Base:

/cursos

Método

Endpoint

Función

GET

/cursos/

Listar cursos

GET

/cursos/{curso_id}

Obtener curso

POST

/cursos/

Crear curso

PUT

/cursos/{curso_id}

Actualizar curso

DELETE

/cursos/{curso_id}

Eliminar curso

Datos principales:

nombre
descripcion
creditos
ciclo
horas_semanales
id_docente

Validaciones:

creditos > 0

horas_semanales > 0

# Matrículas

Base:

/matriculas

Método

Endpoint

Función

GET

/matriculas/

Listar matrículas

GET

/matriculas/{matricula_id}

Obtener matrícula

POST

/matriculas/

Crear matrícula

PUT

/matriculas/{matricula_id}

Actualizar matrícula

DELETE

/matriculas/{matricula_id}

Eliminar matrícula

Datos principales:

fecha_matricula
estado
id_alumno
id_curso

Estados válidos:

ACTIVO
RETIRADO
FINALIZADO

# Historial

Base:

/logs

Método

Endpoint

Función

GET

/logs/

Obtener historial

DELETE

/logs/

Limpiar historial

Cada evento contiene:

{
  "hora": "12:30:15",
  "nivel": "INFO",
  "msg": "Mensaje del evento"
}

# 16. Códigos HTTP utilizados

El backend utiliza principalmente:

200 OK
201 Created
400 Bad Request
404 Not Found

# 200

La operación se realizó correctamente.

# 201

Se creó correctamente un nuevo recurso.

# 400

Los datos enviados no son válidos o la operación no puede realizarse debido a una regla del sistema.

Ejemplos:

·DNI duplicado.
·Código de alumno duplicado.
·Curso con datos inválidos.
·Matrícula duplicada.
·Intentar eliminar un registro relacionado.

# 404

El recurso solicitado no existe.

# 17. Validaciones

El backend utiliza Pydantic para validar los datos.

# DNI

Debe tener exactamente:

8 dígitos numéricos

Ejemplo válido:

12345678

# Créditos

Debe ser mayor que cero.

# Horas semanales

Debe ser mayor que cero.

# Estado de matrícula

Solo se permiten:

ACTIVO
RETIRADO
FINALIZADO

# 18. CORS

La API tiene configurado CORS para permitir conexiones desde los puertos utilizados por el frontend local.

Actualmente se permiten:

http://localhost:5173
http://localhost:5174
http://localhost:3000

También están habilitados:

allow_credentials=True
allow_methods=["*"]
allow_headers=["*"]

Esto permite que el frontend React pueda comunicarse con la API durante el desarrollo local.

# 19. Historial interno

El sistema posee un Logger implementado como Singleton.

Permite registrar:

INFO
WARNING
ERROR

Los registros se mantienen en memoria durante la ejecución de la aplicación.

Por lo tanto, el historial no se almacena permanentemente en PostgreSQL.

Al reiniciar el backend, los registros en memoria se pierden.

# 20. Ejemplo de ejecución

Una ejecución típica del proyecto es:

# Crear entorno
python -m venv venv

# Activar entorno en Windows
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar API
uvicorn main:app --reload

Después abrir:

http://localhost:8000/docs

# 21. Conexión con el frontend

El frontend React utiliza esta API para realizar las operaciones CRUD.

La comunicación se realiza mediante HTTP utilizando Axios.

La configuración local utilizada por el frontend apunta a:

http://localhost:8000

Por ejemplo:

Frontend
    │
    │ HTTP / Axios
    ▼
FastAPI
    │
    │ DAO
    ▼
PostgreSQL

# 22. .gitignore

El repositorio ignora archivos que no deben subirse a Git, entre ellos:

__pycache__/
*.py[cod]

venv/
.venv/
env/

.env

*.db
*.sqlite
*.sqlite3

.vscode/

*.log

·Esto evita subir:
·Entornos virtuales.
·Archivos temporales de Python.
·Variables de entorno.
·Bases de datos locales.
·Configuración del editor.
·Logs.

# 23. Git

Para subir el proyecto a GitHub:

git init

Comprobar el estado:

git status

Agregar los archivos:

git add .

Crear el commit:

git commit -m "Backend sistema gestión cursos y estudiantes"

Agregar el repositorio remoto:

git remote add origin <URL_DEL_REPOSITORIO>

Establecer la rama principal:

git branch -M main

Subir el proyecto:

git push -u origin main

# 24. Seguridad

Este proyecto está orientado a un entorno académico/local.

Para un entorno de producción se recomienda:

·No guardar contraseñas directamente en el código.
·Utilizar variables de entorno.
·Implementar autenticación.
·Implementar autorización por roles.
·Utilizar HTTPS.
·Restringir CORS a dominios autorizados.
·Validar y controlar los permisos de acceso a los recursos.
·Utilizar una estrategia persistente para los logs.

# 25. Estado del proyecto

Actualmente el backend cuenta con:

API REST con FastAPI
PostgreSQL
Conexión mediante psycopg2
CRUD de Personas
CRUD de Distritos
CRUD de Alumnos
CRUD de Docentes
CRUD de Cursos
CRUD de Matrículas
Historial de logs
Validación mediante Pydantic
Manejo de errores HTTP
CORS
Documentación automática de FastAPI
Arquitectura DAO
Modelos separados
Schemas separados
Configuración de base de datos
Variables de entorno para configuración de PostgreSQL

# 26. Autoría

Sistema de Gestión de Cursos y Estudiantes

Proyecto académico.

Autores configurados en el sistema:

Tello Luis
Castro Raquel

Empresa/institución configurada:

ISTP Argentina

Versión:

1.0
