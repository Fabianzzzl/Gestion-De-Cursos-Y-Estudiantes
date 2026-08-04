from models.docente import Docente
from config.base_datos import obtener_conexion


class DocenteNoEncontradoError(Exception):

    def __init__(self, docente_id):
        super().__init__(f"Docente ID={docente_id} no encontrado")


class DocenteDAO:

    # ==================================================
    # INSERTAR
    # ==================================================

    def insertar(self, docente):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO docente
            (especialidad,id_persona)
            VALUES(?,?)
            """,
            (
                docente.especialidad,
                docente.id_persona
            )
        )

        conn.commit()

        docente.id_docente = cursor.lastrowid

        conn.close()

        return docente

    # ==================================================
    # BUSCAR POR ID
    # ==================================================

    def buscar_por_id(self, docente_id):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM docente
            WHERE id_docente = ?
            """,
            (docente_id,)
        )

        fila = cursor.fetchone()

        conn.close()

        if fila:

            return Docente(

                fila["id_docente"],
                fila["especialidad"],
                fila["id_persona"]

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
            FROM docente
            ORDER BY especialidad
            """
        )

        filas = cursor.fetchall()

        conn.close()

        return [

            Docente(

                fila["id_docente"],
                fila["especialidad"],
                fila["id_persona"]

            )

            for fila in filas

        ]

    # ==================================================
    # ACTUALIZAR
    # ==================================================

    def actualizar(
    self,
    docente_id,
    especialidad=None,
    id_persona=None
    ):

    # Buscar docente actual
        docente = self.buscar_por_id(docente_id)

        if docente is None:
            raise DocenteNoEncontradoError(docente_id)

        # Mantener valores actuales si no se envía un cambio
        especialidad = docente.especialidad if especialidad is None else especialidad
        id_persona = docente.id_persona if id_persona is None else id_persona


        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE docente
            SET
                especialidad = ?,
                id_persona = ?
            WHERE id_docente = ?
            """,
            (
                especialidad,
                id_persona,
                docente_id
            )
        )

        conn.commit()
        conn.close()

        return self.buscar_por_id(docente_id)

    # ==================================================
    # ELIMINAR
    # ==================================================

    def eliminar(self, docente_id):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM docente
            WHERE id_docente = ?
            """,
            (docente_id,)
        )

        conn.commit()

        if cursor.rowcount == 0:

            conn.close()

            raise DocenteNoEncontradoError(docente_id)

        conn.close()
