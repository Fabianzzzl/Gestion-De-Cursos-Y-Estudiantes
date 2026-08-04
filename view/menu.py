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
# ==========================================================
# DISTRITO
# ==========================================================

def agregar_distrito(ddao):

    print("\n--- REGISTRAR DISTRITO ---")

    nombre = input("Nombre del distrito: ")

    try:

        distrito = Distrito(

            0,

            nombre

        )

        distrito = ddao.insertar(distrito)

        print(f"\nDistrito registrado con ID={distrito.id_distrito}")

    except Exception as ex:

        print(f"\nERROR: {ex}")


# ----------------------------------------------------------

def listar_distritos(ddao):

    print("\n--- DISTRITOS ---")

    distritos = ddao.obtener_todos()

    if distritos:

        for d in distritos:

            print(f"  {d}")

    else:

        print("  (No hay distritos registrados)")


# ----------------------------------------------------------

def eliminar_distrito(ddao):

    print("\n--- ELIMINAR DISTRITO ---")

    try:

        id_distrito = int(input("  ID del distrito a eliminar: "))

        ddao.eliminar(id_distrito)

        print(f"  OK Distrito ID={id_distrito} eliminado")

    except DistritoNoEncontradoError as ex:

        print(f"  ERROR: {ex}")

    except ValueError:

        print("  ERROR: El ID debe ser un número entero")


# ----------------------------------------------------------

def actualizar_distrito(ddao):

    print("\n--- ACTUALIZAR DISTRITO ---")

    try:

        id_distrito = int(input("  ID del distrito a actualizar: "))

        nombre = input("  Nuevo nombre (Enter para no cambiar): ").strip()

        d = ddao.actualizar(
            id_distrito,
            nombre or None
        )

        print(f"  OK Distrito actualizado: {d}")

    except DistritoNoEncontradoError as ex:

        print(f"  ERROR: {ex}")

    except ValueError:

        print("  ERROR: El ID debe ser un número entero")
        
def menu_distritos(ddao):

    while True:

        print("\n========================================")
        print("         MENÚ DISTRITOS")
        print("========================================")
        print("1. Registrar Distrito")
        print("2. Listar Distritos")
        print("3. Actualizar Distrito")
        print("4. Eliminar Distrito")
        print("5. Ver Distritos en JSON")
        print("0. Volver")
        print("========================================")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:

            case "1":
                agregar_distrito(ddao)

            case "2":
                listar_distritos(ddao)

            case "3":
                actualizar_distrito(ddao)

            case "4":
                eliminar_distrito(ddao)

            case "5":
                ver_distrito_json(ddao)

            case "0":
                break

            case _:
                print("Opción no válida.")
# ==========================================================
# ALUMNO
# ==========================================================

def agregar_alumno(adao):

    print("\n--- AGREGAR ALUMNO ---")

    codigo = input("  Código Alumno : ")

    try:

        id_persona = int(input("  ID Persona   : "))
        id_distrito = int(input("  ID Distrito  : "))

        a = adao.insertar(

            Alumno(
                0,
                codigo,
                id_persona,
                id_distrito
            )

        )

        print(f"  OK Alumno agregado con ID={a.id_alumno}")

    except CodigoAlumnoDuplicadoError as ex:

        print(f"  ERROR: {ex}")

    except ValueError:

        print("  ERROR: Los ID deben ser números enteros")


# ----------------------------------------------------------

def listar_alumnos(adao):

    print("\n--- ALUMNOS ---")

    alumnos = adao.obtener_todos()

    if alumnos:

        for a in alumnos:

            print(f"  {a}")

    else:

        print("  (No hay alumnos registrados)")


# ----------------------------------------------------------

def eliminar_alumno(adao):

    print("\n--- ELIMINAR ALUMNO ---")

    try:

        alumno_id = int(input("  ID del alumno a eliminar: "))

        adao.eliminar(alumno_id)

        print(f"  OK Alumno ID={alumno_id} eliminado")

    except AlumnoNoEncontradoError as ex:

        print(f"  ERROR: {ex}")

    except ValueError:

        print("  ERROR: El ID debe ser un número entero")


# ----------------------------------------------------------

def actualizar_alumno(adao):

    print("\n--- ACTUALIZAR ALUMNO ---")

    try:

        alumno_id = int(input("  ID del alumno a actualizar: "))

        codigo = input("  Nuevo código (Enter para no cambiar): ").strip()

        persona = input("  Nuevo ID Persona (Enter para no cambiar): ").strip()

        distrito = input("  Nuevo ID Distrito (Enter para no cambiar): ").strip()

        id_persona = int(persona) if persona else None
        id_distrito = int(distrito) if distrito else None

        a = adao.actualizar(

            alumno_id,
            codigo or None,
            id_persona,
            id_distrito

        )

        print(f"  OK Alumno actualizado: {a}")

    except AlumnoNoEncontradoError as ex:

        print(f"  ERROR: {ex}")

    except ValueError:

        print("  ERROR: El ID debe ser un número entero")
        
def menu_alumnos(adao):

    while True:

        print("\n========================================")
        print("          MENÚ ALUMNOS")
        print("========================================")
        print("1. Registrar Alumno")
        print("2. Listar Alumnos")
        print("3. Actualizar Alumno")
        print("4. Eliminar Alumno")
        print("5. Ver Alumnos en JSON")
        print("0. Volver")
        print("========================================")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:

            case "1":
                agregar_alumno(adao)

            case "2":
                listar_alumnos(adao)

            case "3":
                actualizar_alumno(adao)

            case "4":
                eliminar_alumno(adao)

            case "5":
                ver_alumnos_json(adao)

            case "0":
                break

            case _:
                print("Opción no válida.")
