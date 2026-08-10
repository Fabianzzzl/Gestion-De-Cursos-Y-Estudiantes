from fastapi import APIRouter, HTTPException
from Dao.docente_dao import (
    DocenteDAO,
    DocenteNoEncontradoError,
    DocenteConCursosError
)
from models.docente import Docente
from schemas.docente_schema import (
    DocenteCrear,
    DocenteActualizar,
    DocenteRespuesta
)

router = APIRouter(
    prefix="/docentes",
    tags=["Docentes"]
)

dao = DocenteDAO()


@router.get("/", response_model=list[DocenteRespuesta])
def listar_docentes():

    return [
        d.to_dict()
        for d in dao.obtener_todos()
    ]


@router.get("/{docente_id}", response_model=DocenteRespuesta)
def obtener_docente(docente_id: int):

    d = dao.buscar_por_id(docente_id)

    if not d:

        raise HTTPException(
            status_code=404,
            detail=f"Docente ID={docente_id} no encontrado"
        )

    return d.to_dict()


@router.post(
    "/",
    response_model=DocenteRespuesta,
    status_code=201
)
def crear_docente(datos: DocenteCrear):

    d = dao.insertar(
        Docente(
            0,
            datos.especialidad,
            datos.id_persona
        )
    )

    return d.to_dict()


@router.put(
    "/{docente_id}",
    response_model=DocenteRespuesta
)
def actualizar_docente(
    docente_id: int,
    datos: DocenteActualizar
):

    try:

        d = dao.actualizar(
            docente_id,
            datos.especialidad,
            datos.id_persona
        )

        return d.to_dict()

    except DocenteNoEncontradoError as ex:

        raise HTTPException(
            status_code=404,
            detail=str(ex)
        )


@router.delete("/{docente_id}")
def eliminar_docente(docente_id: int):

    try:

        dao.eliminar(docente_id)

        return {
            "mensaje": f"Docente ID={docente_id} eliminado"
        }

    except DocenteNoEncontradoError as ex:

        raise HTTPException(
            status_code=404,
            detail=str(ex)
        )

    except DocenteConCursosError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )
