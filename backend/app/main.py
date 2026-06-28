from fastapi import FastAPI
from app.api.routes.discovery import router as discovery_router

app = FastAPI(
    title="LiveMusicShare API"
)

# register routers AFTER app is created
app.include_router(discovery_router)


@app.get("/")
def root():
    return {
        "message": "LiveMusicShare API running 🎧"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }