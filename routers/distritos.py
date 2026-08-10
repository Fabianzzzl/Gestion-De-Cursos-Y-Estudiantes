from fastapi import APIRouter, HTTPException
from Dao.distrito_dao import (
    DistritoDAO,
    DistritoNoEncontradoError,
    DistritoDuplicadoError
)
from models.distrito import Distrito
from schemas.distrito_schema import (
    DistritoCrear,
    DistritoActualizar,
    DistritoRespuesta
)

router = APIRouter(
    prefix="/distritos",
    tags=["Distritos"]
)
dao = DistritoDAO()

@router.get("/", response_model=list[DistritoRespuesta])
def listar_distritos():

    return [
        d.to_dict()
        for d in dao.obtener_todos()
    ]

@router.get("/{distrito_id}", response_model=DistritoRespuesta)
def obtener_distrito(distrito_id: int):

    d = dao.buscar_por_id(distrito_id)
    if not d:
        raise HTTPException(
            status_code=404,
            detail=f"Distrito ID={distrito_id} no encontrado"
        )
    return d.to_dict()

@router.post(
    "/",
    response_model=DistritoRespuesta,
    status_code=201
)
def crear_distrito(datos: DistritoCrear):

    try:

        d = dao.insertar(
            Distrito(
                0,
                datos.nombre
            )
        )
        return d.to_dict()

    except DistritoDuplicadoError as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )

@router.put(
    "/{distrito_id}",
    response_model=DistritoRespuesta
)
def actualizar_distrito(
    distrito_id: int,
    datos: DistritoActualizar
):

    try:
        d = dao.actualizar(
            distrito_id,
            datos.nombre
        )
        return d.to_dict()

    except DistritoNoEncontradoError as ex:
        raise HTTPException(
            status_code=404,
            detail=str(ex)
        )

    except DistritoDuplicadoError as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )


@router.delete("/{distrito_id}")
def eliminar_distrito(distrito_id: int):

    try:
        dao.eliminar(distrito_id)

        return {
            "mensaje": f"Distrito ID={distrito_id} eliminado"
        }

    except DistritoNoEncontradoError as ex:
        raise HTTPException(
            status_code=404,
            detail=str(ex)
        )
