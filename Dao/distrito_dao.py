# ==========================================
# DAO: DISTRITO
# Proyecto: Sistema de Gestión de Cursos y Estudiantes
# Descripción:
# Gestiona las operaciones CRUD de la entidad Distrito.
# ==========================================

from models.distrito import Distrito
from config.logger import Logger


# ==========================================
# Excepción personalizada
# ==========================================

class DistritoNoEncontradoError(Exception):

    def __init__(self, distrito_id):
        super().__init__(f"Distrito ID={distrito_id} no encontrado")


class DistritoDuplicadoError(Exception):

    def __init__(self, nombre):
        super().__init__(f"El distrito '{nombre}' ya está registrado")


# ==========================================
# DAO Distrito
# ==========================================

class DistritoDAO:

    # Constructor
    def __init__(self):
        self.__bd = []
        self.__cid = 1
        self.__log = Logger()

    # --------------------------------------
    # Insertar un nuevo distrito
    # --------------------------------------
    def insertar(self, distrito):

        if self.buscar_por_nombre(distrito.nombre):
            self.__log.warning(f"Distrito duplicado: {distrito.nombre}")
            raise DistritoDuplicadoError(distrito.nombre)

        distrito.id_distrito = self.__cid
        self.__cid += 1

        self.__bd.append(distrito)

        self.__log.info(
            f"Distrito agregado: {distrito.nombre} (ID={distrito.id_distrito})"
        )

        return distrito

    # --------------------------------------
    # Buscar distrito por nombre
    # --------------------------------------
    def buscar_por_nombre(self, nombre):

        for d in self.__bd:
            if d.nombre.upper() == nombre.upper():
                return d

        return None

    # --------------------------------------
    # Buscar distrito por ID
    # --------------------------------------
    def buscar_por_id(self, distrito_id):

        for d in self.__bd:
            if d.id_distrito == distrito_id:
                return d

        return None

    # --------------------------------------
    # Obtener todos los distritos
    # --------------------------------------
    def obtener_todos(self):

        return sorted(self.__bd, key=lambda distrito: distrito.nombre)

    # --------------------------------------
    # Actualizar un distrito
    # --------------------------------------
    def actualizar(self, distrito_id, nombre=None):

        d = self.buscar_por_id(distrito_id)

        if not d:
            self.__log.error(
                f"Actualizar fallido: Distrito ID={distrito_id} no existe"
            )
            raise DistritoNoEncontradoError(distrito_id)

        if nombre:
            d.nombre = nombre

        self.__log.info(f"Distrito actualizado: ID={distrito_id}")

        return d

    # --------------------------------------
    # Eliminar un distrito
    # --------------------------------------
    def eliminar(self, distrito_id):

        d = self.buscar_por_id(distrito_id)

        if not d:
            self.__log.error(
                f"Eliminar fallido: Distrito ID={distrito_id} no existe"
            )
            raise DistritoNoEncontradoError(distrito_id)

        self.__bd.remove(d)

        self.__log.info(
            f"Distrito eliminado: {d.nombre} (ID={distrito_id})"
        )

        return True

    # --------------------------------------
    # Total de distritos registrados
    # --------------------------------------
    def total(self):
        return len(self.__bd)