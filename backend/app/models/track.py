from sqlalchemy import Column, Integer, String

from app.database.session import Base


class Track(Base):

    __tablename__ = "tracks"


    id = Column(
        Integer,
        primary_key=True
    )


    name = Column(String)

    artist = Column(String)

    genre = Column(String)