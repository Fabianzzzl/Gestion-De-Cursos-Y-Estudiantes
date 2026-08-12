# Sistema de Gestión de Cursos y Estudiantes - Backend

API REST para la gestión académica de una institución educativa.

El backend permite administrar la información relacionada con personas, alumnos, docentes, distritos, cursos y matrículas. También cuenta con un sistema de registro de actividades para llevar un historial de las operaciones realizadas.

El proyecto está desarrollado en Python utilizando FastAPI y PostgreSQL, siguiendo una arquitectura organizada por routers, schemas, models y DAO.

## Descripción

El sistema permite realizar operaciones CRUD sobre las principales entidades del sistema académico:

- Personas
- Distritos
- Alumnos
- Docentes
- Cursos
- Matrículas

Además, incluye funcionalidades de búsqueda, consulta por identificador, validación de datos, relaciones entre entidades y registro de actividades del sistema.

La API cuenta con documentación automática mediante Swagger.

## Tecnologías utilizadas

- Python
- FastAPI
- PostgreSQL
- Pydantic
- psycopg2
- Uvicorn
- SQL

## Arquitectura del proyecto

El backend está organizado de la siguiente manera:

```text
Backend/
│
├── config/
│   └── base_datos.py
│
├── Dao/
│   ├── alumno_dao.py
│   ├── cursos_dao.py
│   ├── distrito_dao.py
│   ├── docente_dao.py
│   ├── matricula_dao.py
│   └── persona_dao.py
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
├── main.py
└── requirements.txt
