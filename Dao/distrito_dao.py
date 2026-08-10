import psycopg2
from config.logger import Logger
from config.base_datos import obtener_conexion
from models.distrito import Distrito

# ==========================================
# EXCEPCIONES
# ==========================================

class DistritoNoEncontradoError(Exception):

    def __init__(self, distrito_id):

        super().__init__(
            f"Distrito ID={distrito_id} no encontrado"
        )


class DistritoDuplicadoError(Exception):

    def __init__(self, nombre):

        super().__init__(
            f"El distrito '{nombre}' ya está registrado"
        )


class DistritoConRegistrosError(Exception):

    def __init__(self, distrito_id):

        super().__init__(
            f"Distrito ID={distrito_id} no se puede eliminar: "
            f"tiene registros asociados"
        )


# ==========================================
# CLASE DISTRITO DAO
# ==========================================

class DistritoDAO:

    def __init__(self):

        self.__log = Logger()


    # ==========================================
    # INSERTAR
    # ==========================================

    def insertar(self, distrito):

        if self.buscar_por_nombre(distrito.nombre):

            self.__log.warning(
                f"Distrito duplicado: {distrito.nombre}"
            )

            raise DistritoDuplicadoError(
                distrito.nombre
            )

        conn = obtener_conexion()
        cursor = conn.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO distrito (nombre)
                VALUES (%s)
                RETURNING id_distrito
                """,
                (
                    distrito.nombre,
                )
            )

            fila = cursor.fetchone()

            conn.commit()

            distrito.id_distrito = fila["id_distrito"]

        except psycopg2.IntegrityError:

            conn.rollback()

            self.__log.warning(
                f"Distrito duplicado: {distrito.nombre}"
            )

            raise DistritoDuplicadoError(
                distrito.nombre
            )

        finally:

            cursor.close()
            conn.close()

        self.__log.info(
            f"Distrito agregado: {distrito.nombre} "
            f"(ID={distrito.id_distrito})"
        )

        return distrito


    # ==========================================
    # BUSCAR POR NOMBRE
    # ==========================================

    def buscar_por_nombre(self, nombre):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM distrito
            WHERE UPPER(nombre) = UPPER(%s)
            """,
            (
                nombre,
            )
        )

        fila = cursor.fetchone()

        cursor.close()
        conn.close()

        return (
            self.__fila_a_distrito(fila)
            if fila
            else None
        )


    # ==========================================
    # BUSCAR POR ID
    # ==========================================

    def buscar_por_id(self, distrito_id):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM distrito
            WHERE id_distrito = %s
            """,
            (
                distrito_id,
            )
        )

        fila = cursor.fetchone()

        cursor.close()
        conn.close()

        return (
            self.__fila_a_distrito(fila)
            if fila
            else None
        )
