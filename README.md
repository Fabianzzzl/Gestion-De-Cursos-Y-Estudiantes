Sistema de Gestión de Cursos y Estudiantes - Backend

API REST para la gestión académica de una institución educativa. El backend permite administrar personas, distritos, alumnos, docentes, cursos y matrículas, además de proporcionar un historial de actividades del sistema.

El proyecto está desarrollado con Python, FastAPI y PostgreSQL y utiliza una arquitectura separada por routers, schemas, modelos y DAO.

Contenido

Descripción

Tecnologías

Estructura del proyecto

Arquitectura

Base de datos

Instalación

Configuración de PostgreSQL

Ejecución

Documentación de la API

Endpoints

Códigos HTTP

Validaciones

CORS

Historial de eventos

Conexión con el frontend

Git

Seguridad

Estado del proyecto

Autoría

Descripción

El backend proporciona los servicios necesarios para que el frontend pueda consultar y administrar la información académica.

Módulos principales

Personas

Distritos

Alumnos

Docentes

Cursos

Matrículas

Historial del sistema

La API expone operaciones CRUD mediante endpoints HTTP y utiliza Pydantic para validar los datos.

Tecnologías

Tecnología

Uso

Python

Lenguaje principal

FastAPI

Framework para la API REST

Uvicorn

Servidor ASGI

PostgreSQL

Base de datos

psycopg2-binary

Conexión con PostgreSQL

Pydantic

Validación de datos

Dependencias

Las dependencias del proyecto se encuentran en requirements.txt:

fastapi
uvicorn
psycopg2-binary
pydantic

Estructura del proyecto

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

Arquitectura

El proyecto separa las responsabilidades en diferentes capas.

main.py

Es el punto de entrada de la API.

Aquí se:

Crea la aplicación FastAPI.

Configura CORS.

Inicializa la base de datos.

Registra los routers.

Define el endpoint principal /.

routers/

Contiene los endpoints HTTP de cada módulo.

Los routers reciben las peticiones del cliente y utilizan los DAO para realizar las operaciones correspondientes.

schemas/

Contiene los modelos de Pydantic utilizados para:

Recibir datos.

Validar datos.

Definir respuestas de la API.

Por ejemplo:

PersonaCrear

PersonaActualizar

PersonaRespuesta

models/

Contiene las clases que representan las entidades del sistema:

Persona

Distrito

Alumno

Docente

Curso

Matrícula

Dao/

Contiene las clases de acceso a datos.

Los DAO se encargan de realizar operaciones sobre PostgreSQL, como:

Obtener registros.

Buscar por ID.

Insertar.

Actualizar.

Eliminar.

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

Nombre.

Versión.

Empresa.

Autor.

Base de datos

El backend utiliza PostgreSQL.

La base de datos configurada por defecto es:

db_gestion_cursos_estudiantes

Configuración de conexión

Variable

Valor predeterminado

DB_HOST

localhost

DB_PORT

5432

DB_NAME

db_gestion_cursos_estudiantes

DB_USER

postgres

DB_PASSWORD

configuración local

La configuración puede modificarse mediante variables de entorno.

La base de datos PostgreSQL debe existir antes de iniciar la aplicación. Al iniciar el backend, base_datos.py crea las tablas que no existan.

Modelo de datos

El sistema utiliza las siguientes tablas:

distrito

persona

alumno

docente

curso

matricula

Relaciones principales

DISTRITO
   └── ALUMNO
          └── MATRÍCULA ─── CURSO
                              └── DOCENTE

PERSONA
   ├── ALUMNO
   └── DOCENTE

Distrito

Contiene los distritos disponibles.

Campos principales:

id_distrito
nombre

Persona

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

Alumno

Relaciona una persona con un distrito.

Campos:

id_alumno
codigo_alumno
id_persona
id_distrito

El código del alumno es único.

Docente

Relaciona una persona con una especialidad.

Campos:

id_docente
especialidad
id_persona

Curso

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

Matrícula

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

Instalación

Requisitos

Se necesita tener instalado:

Python 3

PostgreSQL

pip

Comprobar Python:

python --version

Comprobar pip:

pip --version

Configuración de PostgreSQL

Crear en PostgreSQL la base de datos:

CREATE DATABASE db_gestion_cursos_estudiantes;

Después verificar que PostgreSQL esté ejecutándose.

El backend se encargará de crear las tablas al iniciar.

Variables de entorno

Si las credenciales locales no coinciden con los valores predeterminados, se pueden configurar variables de entorno.

Ejemplo en Windows PowerShell:

$env:DB_HOST="localhost"
$env:DB_PORT="5432"
$env:DB_NAME="db_gestion_cursos_estudiantes"
$env:DB_USER="postgres"
$env:DB_PASSWORD="TU_CONTRASEÑA"

Después iniciar el servidor en la misma terminal.

No subas contraseñas reales al repositorio.

Crear entorno virtual

Desde la carpeta del backend.

Windows

python -m venv venv

Activar:

venv\Scripts\activate

Linux / macOS

python3 -m venv venv

Activar:

source venv/bin/activate

Instalar dependencias

Con el entorno virtual activado:

pip install -r requirements.txt

Ejecución

Desde la raíz del proyecto:

uvicorn main:app --reload

La API estará disponible normalmente en:

http://127.0.0.1:8000

También puede utilizarse:

http://localhost:8000

Documentación de la API

FastAPI genera documentación automáticamente.

Swagger UI

http://localhost:8000/docs

ReDoc

http://localhost:8000/redoc

Estas páginas permiten consultar y probar los endpoints directamente desde el navegador.

Endpoints

Endpoint principal

GET /

Comprueba que la API está funcionando.

Respuesta:

{
  "mensaje": "API del Sistema de Gestión de Cursos y Estudiantes funcionando correctamente"
}

Personas

Base: /personas

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

Validación: el DNI debe contener exactamente 8 dígitos numéricos.

Distritos

Base: /distritos

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

Alumnos

Base: /alumnos

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

Docentes

Base: /docentes

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

Cursos

Base: /cursos

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

Matrículas

Base: /matriculas

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

Historial

Base: /logs

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

Códigos HTTP

El backend utiliza principalmente:

Código

Significado

200

OK

201

Created

400

Bad Request

404

Not Found

200 OK

La operación se realizó correctamente.

201 Created

Se creó correctamente un nuevo recurso.

400 Bad Request

Los datos enviados no son válidos o la operación no puede realizarse debido a una regla del sistema.

Ejemplos:

DNI duplicado.

Código de alumno duplicado.

Curso con datos inválidos.

Matrícula duplicada.

Intentar eliminar un registro relacionado.

404 Not Found

El recurso solicitado no existe.

Validaciones

El backend utiliza Pydantic para validar los datos.

DNI

Debe tener exactamente:

8 dígitos numéricos

Ejemplo válido:

12345678

Créditos

Debe ser mayor que cero.

Horas semanales

Debe ser mayor que cero.

Estado de matrícula

Solo se permiten:

ACTIVO
RETIRADO
FINALIZADO

CORS

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

Historial de eventos

El sistema posee un Logger implementado como Singleton.

Permite registrar:

INFO
WARNING
ERROR

Los registros se mantienen en memoria durante la ejecución de la aplicación.

Por lo tanto, el historial no se almacena permanentemente en PostgreSQL.

Al reiniciar el backend, los registros en memoria se pierden.

Conexión con el frontend

El frontend React utiliza esta API para realizar las operaciones CRUD.

La comunicación se realiza mediante HTTP utilizando Axios.

La configuración local utilizada por el frontend apunta a:

http://localhost:8000

Flujo de comunicación

Frontend React
      │
      │ HTTP / Axios
      ▼
   FastAPI
      │
      │ DAO
      ▼
 PostgreSQL

Git

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

Seguridad

Este proyecto está orientado a un entorno académico/local.

Para un entorno de producción se recomienda:

No guardar contraseñas directamente en el código.

Utilizar variables de entorno.

Implementar autenticación.

Implementar autorización por roles.

Utilizar HTTPS.

Restringir CORS a dominios autorizados.

Validar y controlar los permisos de acceso a los recursos.

Utilizar una estrategia persistente para los logs.

Estado del proyecto

Actualmente el backend cuenta con:

API REST con FastAPI.

PostgreSQL.

Conexión mediante psycopg2.

CRUD de Personas.

CRUD de Distritos.

CRUD de Alumnos.

CRUD de Docentes.

CRUD de Cursos.

CRUD de Matrículas.

Historial de logs.

Validación mediante Pydantic.

Manejo de errores HTTP.

CORS.

Documentación automática de FastAPI.

Arquitectura DAO.

Modelos separados.

Schemas separados.

Configuración de base de datos.

Variables de entorno para configuración de PostgreSQL.

Autoría

Sistema de Gestión de Cursos y Estudiantes

Proyecto académico.

Autores configurados en el sistema

Tello Luis

Castro Raquel

Empresa / institución configurada

ISTP Argentina

Versión

1.0
