from fastapi import FastAPI

app = FastAPI(
    title="LiveMusicShare API"
)


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