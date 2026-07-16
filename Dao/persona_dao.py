# ==========================================
# DAO: PERSONA
# Proyecto: Sistema de Gestión de Cursos y Estudiantes
# Descripción:
# Gestiona las operaciones CRUD de la entidad Persona.
# ==========================================

from models.persona import Persona
from config.logger import Logger


# ==========================================
# Excepción personalizada
# ==========================================

class PersonaNoEncontradaError(Exception):

    def __init__(self, persona_id):
        super().__init__(f"Persona ID={persona_id} no encontrada")


class DNIDuplicadoError(Exception):

    def __init__(self, dni):
        super().__init__(f"DNI '{dni}' ya registrado")


# ==========================================
# DAO Persona
# ==========================================

class PersonaDAO:

    # Constructor
    def __init__(self):
        self.__bd = []
        self.__cid = 1
        self.__log = Logger()

    # --------------------------------------
    # Insertar una nueva persona
    # --------------------------------------
    def insertar(self, persona):

        if self.buscar_por_dni(persona.dni):
            self.__log.warning(f"DNI duplicado: {persona.dni}")
            raise DNIDuplicadoError(persona.dni)

        persona.id_persona = self.__cid
        self.__cid += 1
        self.__bd.append(persona)
        self.__log.info(f"Persona agregada: {persona.nombres} {persona.apellidos} (ID={persona.id_persona})")
        return persona

    # --------------------------------------
    # Buscar persona por DNI
    # --------------------------------------
    def buscar_por_dni(self, dni):

        for p in self.__bd:
            if p.dni == dni:
                return p

        return None

    # --------------------------------------
    # Buscar persona por ID
    # --------------------------------------
    def buscar_por_id(self, persona_id):

        for p in self.__bd:
            if p.id_persona == persona_id:
                return p
        return None

    # --------------------------------------
    # Obtener todas las personas
    # --------------------------------------
    def obtener_todos(self):

        return sorted(self.__bd, key=lambda persona: persona.nombres)

    # --------------------------------------
    # Actualizar datos de una persona
    # --------------------------------------
    def actualizar(
        self,
        persona_id,
        nombres=None,
        apellidos=None,
        telefono=None,
        correo=None,
        direccion=None
    ):

        p = self.buscar_por_id(persona_id)

        if not p:
            self.__log.error(
                f"Actualizar fallido: Persona ID={persona_id} no existe"
            )
            raise PersonaNoEncontradaError(persona_id)

        if nombres:
            p.nombres = nombres

        if apellidos:
            p.apellidos = apellidos

        if telefono:
            p.telefono = telefono

        if correo:
            p.correo = correo

        if direccion:
            p.direccion = direccion

        self.__log.info(f"Persona actualizada: ID={persona_id}")

        return p

    # --------------------------------------
    # Eliminar persona
    # --------------------------------------
    def eliminar(self, persona_id):

        p = self.buscar_por_id(persona_id)

        if not p:
            self.__log.error(
                f"Eliminar fallido: Persona ID={persona_id} no existe"
            )
            raise PersonaNoEncontradaError(persona_id)

        self.__bd.remove(p)

        self.__log.info(
            f"Persona eliminada: {p.nombres} {p.apellidos}"
        )

        return True

    # --------------------------------------
    # Total de personas registradas
    # --------------------------------------
    def total(self):
        return len(self.__bd)