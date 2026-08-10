from fastapi import APIRouter, HTTPException
from Dao.persona_dao import (
    PersonaDAO,
    PersonaNoEncontradaError,
    DNIDuplicadoError,
    PersonaConRegistrosError
)
from models.persona import Persona
from schemas.persona_schema import (
    PersonaCrear,
    PersonaActualizar,
    PersonaRespuesta
)

router = APIRouter(
    prefix="/personas",
    tags=["Personas"]
)

dao = PersonaDAO()


@router.get("/", response_model=list[PersonaRespuesta])
def listar_personas():

    return [
        p.to_dict()
        for p in dao.obtener_todos()
    ]


@router.get("/{persona_id}", response_model=PersonaRespuesta)
def obtener_persona(persona_id: int):

    p = dao.buscar_por_id(persona_id)

    if not p:

        raise HTTPException(
            status_code=404,
            detail=f"Persona ID={persona_id} no encontrada"
        )

    return p.to_dict()


@router.post(
    "/",
    response_model=PersonaRespuesta,
    status_code=201
)
def crear_persona(datos: PersonaCrear):

    try:

        p = dao.insertar(
            Persona(
                0,
                datos.dni,
                datos.nombres,
                datos.apellidos,
                datos.telefono,
                datos.correo,
                datos.direccion
            )
        )

        return p.to_dict()

    except DNIDuplicadoError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )


@router.put(
    "/{persona_id}",
    response_model=PersonaRespuesta
)
def actualizar_persona(
    persona_id: int,
    datos: PersonaActualizar
):

    try:

        p = dao.actualizar(
            persona_id,
            datos.dni,
            datos.nombres,
            datos.apellidos,
            datos.telefono,
            datos.correo,
            datos.direccion
        )

        return p.to_dict()

    except PersonaNoEncontradaError as ex:

        raise HTTPException(
            status_code=404,
            detail=str(ex)
        )

    except DNIDuplicadoError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )


@router.delete("/{persona_id}")
def eliminar_persona(persona_id: int):

    try:

        dao.eliminar(persona_id)

        return {
            "mensaje": f"Persona ID={persona_id} eliminada"
        }

    except PersonaNoEncontradaError as ex:

        raise HTTPException(
            status_code=404,
            detail=str(ex)
        )

    except PersonaConRegistrosError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )
