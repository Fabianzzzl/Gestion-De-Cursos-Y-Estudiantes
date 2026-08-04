from models.matricula import Matricula
from config.base_datos import obtener_conexion


class MatriculaNoEncontradaError(Exception):

    def __init__(self, matricula_id):
        super().__init__(f"Matrícula ID={matricula_id} no encontrada")


class MatriculaDAO:

    # ==================================================
    # INSERTAR
    # ==================================================

    def insertar(self, matricula):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO matricula
            (fecha_matricula,estado,id_alumno,id_curso)
            VALUES(?,?,?,?)
            """,
            (
                matricula.fecha_matricula,
                matricula.estado,
                matricula.id_alumno,
                matricula.id_curso
            )
        )

        conn.commit()

        matricula.id_matricula = cursor.lastrowid

        conn.close()

        return matricula

    # ==================================================
    # BUSCAR POR ID
    # ==================================================

    def buscar_por_id(self, matricula_id):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM matricula
            WHERE id_matricula = ?
            """,
            (matricula_id,)
        )

        fila = cursor.fetchone()

        conn.close()

        if fila:

            return Matricula(

                fila["id_matricula"],
                fila["fecha_matricula"],
                fila["estado"],
                fila["id_alumno"],
                fila["id_curso"]

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
            FROM matricula
            ORDER BY fecha_matricula
            """
        )

        filas = cursor.fetchall()

        conn.close()

        return [

            Matricula(

                fila["id_matricula"],
                fila["fecha_matricula"],
                fila["estado"],
                fila["id_alumno"],
                fila["id_curso"]

            )

            for fila in filas

        ]

    # ==================================================
    # ACTUALIZAR
    # ==================================================

    def actualizar(
        self,
        matricula_id,
        fecha_matricula=None,
        estado=None,
        id_alumno=None,
        id_curso=None
    ):

        # Buscar matrícula actual
        matricula = self.buscar_por_id(matricula_id)

        if matricula is None:
            raise MatriculaNoEncontradaError(matricula_id)

        # Mantener valores actuales si no se envían cambios
        fecha_matricula = matricula.fecha_matricula if fecha_matricula is None else fecha_matricula
        estado = matricula.estado if estado is None else estado
        id_alumno = matricula.id_alumno if id_alumno is None else id_alumno
        id_curso = matricula.id_curso if id_curso is None else id_curso


        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE matricula
            SET
                fecha_matricula = ?,
                estado = ?,
                id_alumno = ?,
                id_curso = ?
            WHERE id_matricula = ?
            """,
            (
                fecha_matricula,
                estado,
                id_alumno,
                id_curso,
                matricula_id
            )
        )

        conn.commit()
        conn.close()

        return self.buscar_por_id(matricula_id)

    # ==================================================
    # ELIMINAR
    # ==================================================

    def eliminar(self, matricula_id):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM matricula
            WHERE id_matricula = ?
            """,
            (matricula_id,)
        )

        conn.commit()

        if cursor.rowcount == 0:

            conn.close()

            raise MatriculaNoEncontradaError(matricula_id)

        conn.close()
