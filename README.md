# Sistema de Gestión de Cursos y Estudiantes - Backend

API REST desarrollada para la gestión académica de una institución educativa.

El backend permite administrar personas, distritos, alumnos, docentes, cursos y matrículas. También cuenta con un sistema de historial de actividades.

El proyecto utiliza Python, FastAPI y PostgreSQL, siguiendo una arquitectura separada por routers, schemas, modelos y DAO.

---

## Contenido

- [Descripción](#descripción)
- [Tecnologías](#tecnologías)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Arquitectura](#arquitectura)
- [Base de datos](#base-de-datos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Ejecución](#ejecución)
- [Documentación de la API](#documentación-de-la-api)
- [Endpoints](#endpoints)
- [Validaciones](#validaciones)
- [Códigos HTTP](#códigos-http)
- [CORS](#cors)
- [Historial de eventos](#historial-de-eventos)
- [Conexión con el frontend](#conexión-con-el-frontend)
- [Git](#git)
- [Seguridad](#seguridad)
- [Estado del proyecto](#estado-del-proyecto)
- [Autoría](#autoría)

---

## Descripción

El backend proporciona los servicios necesarios para que el frontend pueda consultar, registrar, actualizar y eliminar información académica.

### Módulos

- Personas
- Distritos
- Alumnos
- Docentes
- Cursos
- Matrículas
- Historial del sistema

La API implementa operaciones CRUD mediante endpoints HTTP y utiliza Pydantic para la validación de datos.

---

## Tecnologías

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal |
| FastAPI | Framework para la API REST |
| Uvicorn | Servidor ASGI |
| PostgreSQL | Sistema gestor de base de datos |
| psycopg2 | Conexión con PostgreSQL |
| Pydantic | Validación de datos |

---

## Estructura del proyecto

```text
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
```

---

## Arquitectura

El proyecto está dividido en diferentes capas para separar las responsabilidades.

### Main

`main.py` es el punto de entrada de la aplicación.

Se encarga de:

- Crear la aplicación FastAPI.
- Configurar CORS.
- Inicializar la base de datos.
- Registrar los routers.
- Definir el endpoint principal.

### Routers

La carpeta `routers/` contiene los endpoints de la API.

Cada router se encarga de recibir las solicitudes HTTP y comunicarse con la capa DAO correspondiente.

```text
routers/
├── alumnos.py
├── cursos.py
├── distritos.py
├── docentes.py
├── logs.py
├── matriculas.py
└── personas.py
```

### Schemas

La carpeta `schemas/` contiene los modelos de Pydantic.

Se utilizan para:

- Validar los datos recibidos.
- Definir los datos de entrada.
- Definir las respuestas de la API.

### Models

La carpeta `models/` contiene las entidades principales del sistema.

```text
Persona
Distrito
Alumno
Docente
Curso
Matrícula
```

### DAO

La carpeta `Dao/` contiene la capa de acceso a datos.

Los DAO se encargan de realizar operaciones como:

- Consultar registros.
- Buscar registros por ID.
- Insertar registros.
- Actualizar registros.
- Eliminar registros.

También permiten centralizar el acceso a PostgreSQL.

### Config

La carpeta `config/` contiene la configuración general.

#### base_datos.py

Gestiona la conexión con PostgreSQL y la creación de las tablas necesarias.

#### logger.py

Gestiona el historial de eventos de la aplicación.

#### sistema_config.py

Contiene información general de configuración del sistema.

---

## Base de datos

El sistema utiliza PostgreSQL.

La base de datos utilizada es:

```text
db_gestion_cursos_estudiantes
```

### Tablas

```text
distrito
persona
alumno
docente
curso
matricula
```

### Relaciones principales

```text
Distrito
   │
   └── Alumno
          │
          └── Matrícula
                 │
                 └── Curso
                        │
                        └── Docente

Persona
   ├── Alumno
   └── Docente
```

### Persona

Contiene la información personal de los usuarios relacionados con alumnos y docentes.

```text
id_persona
dni
nombres
apellidos
telefono
correo
direccion
```

### Distrito

Contiene los distritos registrados.

```text
id_distrito
nombre
```

### Alumno

Relaciona una persona con un distrito.

```text
id_alumno
codigo_alumno
id_persona
id_distrito
```

El código del alumno debe ser único.

### Docente

Relaciona una persona con una especialidad.

```text
id_docente
especialidad
id_persona
```

### Curso

Contiene la información académica de los cursos.

```text
id_curso
nombre
descripcion
creditos
ciclo
horas_semanales
id_docente
```

### Matrícula

Relaciona un alumno con un curso.

```text
id_matricula
fecha_matricula
estado
id_alumno
id_curso
```

Los estados disponibles son:

```text
ACTIVO
RETIRADO
FINALIZADO
```

---

## Instalación

### Requisitos

Antes de ejecutar el proyecto se necesita:

- Python 3
- PostgreSQL
- pip

Comprobar Python:

```bash
python --version
```

Comprobar pip:

```bash
pip --version
```

---

## Configuración

### Crear la base de datos

En PostgreSQL:

```sql
CREATE DATABASE db_gestion_cursos_estudiantes;
```

El backend se encarga de crear las tablas necesarias al iniciar.

### Variables de entorno

La conexión con PostgreSQL puede configurarse mediante variables de entorno.

Ejemplo en Windows PowerShell:

```powershell
$env:DB_HOST="localhost"
$env:DB_PORT="5432"
$env:DB_NAME="db_gestion_cursos_estudiantes"
$env:DB_USER="postgres"
$env:DB_PASSWORD="TU_CONTRASEÑA"
```

No se deben subir contraseñas reales al repositorio.

---

## Entorno virtual

Crear el entorno virtual:

```bash
python -m venv venv
```

### Windows

Activar:

```powershell
venv\Scripts\activate
```

### Linux y macOS

Activar:

```bash
source venv/bin/activate
```

---

## Instalar dependencias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

Las dependencias principales son:

```text
fastapi
uvicorn
psycopg2-binary
pydantic
```

---

## Ejecución

Ejecutar desde la carpeta principal del backend:

```bash
uvicorn main:app --reload
```

La API estará disponible en:

```text
http://localhost:8000
```

También puede utilizarse:

```text
http://127.0.0.1:8000
```

---

## Documentación de la API

FastAPI genera automáticamente la documentación de los endpoints.

### Swagger UI

```text
http://localhost:8000/docs
```

### ReDoc

```text
http://localhost:8000/redoc
```

Desde Swagger se pueden consultar y probar directamente los endpoints de la API.

---

## Endpoints

### Endpoint principal

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/` | Comprueba que la API está funcionando |

---

### Personas

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/personas/` | Listar personas |
| GET | `/personas/{persona_id}` | Obtener una persona |
| POST | `/personas/` | Registrar una persona |
| PUT | `/personas/{persona_id}` | Actualizar una persona |
| DELETE | `/personas/{persona_id}` | Eliminar una persona |

---

### Distritos

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/distritos/` | Listar distritos |
| GET | `/distritos/{distrito_id}` | Obtener un distrito |
| POST | `/distritos/` | Registrar un distrito |
| PUT | `/distritos/{distrito_id}` | Actualizar un distrito |
| DELETE | `/distritos/{distrito_id}` | Eliminar un distrito |

---

### Alumnos

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/alumnos/` | Listar alumnos |
| GET | `/alumnos/{alumno_id}` | Obtener un alumno |
| POST | `/alumnos/` | Registrar un alumno |
| PUT | `/alumnos/{alumno_id}` | Actualizar un alumno |
| DELETE | `/alumnos/{alumno_id}` | Eliminar un alumno |

---

### Docentes

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/docentes/` | Listar docentes |
| GET | `/docentes/{docente_id}` | Obtener un docente |
| POST | `/docentes/` | Registrar un docente |
| PUT | `/docentes/{docente_id}` | Actualizar un docente |
| DELETE | `/docentes/{docente_id}` | Eliminar un docente |

---

### Cursos

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/cursos/` | Listar cursos |
| GET | `/cursos/{curso_id}` | Obtener un curso |
| POST | `/cursos/` | Registrar un curso |
| PUT | `/cursos/{curso_id}` | Actualizar un curso |
| DELETE | `/cursos/{curso_id}` | Eliminar un curso |

---

### Matrículas

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/matriculas/` | Listar matrículas |
| GET | `/matriculas/{matricula_id}` | Obtener una matrícula |
| POST | `/matriculas/` | Registrar una matrícula |
| PUT | `/matriculas/{matricula_id}` | Actualizar una matrícula |
| DELETE | `/matriculas/{matricula_id}` | Eliminar una matrícula |

---

### Historial

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/logs/` | Obtener historial |
| DELETE | `/logs/` | Limpiar historial |

---

## Validaciones

El backend utiliza Pydantic para validar los datos recibidos.

### DNI

Debe contener exactamente 8 dígitos numéricos.

Ejemplo:

```text
12345678
```

### Créditos

Los créditos de un curso deben ser mayores que cero.

### Horas semanales

Las horas semanales deben ser mayores que cero.

### Estado de matrícula

Los estados permitidos son:

```text
ACTIVO
RETIRADO
FINALIZADO
```

### Datos únicos

El sistema controla valores que deben ser únicos, como:

- DNI.
- Código de alumno.

También controla relaciones entre los diferentes registros.

---

## Códigos HTTP

| Código | Significado |
|---|---|
| 200 | Operación realizada correctamente |
| 201 | Recurso creado correctamente |
| 400 | Solicitud incorrecta o regla de negocio no válida |
| 404 | Recurso no encontrado |

### Ejemplos de errores 400

- DNI duplicado.
- Código de alumno duplicado.
- Matrícula duplicada.
- Datos inválidos.
- Intentar eliminar un registro relacionado.

---

## CORS

El backend utiliza CORS para permitir la comunicación con el frontend durante el desarrollo.

Orígenes configurados:

```text
http://localhost:5173
http://localhost:5174
http://localhost:3000
```

Configuración utilizada:

```text
allow_credentials=True
allow_methods=["*"]
allow_headers=["*"]
```

---

## Historial de eventos

El sistema cuenta con un Logger implementado mediante Singleton.

Los eventos pueden registrar los siguientes niveles:

```text
INFO
WARNING
ERROR
```

El historial puede consultarse mediante:

```text
GET /logs/
```

Y puede limpiarse mediante:

```text
DELETE /logs/
```

Los registros se mantienen en memoria durante la ejecución del backend.

Por esta razón, los registros se pierden cuando la aplicación se reinicia.

---

## Conexión con el frontend

El frontend desarrollado en React se comunica con el backend mediante HTTP utilizando Axios.

La API se ejecuta normalmente en:

```text
http://localhost:8000
```

Flujo de comunicación:

```text
React
  │
  │ Axios / HTTP
  ▼
FastAPI
  │
  │ DAO
  ▼
PostgreSQL
```

El frontend utiliza los endpoints de la API para realizar las operaciones CRUD.

---

## Git

Inicializar el repositorio:

```bash
git init
```

Comprobar los archivos:

```bash
git status
```

Agregar los archivos:

```bash
git add .
```

Crear un commit:

```bash
git commit -m "Backend sistema gestión cursos y estudiantes"
```

Agregar el repositorio remoto:

```bash
git remote add origin <URL_DEL_REPOSITORIO>
```

Establecer la rama principal:

```bash
git branch -M main
```

Subir el proyecto:

```bash
git push -u origin main
```

---

## Seguridad

El proyecto está orientado principalmente a un entorno académico y de desarrollo local.

Para un entorno de producción se recomienda:

- Utilizar variables de entorno para las credenciales.
- No almacenar contraseñas directamente en el código.
- Implementar autenticación.
- Implementar autorización por roles.
- Utilizar HTTPS.
- Restringir los orígenes permitidos por CORS.
- Implementar una estrategia persistente para los logs.
- Controlar los permisos de acceso a los recursos.

---

## Estado del proyecto

El backend cuenta actualmente con:

- API REST desarrollada con FastAPI.
- Base de datos PostgreSQL.
- Conexión mediante psycopg2.
- CRUD de Personas.
- CRUD de Distritos.
- CRUD de Alumnos.
- CRUD de Docentes.
- CRUD de Cursos.
- CRUD de Matrículas.
- Historial de eventos.
- Validaciones mediante Pydantic.
- Manejo de errores HTTP.
- Configuración CORS.
- Documentación automática mediante FastAPI.
- Arquitectura DAO.
- Modelos separados.
- Schemas separados.
- Configuración de base de datos.
- Configuración mediante variables de entorno.

---

## Autoría

**Sistema de Gestión de Cursos y Estudiantes**

Proyecto académico.

### Autores

- Tello Luis
- Castro Raquel

### Institución

**ISTP Argentina**

### Versión

**1.0**
