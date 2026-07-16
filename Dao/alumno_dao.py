from models.alumno import Alumno
from config.logger import Logger


class AlumnoNoEncontradoError(Exception):

    def __init__(self, alumno_id):
        super().__init__(f"Alumno ID={alumno_id} no encontrado")


class CodigoAlumnoDuplicadoError(Exception):

    def __init__(self, codigo):
        super().__init__(f"Código '{codigo}' ya registrado")


class AlumnoDAO:

    def __init__(self):

        self.__bd = []
        self.__cid = 1
        self.__log = Logger()

    # Insertar
    def insertar(self, alumno):

        if self.buscar_por_codigo(alumno.codigo_alumno):

            self.__log.warning(
                f"Código duplicado: {alumno.codigo_alumno}"
            )

            raise CodigoAlumnoDuplicadoError(
                alumno.codigo_alumno
            )

        alumno.id_alumno = self.__cid
        self.__cid += 1

        self.__bd.append(alumno)

        self.__log.info(
            f"Alumno agregado ID={alumno.id_alumno}"
        )

        return alumno

    # Buscar por código
    def buscar_por_codigo(self, codigo):

        for a in self.__bd:

            if a.codigo_alumno == codigo:

                return a

        return None

    # Buscar por ID
    def buscar_por_id(self, alumno_id):

        for a in self.__bd:

            if a.id_alumno == alumno_id:

                return a

        return None

    # Listar
    def obtener_todos(self):

        return sorted(
            self.__bd,
            key=lambda alumno: alumno.codigo_alumno
        )

    # Actualizar
    def actualizar(
        self,
        alumno_id,
        codigo_alumno=None,
        id_persona=None,
        id_distrito=None
    ):

        a = self.buscar_por_id(alumno_id)

        if not a:

            raise AlumnoNoEncontradoError(alumno_id)

        if codigo_alumno:
            a.codigo_alumno = codigo_alumno

        if id_persona is not None:
            a.id_persona = id_persona

        if id_distrito is not None:
            a.id_distrito = id_distrito

        self.__log.info(
            f"Alumno actualizado ID={alumno_id}"
        )

        return a

    # Eliminar
    def eliminar(self, alumno_id):

        a = self.buscar_por_id(alumno_id)

        if not a:

            raise AlumnoNoEncontradoError(alumno_id)

        self.__bd.remove(a)

        self.__log.info(
            f"Alumno eliminado ID={alumno_id}"
        )

    # Total
    def total(self):

        return len(self.__bd)