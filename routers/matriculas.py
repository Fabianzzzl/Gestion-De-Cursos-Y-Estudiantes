from fastapi import APIRouter, HTTPException
from Dao.matricula_dao import (
    MatriculaDAO,
    MatriculaNoEncontradaError,
    MatriculaDuplicadaError
)
from models.matricula import Matricula
from schemas.matricula_schema import (
    MatriculaCrear,
    MatriculaActualizar,
    MatriculaRespuesta
)
# ==========================================
# ROUTER
# ==========================================

router = APIRouter(
    prefix="/matriculas",
    tags=["Matrículas"]
)

dao = MatriculaDAO()

# ==========================================
# LISTAR MATRÍCULAS
# ==========================================

@router.get(
    "/",
    response_model=list[MatriculaRespuesta]
)
def listar_matriculas():

    return [
        m.to_dict()
        for m in dao.obtener_todos()
    ]

# ==========================================
# OBTENER MATRÍCULA POR ID
# ==========================================

@router.get(
    "/{matricula_id}",
    response_model=MatriculaRespuesta
)
def obtener_matricula(matricula_id: int):

    m = dao.buscar_por_id(matricula_id)

    if not m:

        raise HTTPException(
            status_code=404,
            detail=f"Matrícula ID={matricula_id} no encontrada"
        )

    return m.to_dict()

# ==========================================
# CREAR MATRÍCULA
# ==========================================

@router.post(
    "/",
    response_model=MatriculaRespuesta,
    status_code=201
)
def crear_matricula(datos: MatriculaCrear):

    try:

        m = Matricula(
            0,
            datos.fecha_matricula,
            datos.estado,
            datos.id_alumno,
            datos.id_curso
        )

        m = dao.insertar(m)

        return m.to_dict()

    except MatriculaDuplicadaError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )

    except Exception as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )
# ==========================================
# ACTUALIZAR MATRÍCULA
# ==========================================

@router.put(
    "/{matricula_id}",
    response_model=MatriculaRespuesta
)
def actualizar_matricula(
    matricula_id: int,
    datos: MatriculaActualizar
):

    try:

        m = dao.actualizar(
            matricula_id,
            datos.fecha_matricula,
            datos.estado,
            datos.id_alumno,
            datos.id_curso
        )

        return m.to_dict()

    except MatriculaNoEncontradaError as ex:

        raise HTTPException(
            status_code=404,
            detail=str(ex)
        )

    except MatriculaDuplicadaError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )

    except Exception as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )

# ==========================================
# ELIMINAR MATRÍCULA
# ==========================================

@router.delete(
    "/{matricula_id}"
)
def eliminar_matricula(matricula_id: int):

    try:

        dao.eliminar(matricula_id)

        return {
            "mensaje": f"Matrícula ID={matricula_id} eliminada"
        }

    except MatriculaNoEncontradaError as ex:

        raise HTTPException(
            status_code=404,
            detail=str(ex)
        )
