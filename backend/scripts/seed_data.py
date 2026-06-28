from datetime import datetime
import random

from app.database.session import SessionLocal
from app.models.user import User
from app.models.track import Track
from app.models.listening_event import ListeningEvent


def seed():
    db = SessionLocal()

    # -------------------
    # USERS
    # -------------------
    users = [
        "techno_nomad",
        "neon_rider",
        "bass_seeker",
        "synth_wanderer",
        "audio_hunter"
    ]

    user_objs = []
    for u in users:
        obj = User(username=u)
        db.add(obj)
        user_objs.append(obj)

    db.commit()

    # -------------------
    # TRACKS
    # -------------------
    tracks_data = [
        ("Yellow Lambo", "Indira Paganotto", "Techno"),
        ("Space Drift", "Carbon Based Lifeforms", "Ambient Techno"),
        ("Neon Ritual", "HI-LO", "Psy Trance"),
        ("Deep Signal", "Charlotte de Witte", "Minimal Techno"),
        ("Quantum Bass", "Reinier Zonneveld", "Industrial Techno"),
    ]

    track_objs = []
    for name, artist, genre in tracks_data:
        t = Track(name=name, artist=artist, genre=genre)
        db.add(t)
        track_objs.append(t)

    db.commit()

    # -------------------
    # LISTENING EVENTS
    # -------------------
    for _ in range(50):

        user = random.choice(user_objs)
        track = random.choice(track_objs)

        event = ListeningEvent(
            user_id=user.id,
            track_id=track.id,
            location_bucket=random.choice([
                "sf_downtown",
                "nyc_manhattan",
                "berlin_centre",
                "bangalore_indiranagar"
            ]),
            timestamp=datetime.utcnow()
        )

        db.add(event)

    db.commit()

    db.close()

    print("Seed data inserted 🎧")


if __name__ == "__main__":
    seed()