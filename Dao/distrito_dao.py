from models.distrito import Distrito
from config.base_datos import obtener_conexion

class DistritoNoEncontradoError(Exception):
    def __init__(self, distrito_id):
        super().__init__(f"Distrito ID={distrito_id} no encontrado")


class DistritoDAO:
    # ==================================================
    # INSERTAR
    # ==================================================
    def insertar(self, distrito):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO distrito(nombre)
            VALUES(?)
            """,
            (
                distrito.nombre,
            )
        )

        conn.commit()

        distrito.id_distrito = cursor.lastrowid

        conn.close()

        return distrito
    # ==================================================
    # BUSCAR POR ID
    # ==================================================
    def buscar_por_id(self, distrito_id):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM distrito
            WHERE id_distrito = ?
            """,
            (
                distrito_id,
            )
        )

        fila = cursor.fetchone()

        conn.close()

        if fila:

            return Distrito(

                fila["id_distrito"],
                fila["nombre"]

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
            FROM distrito
            ORDER BY nombre
            """
        )

        filas = cursor.fetchall()

        conn.close()

        return [

            Distrito(

                fila["id_distrito"],
                fila["nombre"]

            )

            for fila in filas

        ]
    # ==================================================
    # ACTUALIZAR
    # ==================================================
    def actualizar(self, distrito_id, nombre):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE distrito
            SET nombre = ?
            WHERE id_distrito = ?
            """,
            (
                nombre,
                distrito_id
            )
        )

        conn.commit()

        if cursor.rowcount == 0:

            conn.close()

            raise DistritoNoEncontradoError(distrito_id)

        conn.close()

        return self.buscar_por_id(distrito_id)
    # ==================================================
    # ELIMINAR
    # ==================================================
    def eliminar(self, distrito_id):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM distrito
            WHERE id_distrito = ?
            """,
            (
                distrito_id,
            )
        )

        conn.commit()

        if cursor.rowcount == 0:

            conn.close()

            raise DistritoNoEncontradoError(distrito_id)

        conn.close()
