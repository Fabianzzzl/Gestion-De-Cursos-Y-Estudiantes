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
# ==========================================================
# DOCENTE
# ==========================================================

def agregar_docente(dodao):

    print("\n--- AGREGAR DOCENTE ---")

    especialidad = input("  Especialidad : ")

    try:

        id_persona = int(input("  ID Persona   : "))

        d = dodao.insertar(

            Docente(
                0,
                especialidad,
                id_persona
            )

        )

        print(f"  OK Docente agregado con ID={d.id_docente}")

    except ValueError:

        print("  ERROR: El ID debe ser un número entero")


# ----------------------------------------------------------

def listar_docentes(dodao):

    print("\n--- DOCENTES ---")

    docentes = dodao.obtener_todos()

    if docentes:

        for d in docentes:

            print(f"  {d}")

    else:

        print("  (No hay docentes registrados)")


# ----------------------------------------------------------

def eliminar_docente(dodao):

    print("\n--- ELIMINAR DOCENTE ---")

    try:

        id_docente = int(input("  ID del docente a eliminar: "))

        dodao.eliminar(id_docente)

        print(f"  OK Docente ID={id_docente} eliminado")

    except DocenteNoEncontradoError as ex:

        print(f"  ERROR: {ex}")

    except ValueError:

        print("  ERROR: El ID debe ser un número entero")


# ----------------------------------------------------------

def actualizar_docente(dodao):

    print("\n--- ACTUALIZAR DOCENTE ---")

    try:

        id_docente = int(input("  ID del docente a actualizar: "))

        especialidad = input("  Nueva especialidad (Enter para no cambiar): ").strip()

        persona = input("  Nuevo ID Persona (Enter para no cambiar): ").strip()

        id_persona = int(persona) if persona else None

        d = dodao.actualizar(

            id_docente,

            especialidad or None,

            id_persona

        )

        print(f"  OK Docente actualizado: {d}")

    except DocenteNoEncontradoError as ex:

        print(f"  ERROR: {ex}")

    except ValueError:

        print("  ERROR: El ID debe ser un número entero")
        
def menu_docentes(dodao):

    while True:

        print("\n========================================")
        print("          MENÚ DOCENTES")
        print("========================================")
        print("1. Registrar Docente")
        print("2. Listar Docentes")
        print("3. Actualizar Docente")
        print("4. Eliminar Docente")
        print("5. Ver Docentes en JSON")
        print("0. Volver")
        print("========================================")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:

            case "1":
                agregar_docente(dodao)

            case "2":
                listar_docentes(dodao)

            case "3":
                actualizar_docente(dodao)

            case "4":
                eliminar_docente(dodao)

            case "5":
                ver_docentes_json(dodao)

            case "0":
                break

            case _:
                print("Opción no válida.")
# ==========================================================
# CURSO
# ==========================================================

def agregar_curso(cdao):

    print("\n--- AGREGAR CURSO ---")

    nombre = input("  Nombre              : ")
    descripcion = input("  Descripción         : ")

    try:

        creditos = int(input("  Créditos            : "))
        ciclo = input("  Ciclo               : ")
        horas = int(input("  Horas Semanales     : "))
        id_docente = int(input("  ID Docente          : "))

        c = cdao.insertar(

            Curso(
                0,
                nombre,
                descripcion,
                creditos,
                ciclo,
                horas,
                id_docente
            )

        )

        print(f"  OK Curso agregado con ID={c.id_curso}")

    except ValueError:

        print("  ERROR: Créditos, horas e ID Docente deben ser números enteros")


# ----------------------------------------------------------

def listar_cursos(cdao):

    print("\n--- CURSOS ---")

    cursos = cdao.obtener_todos()

    if cursos:

        for c in cursos:

            print(f"  {c}")

    else:

        print("  (No hay cursos registrados)")


# ----------------------------------------------------------

def eliminar_curso(cdao):

    print("\n--- ELIMINAR CURSO ---")

    try:

        id_curso = int(input("  ID del curso a eliminar: "))

        cdao.eliminar(id_curso)

        print(f"  OK Curso ID={id_curso} eliminado")

    except CursoNoEncontradoError as ex:

        print(f"  ERROR: {ex}")

    except ValueError:

        print("  ERROR: El ID debe ser un número entero")


# ----------------------------------------------------------

def actualizar_curso(cdao):

    print("\n--- ACTUALIZAR CURSO ---")

    try:

        id_curso = int(input("  ID del curso a actualizar: "))

        nombre = input("  Nuevo nombre (Enter para no cambiar): ").strip()
        descripcion = input("  Nueva descripción (Enter para no cambiar): ").strip()

        creditos = input("  Nuevos créditos (Enter para no cambiar): ").strip()
        ciclo = input("  Nuevo ciclo (Enter para no cambiar): ").strip()
        horas = input("  Nuevas horas semanales (Enter para no cambiar): ").strip()
        docente = input("  Nuevo ID Docente (Enter para no cambiar): ").strip()

        creditos = int(creditos) if creditos else None
        horas = int(horas) if horas else None
        id_docente = int(docente) if docente else None

        c = cdao.actualizar(

            id_curso,
            nombre or None,
            descripcion or None,
            creditos,
            ciclo or None,
            horas,
            id_docente

        )

        print(f"  OK Curso actualizado: {c}")

    except CursoNoEncontradoError as ex:

        print(f"  ERROR: {ex}")

    except ValueError:

        print("  ERROR: Créditos, horas e ID Docente deben ser números enteros")
        
def menu_cursos(cdao):

    while True:

        print("\n========================================")
        print("           MENÚ CURSOS")
        print("========================================")
        print("1. Registrar Curso")
        print("2. Listar Cursos")
        print("3. Actualizar Curso")
        print("4. Eliminar Curso")
        print("5. Ver Cursos en JSON")
        print("0. Volver")
        print("========================================")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:

            case "1":
                agregar_curso(cdao)

            case "2":
                listar_cursos(cdao)

            case "3":
                actualizar_curso(cdao)

            case "4":
                eliminar_curso(cdao)

            case "5":
                ver_cursos_json(cdao)

            case "0":
                break

            case _:
                print("Opción no válida.")
# ==========================================================
# MATRICULA
# ==========================================================   
def agregar_matricula(mdao):

    print("\n--- REGISTRAR MATRÍCULA ---")

    fecha_matricula = input("Fecha Matrícula (YYYY-MM-DD): ")
    estado = input(
        "Estado (ACTIVO/RETIRADO/FINALIZADO): "
    ).strip().upper()

    if estado not in ("ACTIVO", "RETIRADO", "FINALIZADO"):
        print("ERROR: Estado inválido.")
        return    
    id_alumno = int(input("ID Alumno: "))
    id_curso = int(input("ID Curso: "))

    try:

        m = mdao.insertar(

            Matricula(
                0,
                fecha_matricula,
                estado,
                id_alumno,
                id_curso
            )

        )

        print(f"OK Matrícula agregada ID={m.id_matricula}")

    except Exception as ex:

        print(f"ERROR: {ex}")
        
def listar_matriculas(mdao):

    print("\n--- MATRÍCULAS ---")

    matriculas = mdao.obtener_todos()

    if matriculas:

        for m in matriculas:

            print(m)

    else:

        print("No existen matrículas registradas.")
        
def eliminar_matricula(mdao):

    print("\n--- ELIMINAR MATRÍCULA ---")

    try:

        id_matricula = int(input("ID Matrícula: "))

        mdao.eliminar(id_matricula)

        print("Matrícula eliminada correctamente.")

    except MatriculaNoEncontradaError as ex:

        print(f"ERROR: {ex}")

    except ValueError:

        print("ERROR: El ID debe ser numérico.")

def actualizar_matricula(mdao):

    print("\n--- ACTUALIZAR MATRÍCULA ---")

    try:

        id_matricula = int(input("ID Matrícula: "))

        fecha_matricula = input(
            "Fecha Matrícula (Enter=no cambiar): "
        ).strip()

        estado = input(
            "Estado (ACTIVO/RETIRADO/FINALIZADO, Enter=no cambiar): "
        ).strip().upper()

        if estado and estado not in ("ACTIVO", "RETIRADO", "FINALIZADO"):
            print("ERROR: Estado inválido.")
            return

        id_alumno = input(
            "ID Alumno (Enter=no cambiar): "
        ).strip()

        id_curso = input(
            "ID Curso (Enter=no cambiar): "
        ).strip()

        matricula = mdao.actualizar(

            id_matricula,

            fecha_matricula or None,
            estado or None,
            int(id_alumno) if id_alumno else None,
            int(id_curso) if id_curso else None

        )

        print(f"OK Matrícula actualizada: {matricula}")

    except MatriculaNoEncontradaError as ex:

        print(f"ERROR: {ex}")

    except ValueError:

        print("ERROR: Los IDs deben ser numéricos.")
        
def menu_matriculas(mdao):

    while True:

        print("\n========================================")
        print("        MENÚ MATRÍCULAS")
        print("========================================")
        print("1. Registrar Matrícula")
        print("2. Listar Matrículas")
        print("3. Actualizar Matrícula")
        print("4. Eliminar Matrícula")
        print("5. Ver Matrículas en JSON")
        print("0. Volver")
        print("========================================")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:

            case "1":
                agregar_matricula(mdao)

            case "2":
                listar_matriculas(mdao)

            case "3":
                actualizar_matricula(mdao)

            case "4":
                eliminar_matricula(mdao)

            case "5":
                ver_matriculas_json(mdao)

            case "0":
                break

            case _:
                print("Opción no válida.")
# Json
# persona
def ver_personas_json(pdao):
    print("\-- PERSONAS EN JSON --")
    personas = pdao.obtener_todos()
    if personas:
        datos = [p.to_dict() for p in personas]
        print(json.dumps(datos, indent=4, ensure_ascii=False))
    else:
        print(" (No hay personas registradas)")
# distrito       
def ver_distrito_json(ddao):
    print("\-- DISTRITOS EN JSON --")
    distritos = ddao.obtener_todos()
    if distritos:
        datos = [d.to_dict() for d in distritos]
        print(json.dumps(datos, indent=4, ensure_ascii=False))
    else:
        print(" (No hay distritos registradas)")
# alumno
def ver_alumnos_json(adao):
    print("\-- ALUMNOS EN JSON --")
    alumnos = adao.obtener_todos()
    if alumnos:
        datos = [a.to_dict() for a in alumnos]
        print(json.dumps(datos, indent=4, ensure_ascii=False))
    else:
        print(" (No hay alumnos registradas)")
# docente
def ver_docentes_json(dodao):
    print("\-- DOCENTES EN JSON --")
    docentes = dodao.obtener_todos()
    if docentes:
        datos = [do.to_dict() for do in docentes]
        print(json.dumps(datos, indent=4, ensure_ascii=False))
    else:
        print(" (No hay docentes registradas)")
# curso
def ver_cursos_json(cdao):
    print("\-- CURSOS EN JSON --")
    cursos = cdao.obtener_todos()
    if cursos:
        datos = [c.to_dict() for c in cursos]
        print(json.dumps(datos, indent=4, ensure_ascii=False))
    else:
        print(" (No hay cursos registradas)")
# matricula
def ver_matriculas_json(mdao):
    print("\-- MATRICULAS EN JSON --")
    matriculas = mdao.obtener_todos()
    if matriculas:
        datos = [m.to_dict() for m in matriculas]
        print(json.dumps(datos, indent=4, ensure_ascii=False))
    else:
        print(" (No hay matriculas registradas)")
