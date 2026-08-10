from fastapi import APIRouter

from config.logger import Logger


router = APIRouter(
    prefix="/logs",
    tags=["Historial"]
)


@router.get("/")
def obtener_logs():

    return Logger().obtener_logs()