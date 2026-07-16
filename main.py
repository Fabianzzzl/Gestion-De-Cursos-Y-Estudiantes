# ==========================================
# MAIN
# Sistema de Gestión de Cursos y Estudiantes
# ==========================================
from config.sistema_config import SistemaConfig
from config.logger import Logger

from Dao.persona_dao import PersonaDAO
from Dao.distrito_dao import DistritoDAO
from Dao.alumno_dao import AlumnoDAO
from Dao.docente_dao import DocenteDAO
from Dao.cursos_dao import CursoDAO
from Dao.matricula_dao import MatriculaDAO

from config.persistencia import (guardar_personas,guardar_alumnos,guardar_distritos,guardar_matriculas,guardar_docentes,guardar_cursos,cargar_persona,cargar_distritos,cargar_cursos,cargar_matriculas,cargar_docentes,cargar_alumnos)
from views.menu import (mostrar_menu,agregar_persona,agregar_distrito,agregar_alumno,agregar_docente,agregar_curso,agregar_matricula,listar_personas,listar_alumnos,listar_cursos,listar_docentes,listar_distritos,listar_matriculas,eliminar_persona,eliminar_distrito,eliminar_alumno,eliminar_docente,eliminar_curso,eliminar_matricula,actualizar_persona,actualizar_distrito,actualizar_alumno,actualizar_docente,actualizar_curso,actualizar_matricula,ver_cursos_json,ver_distrito_json,ver_alumnos_json,ver_docentes_json,ver_matriculas_json,ver_personas_json,guardar_alumnos,guardar_cursos,guardar_distritos,guardar_docentes,guardar_matriculas,guardar_personas)

def main():
    
    cfg   = SistemaConfig()
    pdao  = PersonaDAO()
    ddao  = DistritoDAO()
    adao  = AlumnoDAO()
    dodao = DocenteDAO()
    cdao  = CursoDAO()
    mdao  = MatriculaDAO()

    while True:

        mostrar_menu(cfg)
        opcion = input("  Elige una opción: ").strip() 

        match opcion:

            case "1":
                agregar_persona(pdao)
            case "2":
                agregar_distrito(ddao)
            case "3":
                agregar_alumno(adao)
            case "4":
                agregar_docente(dodao)
            case "5":
                agregar_curso(cdao)
            case "6":
                agregar_matricula(mdao)
            # LISTAR
            case "7":
                listar_personas(pdao)
            case "8":
                listar_distritos(ddao)
            case "9":
                listar_alumnos(adao)
            case "10":
                listar_docentes(dodao)
            case "11":
                listar_cursos(cdao)
            case "12":
                listar_matriculas(mdao)
            # ELIMINAR
            case "13":
                eliminar_persona(pdao)
            case "14":
                eliminar_distrito(ddao)
            case "15":
                eliminar_alumno(adao)
            case "16":
                eliminar_docente(dodao)
            case "17":
                eliminar_curso(cdao)
            case "18":
                eliminar_matricula(mdao)
            # ACTUALIZAR
            case "19":
                actualizar_persona(pdao)
            case "20":
                actualizar_distrito(ddao)
            case "21":
                actualizar_alumno(adao)
            case "22":
                actualizar_docente(dodao)
            case "23":
                actualizar_curso(cdao)
            case "24":
                actualizar_matricula(mdao)
            case "25":
                ver_personas_json(pdao)
            case "26":
                ver_distrito_json(ddao)
            case "27":
                ver_alumnos_json(adao)
            case "28":
                ver_docentes_json(dodao)
            case "29":
                ver_cursos_json(cdao)
            case "30":
                ver_matriculas_json(mdao)
            case "31":
                guardar_personas(pdao), guardar_distritos(ddao), guardar_alumnos(adao), guardar_docentes(dodao), guardar_cursos(cdao), guardar_matriculas(mdao)
            # LOGS
            case "32":
                Logger().mostrar_logs()
            case "33":
                Logger().limpiar()
            case "0":
                
                guardar_personas(pdao), guardar_distritos(ddao), guardar_alumnos(adao), guardar_docentes(dodao), guardar_cursos(cdao), guardar_matriculas(mdao)

                print("\nGracias por utilizar el sistema.")
                break

            case _:

                print("\nOpción inválida, elige entre 0 y 26")


main()