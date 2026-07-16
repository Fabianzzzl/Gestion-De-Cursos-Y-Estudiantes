# ==========================================
# DAO: DOCENTE
# Proyecto: Sistema de Gestión de Cursos y Estudiantes
# Descripción:
# Gestiona las operaciones CRUD de la entidad Docente.
# ==========================================

from models.docente import Docente
from config.logger import Logger


# ==========================================
# Excepciones personalizadas
# ==========================================

class DocenteNoEncontradoError(Exception):

    def __init__(self, docente_id):
        super().__init__(f"Docente ID={docente_id} no encontrado")


# ==========================================
# DAO Docente
# ==========================================

class DocenteDAO:

    # Constructor
    def __init__(self):

        self.__bd = []
        self.__cid = 1
        self.__log = Logger()

    # --------------------------------------
    # Insertar un nuevo docente
    # --------------------------------------
    def insertar(self, docente):

        docente.id_docente = self.__cid
        self.__cid += 1

        self.__bd.append(docente)

        self.__log.info(
            f"Docente agregado: Especialidad {docente.especialidad} (ID={docente.id_docente})"
        )

        return docente

    # --------------------------------------
    # Buscar docente por ID
    # --------------------------------------
    def buscar_por_id(self, docente_id):

        for do in self.__bd:

            if do.id_docente == docente_id:
                return do

        return None

    # --------------------------------------
    # Obtener todos los docentes
    # --------------------------------------
    def obtener_todos(self):

        return sorted(
            self.__bd,
            key=lambda docente: docente.especialidad
        )

    # --------------------------------------
    # Actualizar docente
    # --------------------------------------
    def actualizar(
        self,
        docente_id,
        especialidad=None,
        id_persona=None
    ):

        do = self.buscar_por_id(docente_id)

        if not do:

            self.__log.error(
                f"Actualizar fallido: Docente ID={docente_id} no existe"
            )

            raise DocenteNoEncontradoError(docente_id)

        if especialidad:
            do.especialidad = especialidad

        if id_persona:
            do.id_persona = id_persona

        self.__log.info(
            f"Docente actualizado: ID={docente_id}"
        )

        return do

    # --------------------------------------
    # Eliminar docente
    # --------------------------------------
    def eliminar(self, docente_id):

        do = self.buscar_por_id(docente_id)

        if not do:

            self.__log.error(
                f"Eliminar fallido: Docente ID={docente_id} no existe"
            )

            raise DocenteNoEncontradoError(docente_id)

        self.__bd.remove(do)

        self.__log.info(
            f"Docente eliminado: ID={docente_id}"
        )

        return True

    # --------------------------------------
    # Total de docentes registrados
    # --------------------------------------
    def total(self):

        return len(self.__bd)