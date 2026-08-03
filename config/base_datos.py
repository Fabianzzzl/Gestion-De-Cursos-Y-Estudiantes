import sqlite3

ARCHIVO_DB = "gestion_cursos_estudiantes.db"


def obtener_conexion():

    conn = sqlite3.connect(ARCHIVO_DB)
    
    conn.execute("PRAGMA foreign_keys = ON")

    conn.row_factory = sqlite3.Row

    return conn


def Inicializar():

    conn = obtener_conexion()

    cursor = conn.cursor()

    # ==========================================
    # TABLA DISTRITO
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS distrito(

            id_distrito INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL

        )
    """)

    # ==========================================
    # TABLA PERSONA
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS persona(

            id_persona INTEGER PRIMARY KEY AUTOINCREMENT,

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

            id_alumno INTEGER PRIMARY KEY AUTOINCREMENT,

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

            id_docente INTEGER PRIMARY KEY AUTOINCREMENT,

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

            id_curso INTEGER PRIMARY KEY AUTOINCREMENT,

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

            id_matricula INTEGER PRIMARY KEY AUTOINCREMENT,

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
                ('ACTIVO','RETIRADO','FINALIZADO')
            )

        )
    """)

    conn.commit()

    conn.close()


if __name__ == "__main__":

    Inicializar()

    print("Base de datos creada correctamente.")