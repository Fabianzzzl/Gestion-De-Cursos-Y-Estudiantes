class Matricula:

    def __init__(self, id_matricula=0,
                 fecha_matricula="",
                 estado="ACTIVO",
                 id_alumno=0,
                 id_curso=0):

        self.__id_matricula = id_matricula
        self.__fecha_matricula = fecha_matricula
        self.__estado = estado
        self.__id_alumno = id_alumno
        self.__id_curso = id_curso

    @property
    def id_matricula(self):
        return self.__id_matricula

    @id_matricula.setter
    def id_matricula(self, valor):
        self.__id_matricula = valor

    @property
    def fecha_matricula(self):
        return self.__fecha_matricula

    @fecha_matricula.setter
    def fecha_matricula(self, valor):
        self.__fecha_matricula = valor

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        self.__estado = valor

    @property
    def id_alumno(self):
        return self.__id_alumno

    @id_alumno.setter
    def id_alumno(self, valor):
        self.__id_alumno = valor

    @property
    def id_curso(self):
        return self.__id_curso

    @id_curso.setter
    def id_curso(self, valor):
        self.__id_curso = valor

    def __str__(self):
        return f"Matrícula {self.__id_matricula} - {self.__estado} - {self.__id_alumno} - {self.__id_curso}"
    
    def to_dict(self):
        return {
            "ID_Matricula": self.__id_matricula,
            "Fecha_Matricula": self.__fecha_matricula,
            "Estado": self.__estado,
            "ID_Alumno": self.__id_alumno,
            "ID_Curso": self.__id_curso,
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos.get("ID_Matricula", 0),
            datos.get("Fecha_Matricula", ""),
            datos.get("Estado", ""),
            datos.get("ID_Alumno", 0),
            datos.get("ID_Curso", 0)
        )
