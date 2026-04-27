from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Jetpack API",
    version="0.1.0",
    description="Backend API for the Jetpack side-scrolling platform game.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/v1/status", tags=["system"])
def status() -> dict[str, str]:
    return {
        "name": "Jetpack",
        "stage": "project-initialized",
        "message": "Project structure is ready. Gameplay is not implemented yet.",
    }

