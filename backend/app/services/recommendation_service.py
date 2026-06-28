from sqlalchemy import text
from app.database.session import SessionLocal


def get_similar_tracks(track_id: int, limit: int = 5):
    db = SessionLocal()

    query = text("""
        SELECT 
            t.id,
            t.name,
            t.artist,
            1 - (e1.embedding <=> e2.embedding) AS score
        FROM music_embeddings e1
        JOIN music_embeddings e2 ON e1.track_id != e2.track_id
        JOIN tracks t ON t.id = e2.track_id
        WHERE e1.track_id = :track_id
        ORDER BY e1.embedding <=> e2.embedding
        LIMIT :limit;
    """)

    result = db.execute(query, {
        "track_id": track_id,
        "limit": limit
    }).fetchall()

    db.close()

    return [
        {
            "track_id": r.id,
            "name": r.name,
            "artist": r.artist,
            "score": float(r.score)
        }
        for r in result
    ]