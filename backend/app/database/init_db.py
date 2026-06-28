from app.database.session import engine
from app.database.session import Base


from app.models.user import User
from app.models.track import Track
from app.models.listening_event import ListeningEvent
from app.models.music_embedding import MusicEmbedding


Base.metadata.create_all(
    bind=engine
)


print("Database initialized")