import json
import os
from models.persona import Persona
from models.distrito import Distrito
from models.alumno import Alumno
from models.docente import Docente
from models.curso import Curso
from models.matricula import Matricula

_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARCHIVO_PERSONA = os.path.join(_BASE, "datos_persona.js")
ARCHIVO_DISTRITO = os.path.join(_BASE, "datos_distrito.js")
ARCHIVO_ALUMNO = os.path.join(_BASE, "datos_alumno.js")
ARCHIVO_DOCENTE = os.path.join(_BASE, "datos_docente.js")
ARCHIVO_CURSO = os.path.join(_BASE, "datos_curso.js")
ARCHIVO_MATRICULA = os.path.join(_BASE, "datos_matricula.js")

def guardar_personas(pdao):
    datos = [p.to_dict() for p in pdao.obtener_todos()] 
    
    with open(ARCHIVO_PERSONA, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print(f"   OK Persona Guardados en {ARCHIVO_PERSONA}")
    
def cargar_persona(pdao):
    try:
        
        with open (ARCHIVO_PERSONA, "r", encoding="utf-8") as f:
            datos = json.load(f)
        for d in datos:
            persona = Persona.from_dict(d)
            pdao._PersonaDAO__bd.append(Persona)
            
            if persona.id >= pdao._PersonaDao__cid:
                pdao._PersonaDao__cid = persona.id + 1
        print(f"  OK{len(datos)} persona cargados desde {ARCHIVO_PERSONA}")
    except FileNotFoundError:
        print(f" AVISO: No existe '{ARCHIVO_PERSONA}', se empieza desde 0")
        
# ==========================================================
# DISTRITO
# ==========================================================

def guardar_distritos(ddao):

    datos = [d.to_dict() for d in ddao.obtener_todos()]

    with open(ARCHIVO_DISTRITO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    print(f"   OK Distritos guardados en {ARCHIVO_DISTRITO}")


def cargar_distritos(ddao):

    try:

        with open(ARCHIVO_DISTRITO, "r", encoding="utf-8") as f:
            datos = json.load(f)

        for d in datos:

            distrito = Distrito.from_dict(d)

            ddao._DistritoDAO__bd.append(distrito)

            if distrito.id_distrito >= ddao._DistritoDAO__cid:
                ddao._DistritoDAO__cid = distrito.id_distrito + 1

        print(f"  OK {len(datos)} distritos cargados desde {ARCHIVO_DISTRITO}")

    except FileNotFoundError:

        print(f" AVISO: No existe '{ARCHIVO_DISTRITO}', se empieza desde 0")


# ==========================================================
# ALUMNO
# ==========================================================

def guardar_alumnos(adao):

    datos = [a.to_dict() for a in adao.obtener_todos()]

    with open(ARCHIVO_ALUMNO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    print(f"   OK Alumnos guardados en {ARCHIVO_ALUMNO}")


def cargar_alumnos(adao):

    try:

        with open(ARCHIVO_ALUMNO, "r", encoding="utf-8") as f:
            datos = json.load(f)

        for d in datos:

            alumno = Alumno.from_dict(d)

            adao._AlumnoDAO__bd.append(alumno)

            if alumno.id_alumno >= adao._AlumnoDAO__cid:
                adao._AlumnoDAO__cid = alumno.id_alumno + 1

        print(f"  OK {len(datos)} alumnos cargados desde {ARCHIVO_ALUMNO}")

    except FileNotFoundError:

        print(f" AVISO: No existe '{ARCHIVO_ALUMNO}', se empieza desde 0")


# ==========================================================
# DOCENTE
# ==========================================================

def guardar_docentes(ddao):

    datos = [d.to_dict() for d in ddao.obtener_todos()]

    with open(ARCHIVO_DOCENTE, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    print(f"   OK Docentes guardados en {ARCHIVO_DOCENTE}")


def cargar_docentes(ddao):

    try:

        with open(ARCHIVO_DOCENTE, "r", encoding="utf-8") as f:
            datos = json.load(f)

        for d in datos:

            docente = Docente.from_dict(d)

            ddao._DocenteDAO__bd.append(docente)

            if docente.id_docente >= ddao._DocenteDAO__cid:
                ddao._DocenteDAO__cid = docente.id_docente + 1

        print(f"  OK {len(datos)} docentes cargados desde {ARCHIVO_DOCENTE}")

    except FileNotFoundError:

        print(f" AVISO: No existe '{ARCHIVO_DOCENTE}', se empieza desde 0")


# ==========================================================
# CURSO
# ==========================================================

def guardar_cursos(cdao):

    datos = [c.to_dict() for c in cdao.obtener_todos()]

    with open(ARCHIVO_CURSO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    print(f"   OK Cursos guardados en {ARCHIVO_CURSO}")


def cargar_cursos(cdao):

    try:

        with open(ARCHIVO_CURSO, "r", encoding="utf-8") as f:
            datos = json.load(f)

        for d in datos:

            curso = Curso.from_dict(d)

            cdao._CursoDAO__bd.append(curso)

            if curso.id_curso >= cdao._CursoDAO__cid:
                cdao._CursoDAO__cid = curso.id_curso + 1

        print(f"  OK {len(datos)} cursos cargados desde {ARCHIVO_CURSO}")

    except FileNotFoundError:

        print(f" AVISO: No existe '{ARCHIVO_CURSO}', se empieza desde 0")


# ==========================================================
# MATRÍCULA
# ==========================================================

def guardar_matriculas(mdao):

    datos = [m.to_dict() for m in mdao.obtener_todos()]

    with open(ARCHIVO_MATRICULA, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    print(f"   OK Matrículas guardadas en {ARCHIVO_MATRICULA}")


def cargar_matriculas(mdao):

    try:

        with open(ARCHIVO_MATRICULA, "r", encoding="utf-8") as f:
            datos = json.load(f)

        for d in datos:

            matricula = Matricula.from_dict(d)

            mdao._MatriculaDAO__bd.append(matricula)

            if matricula.id_matricula >= mdao._MatriculaDAO__cid:
                mdao._MatriculaDAO__cid = matricula.id_matricula + 1

        print(f"  OK {len(datos)} matrículas cargadas desde {ARCHIVO_MATRICULA}")

    except FileNotFoundError:

        print(f" AVISO: No existe '{ARCHIVO_MATRICULA}', se empieza desde 0")
        
# ==========================================================
# ALUMNO
# ==========================================================

def guardar_alumnos(adao):

    datos = [a.to_dict() for a in adao.obtener_todos()]

    with open(ARCHIVO_ALUMNO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    print(f"   OK Alumnos guardados en {ARCHIVO_ALUMNO}")


def cargar_alumnos(adao):

    try:

        with open(ARCHIVO_ALUMNO, "r", encoding="utf-8") as f:
            datos = json.load(f)

        for d in datos:

            alumno = Alumno.from_dict(d)

            adao._AlumnoDAO__bd.append(alumno)

            if alumno.id_alumno >= adao._AlumnoDAO__cid:
                adao._AlumnoDAO__cid = alumno.id_alumno + 1

        print(f"  OK {len(datos)} alumnos cargados desde {ARCHIVO_ALUMNO}")

    except FileNotFoundError:

        print(f" AVISO: No existe '{ARCHIVO_ALUMNO}', se empieza desde 0")
        
# ==========================================================
# DOCENTE
# ==========================================================

def guardar_docentes(ddao):

    datos = [do.to_dict() for do in ddao.obtener_todos()]

    with open(ARCHIVO_DOCENTE, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    print(f"   OK Docentes guardados en {ARCHIVO_DOCENTE}")


def cargar_docentes(ddao):

    try:

        with open(ARCHIVO_DOCENTE, "r", encoding="utf-8") as f:
            datos = json.load(f)

        for d in datos:

            docente = Docente.from_dict(d)

            ddao._DocenteDAO__bd.append(docente)

            if docente.id_docente >= ddao._DocenteDAO__cid:
                ddao._DocenteDAO__cid = docente.id_docente + 1

        print(f"  OK {len(datos)} docentes cargados desde {ARCHIVO_DOCENTE}")

    except FileNotFoundError:

        print(f" AVISO: No existe '{ARCHIVO_DOCENTE}', se empieza desde 0")


# ==========================================================
# CURSO
# ==========================================================

def guardar_cursos(cdao):

    datos = [c.to_dict() for c in cdao.obtener_todos()]

    with open(ARCHIVO_CURSO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    print(f"   OK Cursos guardados en {ARCHIVO_CURSO}")


def cargar_cursos(cdao):

    try:

        with open(ARCHIVO_CURSO, "r", encoding="utf-8") as f:
            datos = json.load(f)

        for d in datos:

            curso = Curso.from_dict(d)

            cdao._CursoDAO__bd.append(curso)

            if curso.id_curso >= cdao._CursoDAO__cid:
                cdao._CursoDAO__cid = curso.id_curso + 1

        print(f"  OK {len(datos)} cursos cargados desde {ARCHIVO_CURSO}")

    except FileNotFoundError:

        print(f" AVISO: No existe '{ARCHIVO_CURSO}', se empieza desde 0")


# ==========================================================
# MATRÍCULA
# ==========================================================

def guardar_matriculas(mdao):

    datos = [m.to_dict() for m in mdao.obtener_todos()]

    with open(ARCHIVO_MATRICULA, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    print(f"   OK Matrículas guardadas en {ARCHIVO_MATRICULA}")


def cargar_matriculas(mdao):

    try:

        with open(ARCHIVO_MATRICULA, "r", encoding="utf-8") as f:
            datos = json.load(f)

        for d in datos:

            matricula = Matricula.from_dict(d)

            mdao._MatriculaDAO__bd.append(matricula)

            if matricula.id_matricula >= mdao._MatriculaDAO__cid:
                mdao._MatriculaDAO__cid = matricula.id_matricula + 1

        print(f"  OK {len(datos)} matrículas cargadas desde {ARCHIVO_MATRICULA}")

    except FileNotFoundError:

        print(f" AVISO: No existe '{ARCHIVO_MATRICULA}', se empieza desde 0")