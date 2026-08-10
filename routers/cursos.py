from fastapi import APIRouter, HTTPException
from Dao.cursos_dao import (
    CursoDAO,
    CursoNoEncontradoError,
    CursoDuplicadoError,
    CursoConMatriculasError
)
from models.curso import Curso
from schemas.curso_schema import (
    CursoCrear,
    CursoActualizar,
    CursoRespuesta
)

router = APIRouter(
    prefix="/cursos",
    tags=["Cursos"]
)

dao = CursoDAO()


@router.get("/", response_model=list[CursoRespuesta])
def listar_cursos():

    return [
        c.to_dict()
        for c in dao.obtener_todos()
    ]


@router.get("/{curso_id}", response_model=CursoRespuesta)
def obtener_curso(curso_id: int):

    c = dao.buscar_por_id(curso_id)

    if not c:

        raise HTTPException(
            status_code=404,
            detail=f"Curso ID={curso_id} no encontrado"
        )

    return c.to_dict()


@router.post(
    "/",
    response_model=CursoRespuesta,
    status_code=201
)
def crear_curso(datos: CursoCrear):

    try:

        c = dao.insertar(
            Curso(
                0,
                datos.nombre,
                datos.descripcion,
                datos.creditos,
                datos.ciclo,
                datos.horas_semanales,
                datos.id_docente
            )
        )

        return c.to_dict()

    except CursoDuplicadoError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )


@router.put(
    "/{curso_id}",
    response_model=CursoRespuesta
)
def actualizar_curso(
    curso_id: int,
    datos: CursoActualizar
):

    try:

        c = dao.actualizar(
            curso_id,
            datos.nombre,
            datos.descripcion,
            datos.creditos,
            datos.ciclo,
            datos.horas_semanales,
            datos.id_docente
        )

        return c.to_dict()

    except CursoNoEncontradoError as ex:

        raise HTTPException(
            status_code=404,
            detail=str(ex)
        )

    except CursoDuplicadoError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )


@router.delete("/{curso_id}")
def eliminar_curso(curso_id: int):

    try:

        dao.eliminar(curso_id)

        return {
            "mensaje": f"Curso ID={curso_id} eliminado"
        }

    except CursoNoEncontradoError as ex:

        raise HTTPException(
            status_code=404,
            detail=str(ex)
        )

    except CursoConMatriculasError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )
