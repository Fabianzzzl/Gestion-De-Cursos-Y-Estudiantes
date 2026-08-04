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
