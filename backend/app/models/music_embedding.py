from sqlalchemy import Column, Integer

from pgvector.sqlalchemy import Vector

from app.database.session import Base


class MusicEmbedding(Base):

    __tablename__ = "music_embeddings"


    id = Column(
        Integer,
        primary_key=True
    )


    track_id = Column(
        Integer
    )


    embedding = Column(
        Vector(384)
    )