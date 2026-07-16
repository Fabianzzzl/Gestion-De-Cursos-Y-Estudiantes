# ==========================================
# DAO: MATRICULA
# Proyecto: Sistema de Gestión de Cursos y Estudiantes
# Descripción:
# Gestiona las operaciones CRUD de la entidad Matricula.
# ==========================================

from models.matricula import Matricula
from config.logger import Logger


# ==========================================
# Excepciones personalizadas
# ==========================================

class MatriculaNoEncontradaError(Exception):

    def __init__(self, matricula_id):
        super().__init__(f"Matrícula ID={matricula_id} no encontrada")


# ==========================================
# DAO Matricula
# ==========================================

class MatriculaDAO:

    # Constructor
    def __init__(self):

        self.__bd = []
        self.__cid = 1
        self.__log = Logger()

    # --------------------------------------
    # Insertar una nueva matrícula
    # --------------------------------------
    def insertar(self, matricula):

        matricula.id_matricula = self.__cid
        self.__cid += 1

        self.__bd.append(matricula)

        self.__log.info(
            f"Matrícula agregada: ID={matricula.id_matricula}"
        )

        return matricula

    # --------------------------------------
    # Buscar matrícula por ID
    # --------------------------------------
    def buscar_por_id(self, matricula_id):

        for m in self.__bd:

            if m.id_matricula == matricula_id:
                return m

        return None

    # --------------------------------------
    # Obtener todas las matrículas
    # --------------------------------------
    def obtener_todos(self):

        return sorted(
            self.__bd,
            key=lambda matricula: matricula.id_matricula
        )

    # --------------------------------------
    # Actualizar matrícula
    # --------------------------------------
    def actualizar(
        self,
        matricula_id,
        fecha_matricula=None,
        estado=None,
        id_alumno=None,
        id_curso=None
    ):

        m = self.buscar_por_id(matricula_id)

        if not m:

            self.__log.error(
                f"Actualizar fallido: Matrícula ID={matricula_id} no existe"
            )

            raise MatriculaNoEncontradaError(matricula_id)

        if fecha_matricula:
            m.fecha_matricula = fecha_matricula

        if estado:
            m.estado = estado

        if id_alumno is not None:
            m.id_alumno = id_alumno

        if id_curso is not None:
            m.id_curso = id_curso

        self.__log.info(
            f"Matrícula actualizada: ID={matricula_id}"
        )

        return m

    # --------------------------------------
    # Eliminar matrícula
    # --------------------------------------
    def eliminar(self, matricula_id):

        m = self.buscar_por_id(matricula_id)

        if not m:

            self.__log.error(
                f"Eliminar fallido: Matrícula ID={matricula_id} no existe"
            )

            raise MatriculaNoEncontradaError(matricula_id)

        self.__bd.remove(m)

        self.__log.info(
            f"Matrícula eliminada: ID={matricula_id}"
        )

        return True

    # --------------------------------------
    # Total de matrículas registradas
    # --------------------------------------
    def total(self):

        return len(self.__bd)