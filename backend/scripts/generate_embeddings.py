from sentence_transformers import SentenceTransformer

from app.database.session import SessionLocal
from app.models.track import Track
from app.models.music_embedding import MusicEmbedding


def build_text(track):
    return f"{track.name} {track.artist} {track.genre}"


def run():
    db = SessionLocal()

    model = SentenceTransformer("all-MiniLM-L6-v2")

    tracks = db.query(Track).all()

    for t in tracks:
        text = build_text(t)
        embedding = model.encode(text).tolist()

        vec = MusicEmbedding(
            track_id=t.id,
            embedding=embedding
        )

        db.add(vec)

        print(f"Embedded: {t.name}")

    db.commit()
    db.close()

    print("All embeddings created 🎧")


if __name__ == "__main__":
    run()