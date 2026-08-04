from config.base_datos import Inicializar
from config.sistema_config import SistemaConfig
from config.logger import Logger

from views.menu import (
    mostrar_menu,
    menu_personas,
    menu_distritos,
    menu_alumnos,
    menu_docentes,
    menu_cursos,
    menu_matriculas
)

from Dao.persona_dao import PersonaDAO
from Dao.distrito_dao import DistritoDAO
from Dao.alumno_dao import AlumnoDAO
from Dao.docente_dao import DocenteDAO
from Dao.cursos_dao import CursoDAO
from Dao.matricula_dao import MatriculaDAO


def main():
    
# Crea la base de datos y las tablas si todavía no existen.
    Inicializar()

    cfg = SistemaConfig()

    logger = Logger()

    logger.info("Sistema iniciado")

    pdao = PersonaDAO()
    ddao = DistritoDAO()
    adao = AlumnoDAO()
    dodao = DocenteDAO()
    cdao = CursoDAO()
    mdao = MatriculaDAO()

    while True:

        mostrar_menu(cfg)

        opcion = input("\nSeleccione una opción: ").strip()

        match opcion:

            case "1":
                menu_personas(pdao)

            case "2":
                menu_distritos(ddao)

            case "3":
                menu_alumnos(adao)

            case "4":
                menu_docentes(dodao)

            case "5":
                menu_cursos(cdao)

            case "6":
                menu_matriculas(mdao)

            case "7":
                logger.mostrar_logs()

            case "8":
                logger.limpiar()

            case "0":

                logger.info("Sistema finalizado")
                print("\nGracias por utilizar el sistema.")
                break

            case _:

                print("\nOpción no válida.")


if __name__ == "__main__":
    main()
