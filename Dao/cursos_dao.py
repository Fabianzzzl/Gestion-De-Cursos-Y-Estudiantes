from models.curso import Curso
from config.base_datos import obtener_conexion


class CursoNoEncontradoError(Exception):

    def __init__(self, curso_id):
        super().__init__(f"Curso ID={curso_id} no encontrado")


class CursoDAO:

    # ==================================================
    # INSERTAR
    # ==================================================

    def insertar(self, curso):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO curso
            (nombre,descripcion,creditos,ciclo,horas_semanales,id_docente)
            VALUES(?,?,?,?,?,?)
            """,
            (
                curso.nombre,
                curso.descripcion,
                curso.creditos,
                curso.ciclo,
                curso.horas_semanales,
                curso.id_docente
            )
        )

        conn.commit()

        curso.id_curso = cursor.lastrowid

        conn.close()

        return curso

    # ==================================================
    # BUSCAR POR ID
    # ==================================================

    def buscar_por_id(self, curso_id):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM curso
            WHERE id_curso = ?
            """,
            (curso_id,)
        )

        fila = cursor.fetchone()

        conn.close()

        if fila:

            return Curso(

                fila["id_curso"],
                fila["nombre"],
                fila["descripcion"],
                fila["creditos"],
                fila["ciclo"],
                fila["horas_semanales"],
                fila["id_docente"]

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
            FROM curso
            ORDER BY nombre
            """
        )

        filas = cursor.fetchall()

        conn.close()

        return [

            Curso(

                fila["id_curso"],
                fila["nombre"],
                fila["descripcion"],
                fila["creditos"],
                fila["ciclo"],
                fila["horas_semanales"],
                fila["id_docente"]

            )

            for fila in filas

        ]
    # ==================================================
    # ACTUALIZAR
    # ==================================================

    def actualizar(
        self,
        curso_id,
        nombre=None,
        descripcion=None,
        creditos=None,
        ciclo=None,
        horas_semanales=None,
        id_docente=None
    ):

        # Buscar curso actual
        curso = self.buscar_por_id(curso_id)

        if curso is None:
            raise CursoNoEncontradoError(curso_id)

        # Mantener valores actuales si no se envían cambios
        nombre = curso.nombre if nombre is None else nombre
        descripcion = curso.descripcion if descripcion is None else descripcion
        creditos = curso.creditos if creditos is None else creditos
        ciclo = curso.ciclo if ciclo is None else ciclo
        horas_semanales = curso.horas_semanales if horas_semanales is None else horas_semanales
        id_docente = curso.id_docente if id_docente is None else id_docente


        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE curso
            SET
                nombre = ?,
                descripcion = ?,
                creditos = ?,
                ciclo = ?,
                horas_semanales = ?,
                id_docente = ?
            WHERE id_curso = ?
            """,
            (
                nombre,
                descripcion,
                creditos,
                ciclo,
                horas_semanales,
                id_docente,
                curso_id
            )
        )

        conn.commit()
        conn.close()

        return self.buscar_por_id(curso_id)

    # ==================================================
    # ELIMINAR
    # ==================================================

    def eliminar(self, curso_id):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM curso
            WHERE id_curso = ?
            """,
            (curso_id,)
        )

        conn.commit()

        if cursor.rowcount == 0:

            conn.close()

            raise CursoNoEncontradoError(curso_id)

        conn.close()
