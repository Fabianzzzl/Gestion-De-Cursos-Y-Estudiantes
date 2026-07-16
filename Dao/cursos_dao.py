# ==========================================
# DAO: CURSO
# Proyecto: Sistema de Gestión de Cursos y Estudiantes
# Descripción:
# Gestiona las operaciones CRUD de la entidad Curso.
# ==========================================

from models.curso import Curso
from config.logger import Logger


# ==========================================
# Excepciones personalizadas
# ==========================================

class CursoNoEncontradoError(Exception):

    def __init__(self, curso_id):
        super().__init__(f"Curso ID={curso_id} no encontrado")


class CursoDuplicadoError(Exception):

    def __init__(self, nombre):
        super().__init__(f"El curso '{nombre}' ya está registrado")


# ==========================================
# DAO Curso
# ==========================================

class CursoDAO:

    # Constructor
    def __init__(self):

        self.__bd = []
        self.__cid = 1
        self.__log = Logger()

    # --------------------------------------
    # Insertar un nuevo curso
    # --------------------------------------
    def insertar(self, curso):

        if self.buscar_por_nombre(curso.nombre):

            self.__log.warning(
                f"Curso duplicado: {curso.nombre}"
            )

            raise CursoDuplicadoError(curso.nombre)

        curso.id_curso = self.__cid
        self.__cid += 1

        self.__bd.append(curso)

        self.__log.info(
            f"Curso agregado: {curso.nombre} (ID={curso.id_curso})"
        )

        return curso

    # --------------------------------------
    # Buscar curso por nombre
    # --------------------------------------
    def buscar_por_nombre(self, nombre):

        for c in self.__bd:

            if c.nombre.upper() == nombre.upper():
                return c
        return None

    # --------------------------------------
    # Buscar curso por ID
    # --------------------------------------
    def buscar_por_id(self, curso_id):

        for c in self.__bd:

            if c.id_curso == curso_id:
                return c

        return None

    # --------------------------------------
    # Obtener todos los cursos
    # --------------------------------------
    def obtener_todos(self):

        return sorted(
            self.__bd,
            key=lambda curso: curso.nombre
        )

    # --------------------------------------
    # Actualizar un curso
    # --------------------------------------
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

        c = self.buscar_por_id(curso_id)

        if not c:

            self.__log.error(
                f"Actualizar fallido: Curso ID={curso_id} no existe"
            )

            raise CursoNoEncontradoError(curso_id)

        if nombre:
            c.nombre = nombre

        if descripcion:
            c.descripcion = descripcion

        if creditos is not None:
            c.creditos = creditos

        if ciclo:
            c.ciclo = ciclo

        if horas_semanales is not None:
            c.horas_semanales = horas_semanales

        if id_docente is not None:
            c.id_docente = id_docente

        self.__log.info(
            f"Curso actualizado: ID={curso_id}"
        )

        return c

    # --------------------------------------
    # Eliminar un curso
    # --------------------------------------
    def eliminar(self, curso_id):

        c = self.buscar_por_id(curso_id)

        if not c:

            self.__log.error(
                f"Eliminar fallido: Curso ID={curso_id} no existe"
            )

            raise CursoNoEncontradoError(curso_id)

        self.__bd.remove(c)

        self.__log.info(
            f"Curso eliminado: {c.nombre} (ID={curso_id})"
        )

        return True

    # --------------------------------------
    # Total de cursos registrados
    # --------------------------------------
    def total(self):

        return len(self.__bd)