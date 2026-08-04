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
    # ==================================================
    # LISTAR
    # ==================================================

    def obtener_todos(self):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM alumno
            ORDER BY codigo_alumno
            """
        )

        filas = cursor.fetchall()

        conn.close()

        return [

            Alumno(

                fila["id_alumno"],
                fila["codigo_alumno"],
                fila["id_persona"],
                fila["id_distrito"]

            )

            for fila in filas

        ]

    # ==================================================
    # ACTUALIZAR
    # ==================================================

    def actualizar(
        self,
        alumno_id,
        codigo_alumno=None,
        id_persona=None,
        id_distrito=None
    ):

        # Buscar alumno actual
        alumno = self.buscar_por_id(alumno_id)

        if alumno is None:
            raise AlumnoNoEncontradoError(alumno_id)

        # Mantener valores actuales si no se envían cambios
        codigo_alumno = alumno.codigo_alumno if codigo_alumno is None else codigo_alumno
        id_persona = alumno.id_persona if id_persona is None else id_persona
        id_distrito = alumno.id_distrito if id_distrito is None else id_distrito


        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE alumno
            SET
                codigo_alumno = ?,
                id_persona = ?,
                id_distrito = ?
            WHERE id_alumno = ?
            """,
            (
                codigo_alumno,
                id_persona,
                id_distrito,
                alumno_id
            )
        )

        conn.commit()
        conn.close()

        return self.buscar_por_id(alumno_id)
    # ==================================================
    # ELIMINAR
    # ==================================================

    def eliminar(self, alumno_id):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM alumno
            WHERE id_alumno = ?
            """,
            (alumno_id,)
        )

        conn.commit()

        if cursor.rowcount == 0:

            conn.close()

            raise AlumnoNoEncontradoError(alumno_id)

        conn.close()
