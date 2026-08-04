from models.alumno import Alumno
from config.base_datos import obtener_conexion


class AlumnoNoEncontradoError(Exception):

    def __init__(self, alumno_id):
        super().__init__(f"Alumno ID={alumno_id} no encontrado")


class CodigoAlumnoDuplicadoError(Exception):

    def __init__(self, codigo):
        super().__init__(f"Código '{codigo}' ya registrado")


class AlumnoDAO:

    # ==================================================
    # INSERTAR
    # ==================================================

    def insertar(self, alumno):

        if self.buscar_por_codigo(alumno.codigo_alumno):
            raise CodigoAlumnoDuplicadoError(alumno.codigo_alumno)

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO alumno
            (codigo_alumno,id_persona,id_distrito)
            VALUES(?,?,?)
            """,
            (
                alumno.codigo_alumno,
                alumno.id_persona,
                alumno.id_distrito
            )
        )

        conn.commit()

        alumno.id_alumno = cursor.lastrowid

        conn.close()

        return alumno

    # ==================================================
    # BUSCAR POR CÓDIGO
    # ==================================================

    def buscar_por_codigo(self, codigo):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM alumno
            WHERE codigo_alumno = ?
            """,
            (codigo,)
        )

        fila = cursor.fetchone()

        conn.close()

        if fila:

            return Alumno(

                fila["id_alumno"],
                fila["codigo_alumno"],
                fila["id_persona"],
                fila["id_distrito"]

            )

        return None

    # ==================================================
    # BUSCAR POR ID
    # ==================================================

    def buscar_por_id(self, alumno_id):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM alumno
            WHERE id_alumno = ?
            """,
            (alumno_id,)
        )

        fila = cursor.fetchone()

        conn.close()

        if fila:

            return Alumno(

                fila["id_alumno"],
                fila["codigo_alumno"],
                fila["id_persona"],
                fila["id_distrito"]

            )

        return None
