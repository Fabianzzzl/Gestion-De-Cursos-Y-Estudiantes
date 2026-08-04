from models.persona import Persona
from config.base_datos import obtener_conexion


class PersonaNoEncontradaError(Exception):

    def __init__(self, persona_id):
        super().__init__(f"Persona ID={persona_id} no encontrada")


class DNIDuplicadoError(Exception):

    def __init__(self, dni):
        super().__init__(f"DNI '{dni}' ya registrado")


class PersonaDAO:

    # ==================================================
    # INSERTAR
    # ==================================================

    def insertar(self, persona):

        if self.buscar_por_dni(persona.dni):
            raise DNIDuplicadoError(persona.dni)

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO persona
            (dni,nombres,apellidos,telefono,correo,direccion)
            VALUES(?,?,?,?,?,?)
            """,
            (
                persona.dni,
                persona.nombres,
                persona.apellidos,
                persona.telefono,
                persona.correo,
                persona.direccion
            )
        )

        conn.commit()

        persona.id_persona = cursor.lastrowid

        conn.close()

        return persona

    # ==================================================
    # BUSCAR POR DNI
    # ==================================================

    def buscar_por_dni(self, dni):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM persona
            WHERE dni = ?
            """,
            (dni,)
        )

        fila = cursor.fetchone()

        conn.close()

        if fila:

            return Persona(

                fila["id_persona"],
                fila["dni"],
                fila["nombres"],
                fila["apellidos"],
                fila["telefono"],
                fila["correo"],
                fila["direccion"]

            )

        return None
