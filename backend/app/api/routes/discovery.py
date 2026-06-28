from fastapi import APIRouter
from app.services.recommendation_service import get_similar_tracks

router = APIRouter()


@router.get("/discover/similar/{track_id}")
def similar_tracks(track_id: int):
    return {
        "track_id": track_id,
        "recommendations": get_similar_tracks(track_id)
    }