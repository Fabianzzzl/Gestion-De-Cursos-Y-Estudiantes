# ==========================================
# MODELO: ALUMNO
# Proyecto: Sistema de Gestión de Cursos y Estudiantes
# ==========================================

class Alumno:

    # Constructor
    def __init__(self, codigo_alumno="", id_persona=0, id_distrito=0):

        self.__id_alumno = 0
        self.__codigo_alumno = codigo_alumno
        self.__id_persona = id_persona
        self.__id_distrito = id_distrito

    # Getter y Setter del ID
    @property
    def id_alumno(self):
        return self.__id_alumno

    @id_alumno.setter
    def id_alumno(self, valor):
        self.__id_alumno = valor

    # Getter y Setter del código
    @property
    def codigo_alumno(self):
        return self.__codigo_alumno

    @codigo_alumno.setter
    def codigo_alumno(self, valor):
        self.__codigo_alumno = valor

    # Getter y Setter de Persona
    @property
    def id_persona(self):
        return self.__id_persona

    @id_persona.setter
    def id_persona(self, valor):
        self.__id_persona = valor

    # Getter y Setter de Distrito
    @property
    def id_distrito(self):
        return self.__id_distrito

    @id_distrito.setter
    def id_distrito(self, valor):
        self.__id_distrito = valor

    # Representación en texto
    def __str__(self):

        return (
            f"ID:{self.__id_alumno} | "
            f"Código:{self.__codigo_alumno} | "
            f"Persona:{self.__id_persona} | "
            f"Distrito:{self.__id_distrito}"
        )
        
    def to_dict(self):   
        return {
            "ID"              : self.__id_alumno,
            "Código"          : self.__codigo_alumno,
            "ID_Persona"      : self.__id_persona,
            "ID_Distrito"     : self.__id_distrito,            
        };
        
    @classmethod
    def from_dict(cls, datos):
        a = cls(datos["Código"], datos["ID_Persona"], datos["ID_Distrito"])
        a.id = datos["ID_Alumno"]
        return a