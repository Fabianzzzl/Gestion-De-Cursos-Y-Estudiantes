import json
from config.logger import Logger
from models.persona import Persona
from models.distrito import Distrito
from models.alumno import Alumno
from models.docente import Docente
from models.curso import Curso
from models.matricula import Matricula
from Dao.persona_dao import PersonaNoEncontradaError,DNIDuplicadoError
from Dao.alumno_dao import AlumnoNoEncontradoError,CodigoAlumnoDuplicadoError
from Dao.docente_dao import DocenteNoEncontradoError
from Dao.cursos_dao import CursoNoEncontradoError
from Dao.matricula_dao import MatriculaNoEncontradaError
from Dao.distrito_dao import DistritoNoEncontradoError

# ==========================================================
# MENÚ
# ==========================================================

def mostrar_menu(cfg):

    print("\n" + "="*50)
    print(f"   {cfg.nombre} v{cfg.version}")
    print(f"   {cfg.empresa}")
    print("="*50)

    print("1. Personas")
    print("2. Distritos")
    print("3. Alumnos")
    print("4. Docentes")
    print("5. Cursos")
    print("6. Matrículas")
    print("7. Ver historial de logs")
    print("8. Limpiar historial de logs")
    print("0. Salir")

    print("="*50)


# ==========================================================
# PERSONA
# ==========================================================
def agregar_persona(pdao):

    print("\n--- REGISTRAR PERSONA ---")

    dni = input("DNI        : ")
    nombres = input("Nombres    : ")
    apellidos = input("Apellidos  : ")
    telefono = input("Teléfono   : ")
    correo = input("Correo     : ")
    direccion = input("Dirección  : ")

    try:

        p = pdao.insertar(
            Persona(
                0,
                dni,
                nombres,
                apellidos,
                telefono,
                correo,
                direccion
            )
        )

        print(f"OK Persona agregada ID={p.id_persona}")

    except DNIDuplicadoError as ex:

        print(f"ERROR: {ex}")


def listar_personas(pdao):

    print("\n--- PERSONAS ---")

    personas = pdao.obtener_todos()
    if personas:
        for p in personas:
            print(f" {p}")
    else:
        print("No existen personas registradas.")


def eliminar_persona(pdao):

    print("\n--- ELIMINAR PERSONA ---")

    try:

        id_persona = int(input("ID Persona: "))

        pdao.eliminar(id_persona)

        print("Persona eliminada correctamente.")

    except PersonaNoEncontradaError as ex:

        print(f"ERROR: {ex}")

    except ValueError:

        print("ERROR: El ID debe ser numérico.")


def actualizar_persona(pdao):

    print("\n--- ACTUALIZAR PERSONA ---")

    try:

        id_persona = int(input("ID Persona: "))
        
        dni = input("DNI (Enter=no cambiar): ").strip()
        nombres = input("Nombres (Enter=no cambiar): ").strip()
        apellidos = input("Apellidos (Enter=no cambiar): ").strip()
        telefono = input("Teléfono (Enter=no cambiar): ").strip()
        correo = input("Correo (Enter=no cambiar): ").strip()
        direccion = input("Dirección (Enter=no cambiar): ").strip()
        

        persona = pdao.actualizar(
            id_persona,
            dni or None,
            nombres or None,
            apellidos or None,
            telefono or None,
            correo or None,
            direccion or None
        )

        print(f"OK Persona actualizada: {persona}")

    except PersonaNoEncontradaError as ex:

        print(f"ERROR: {ex}")

    except ValueError:

        print("ERROR: El ID debe ser numérico.")
        
def menu_personas(pdao):

    while True:

        print("\n========================================")
        print("          MENÚ PERSONAS")
        print("========================================")
        print("1. Registrar Persona")
        print("2. Listar Personas")
        print("3. Actualizar Persona")
        print("4. Eliminar Persona")
        print("5. Ver Personas en JSON")
        print("0. Volver")
        print("========================================")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:

            case "1":
                agregar_persona(pdao)

            case "2":
                listar_personas(pdao)

            case "3":
                actualizar_persona(pdao)

            case "4":
                eliminar_persona(pdao)

            case "5":
                ver_personas_json(pdao)

            case "0":
                break

            case _:
                print("Opción no válida.")
