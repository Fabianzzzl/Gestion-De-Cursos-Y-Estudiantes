from fastapi import APIRouter, HTTPException
from Dao.alumno_dao import (
    AlumnoDAO,
    AlumnoNoEncontradoError,
    CodigoAlumnoDuplicadoError,
    AlumnoConMatriculasError
)
from models.alumno import Alumno
from schemas.alumno_schema import (
    AlumnoCrear,
    AlumnoActualizar,
    AlumnoRespuesta
)

router = APIRouter(
    prefix="/alumnos",
    tags=["Alumnos"]
)

dao = AlumnoDAO()


@router.get("/", response_model=list[AlumnoRespuesta])
def listar_alumnos():

    return [
        a.to_dict()
        for a in dao.obtener_todos()
    ]


@router.get("/{alumno_id}", response_model=AlumnoRespuesta)
def obtener_alumno(alumno_id: int):

    a = dao.buscar_por_id(alumno_id)

    if not a:

        raise HTTPException(
            status_code=404,
            detail=f"Alumno ID={alumno_id} no encontrado"
        )

    return a.to_dict()


@router.post(
    "/",
    response_model=AlumnoRespuesta,
    status_code=201
)
def crear_alumno(datos: AlumnoCrear):

    try:

        a = dao.insertar(
            Alumno(
                0,
                datos.codigo_alumno,
                datos.id_persona,
                datos.id_distrito
            )
        )

        return a.to_dict()

    except CodigoAlumnoDuplicadoError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )


@router.put(
    "/{alumno_id}",
    response_model=AlumnoRespuesta
)
def actualizar_alumno(
    alumno_id: int,
    datos: AlumnoActualizar
):

    try:

        a = dao.actualizar(
            alumno_id,
            datos.codigo_alumno,
            datos.id_persona,
            datos.id_distrito
        )

        return a.to_dict()

    except AlumnoNoEncontradoError as ex:

        raise HTTPException(
            status_code=404,
            detail=str(ex)
        )

    except CodigoAlumnoDuplicadoError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )


@router.delete("/{alumno_id}")
def eliminar_alumno(alumno_id: int):

    try:

        dao.eliminar(alumno_id)

        return {
            "mensaje": f"Alumno ID={alumno_id} eliminado"
        }

    except AlumnoNoEncontradoError as ex:

        raise HTTPException(
            status_code=404,
            detail=str(ex)
        )

    except AlumnoConMatriculasError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )
