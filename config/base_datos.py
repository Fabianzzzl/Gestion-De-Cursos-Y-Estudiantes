import os
import psycopg2
from psycopg2.extras import RealDictCursor

# ==========================================
# CONFIGURACIÓN DE POSTGRESQL
# ==========================================

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME","db_gestion_cursos_estudiantes")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# ==========================================
# OBTENER CONEXIÓN
# ==========================================

def obtener_conexion():

    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        cursor_factory=RealDictCursor
    )

    return conn

# ==========================================
# INICIALIZAR BASE DE DATOS
# ==========================================

def Inicializar():

    conn = obtener_conexion()
    cursor = conn.cursor()

    # ==========================================
    # TABLA DISTRITO
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS distrito(

            id_distrito INTEGER
                GENERATED ALWAYS AS IDENTITY
                PRIMARY KEY,

            nombre TEXT NOT NULL

        )
    """)

    # ==========================================
    # TABLA PERSONA
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS persona(

            id_persona INTEGER
                GENERATED ALWAYS AS IDENTITY
                PRIMARY KEY,

            dni TEXT NOT NULL UNIQUE,

            nombres TEXT NOT NULL,

            apellidos TEXT NOT NULL,

            telefono TEXT,

            correo TEXT UNIQUE,

            direccion TEXT

        )
    """)

    # ==========================================
    # TABLA ALUMNO
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alumno(

            id_alumno INTEGER
                GENERATED ALWAYS AS IDENTITY
                PRIMARY KEY,

            codigo_alumno TEXT NOT NULL UNIQUE,

            id_persona INTEGER NOT NULL,

            id_distrito INTEGER NOT NULL,

            FOREIGN KEY(id_persona)
                REFERENCES persona(id_persona),

            FOREIGN KEY(id_distrito)
                REFERENCES distrito(id_distrito)

        )
    """)

    # ==========================================
    # TABLA DOCENTE
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS docente(

            id_docente INTEGER
                GENERATED ALWAYS AS IDENTITY
                PRIMARY KEY,

            especialidad TEXT NOT NULL,

            id_persona INTEGER NOT NULL,

            FOREIGN KEY(id_persona)
                REFERENCES persona(id_persona)

        )
    """)

    # ==========================================
    # TABLA CURSO
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS curso(

            id_curso INTEGER
                GENERATED ALWAYS AS IDENTITY
                PRIMARY KEY,

            nombre TEXT NOT NULL,

            descripcion TEXT,

            creditos INTEGER NOT NULL,

            ciclo TEXT NOT NULL,

            horas_semanales INTEGER NOT NULL,

            id_docente INTEGER NOT NULL,

            FOREIGN KEY(id_docente)
                REFERENCES docente(id_docente),

            CHECK(creditos > 0),

            CHECK(horas_semanales > 0)

        )
    """)

    # ==========================================
    # TABLA MATRICULA
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matricula(

            id_matricula INTEGER
                GENERATED ALWAYS AS IDENTITY
                PRIMARY KEY,

            fecha_matricula TEXT NOT NULL,

            estado TEXT NOT NULL,

            id_alumno INTEGER NOT NULL,

            id_curso INTEGER NOT NULL,

            FOREIGN KEY(id_alumno)
                REFERENCES alumno(id_alumno),

            FOREIGN KEY(id_curso)
                REFERENCES curso(id_curso),

            CHECK(
                estado IN
                ('ACTIVO', 'RETIRADO', 'FINALIZADO')
            )

        )
    """)

    # ==========================================
    # GUARDAR CAMBIOS
    # ==========================================

    conn.commit()

    # ==========================================
    # CERRAR
    # ==========================================

    cursor.close()
    conn.close()

# ==========================================
# EJECUTAR DIRECTAMENTE
# ==========================================

if __name__ == "__main__":
    Inicializar()
    print( "Base de datos PostgreSQL creada correctamente." )
