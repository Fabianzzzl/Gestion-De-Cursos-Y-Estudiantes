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
        
    # ==================================================
    # BUSCAR POR ID
    # ==================================================

    def buscar_por_id(self, persona_id):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM persona
            WHERE id_persona = ?
            """,
            (persona_id,)
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

    # ==================================================
    # LISTAR
    # ==================================================

    def obtener_todos(self):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM persona
            ORDER BY nombres
            """
        )

        filas = cursor.fetchall()

        conn.close()

        return [

            Persona(

                fila["id_persona"],
                fila["dni"],
                fila["nombres"],
                fila["apellidos"],
                fila["telefono"],
                fila["correo"],
                fila["direccion"]

            )

            for fila in filas

        ]

    # ==================================================
    # ACTUALIZAR
    # ==================================================
    def actualizar(
        self,
        persona_id,
        dni=None,
        nombres=None,
        apellidos=None,
        telefono=None,
        correo=None,
        direccion=None
    ):

        # Buscar la persona existente
        persona = self.buscar_por_id(persona_id)

        # Mantener el valor actual si no se envía uno nuevo
        dni = persona.dni if dni is None else dni
        nombres = persona.nombres if nombres is None else nombres
        apellidos = persona.apellidos if apellidos is None else apellidos
        telefono = persona.telefono if telefono is None else telefono
        correo = persona.correo if correo is None else correo
        direccion = persona.direccion if direccion is None else direccion

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE persona
            SET
                dni = ?,
                nombres = ?,
                apellidos = ?,
                telefono = ?,
                correo = ?,
                direccion = ?
            WHERE id_persona = ?
            """,
            (
                dni,
                nombres,
                apellidos,
                telefono,
                correo,
                direccion,
                persona_id
            )
        )

        conn.commit()
        conn.close()

        return self.buscar_por_id(persona_id)

    # ==================================================
    # ELIMINAR
    # ==================================================

    def eliminar(self, persona_id):

        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM persona
            WHERE id_persona = ?
            """,
            (persona_id,)
        )

        conn.commit()

        if cursor.rowcount == 0:

            conn.close()

            raise PersonaNoEncontradaError(persona_id)

        conn.close()
