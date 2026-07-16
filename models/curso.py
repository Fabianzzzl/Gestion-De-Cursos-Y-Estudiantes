class Curso:

    def __init__(self, id_curso=0, nombre="", descripcion="",
                 creditos=0, ciclo="", horas_semanales=0,
                 id_docente=0):

        self.__id_curso = id_curso
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__creditos = creditos
        self.__ciclo = ciclo
        self.__horas_semanales = horas_semanales
        self.__id_docente = id_docente

    @property
    def id_curso(self):
        return self.__id_curso

    @id_curso.setter
    def id_curso(self, valor):
        self.__id_curso = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self.__descripcion = valor

    @property
    def creditos(self):
        return self.__creditos

    @creditos.setter
    def creditos(self, valor):
        self.__creditos = valor

    @property
    def ciclo(self):
        return self.__ciclo

    @ciclo.setter
    def ciclo(self, valor):
        self.__ciclo = valor

    @property
    def horas_semanales(self):
        return self.__horas_semanales

    @horas_semanales.setter
    def horas_semanales(self, valor):
        self.__horas_semanales = valor

    @property
    def id_docente(self):
        return self.__id_docente

    @id_docente.setter
    def id_docente(self, valor):
        self.__id_docente = valor

    def __str__(self):
        return f"{self.__id_curso} - {self.__nombre} - {self.__descripcion} - {self.__creditos} - {self.__ciclo} - {self.__horas_semanales} - {self.__id_docente}"
    
    def to_dict(self):   
        return {
            "ID_Curso"        : self.__id_curso,
            "Nombre"          : self.__nombre,
            "Descripcion"     : self.__descripcion,
            "Creditos"        : self.__creditos,
            "Ciclo"           : self.__ciclo,
            "Horas Semanales" : self.__horas_semanales,     
            "ID_Docente"      : self.__id_docente,
        };
    
    @classmethod
    def from_dict(cls, datos):
        c = cls(datos["Nombre"], datos["Descripcion"], datos["Credito"], datos["Horas Semanales"], datos["ID_Docente"])
        c.id = datos["ID_Curso"]
        return c