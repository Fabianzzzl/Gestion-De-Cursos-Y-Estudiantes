from fastapi import APIRouter

from config.logger import Logger


router = APIRouter(
    prefix="/logs",
    tags=["Historial"]
)


# =========================================================
# OBTENER HISTORIAL
# =========================================================

@router.get("/")
def obtener_logs():

    return Logger().obtener_logs()


# =========================================================
# LIMPIAR HISTORIAL
# =========================================================

@router.delete("/")
def limpiar_logs():

    Logger().limpiar()

    return {
        "mensaje": "Historial de logs limpiado correctamente."
    }