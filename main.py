from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.base_datos import Inicializar
from routers import (
    distritos,
    personas,
    alumnos,
    docentes,
    cursos,
    matriculas
)

# ==========================================
# APLICACIÓN FASTAPI
# ==========================================
app = FastAPI(
    title="Sistema de Gestión de Cursos y Estudiantes",
    description="API REST para la gestión de estudiantes, docentes, cursos y matrículas.",
    version="1.0.0"
)

# ==========================================
# CORS
# ==========================================
app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:3000"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


# ==========================================
# INICIALIZAR BASE DE DATOS
# ==========================================

Inicializar()


# ==========================================
# REGISTRAR ROUTERS
# ==========================================

app.include_router(distritos.router)
app.include_router(personas.router)
app.include_router(alumnos.router)
app.include_router(docentes.router)
app.include_router(cursos.router)
app.include_router(matriculas.router)


# ==========================================
# ENDPOINT PRINCIPAL
# ==========================================

@app.get("/")
def inicio():

    return {
        "mensaje": "API del Sistema de Gestión de Cursos y Estudiantes funcionando correctamente"
    }
