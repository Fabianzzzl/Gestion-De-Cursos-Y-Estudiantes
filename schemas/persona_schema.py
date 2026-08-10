import re
from pydantic import BaseModel, field_validator
from typing import Optional

class PersonaCrear(BaseModel):
    dni: str
    nombres: str
    apellidos: str
    telefono: Optional[str] = None
    correo: Optional[str] = None
    direccion: Optional[str] = None

    @field_validator("dni")
    @classmethod
    def validar_dni(cls, valor):
        if not re.fullmatch(r"\d{8}", valor):
            raise ValueError(
                "El DNI debe tener exactamente 8 dígitos numéricos"
            )
        return valor

class PersonaActualizar(BaseModel):
    dni: Optional[str] = None
    nombres: Optional[str] = None
    apellidos: Optional[str] = None
    telefono: Optional[str] = None
    correo: Optional[str] = None
    direccion: Optional[str] = None

    @field_validator("dni")
    @classmethod
    def validar_dni(cls, valor):
        if valor is not None and not re.fullmatch(
            r"\d{8}",
            valor
        ):
            raise ValueError(
                "El DNI debe tener exactamente 8 dígitos numéricos"
            )
        return valor

class PersonaRespuesta(BaseModel):
    id_persona: int
    dni: str
    nombres: str
    apellidos: str
    telefono: Optional[str] = None
    correo: Optional[str] = None
    direccion: Optional[str] = None
