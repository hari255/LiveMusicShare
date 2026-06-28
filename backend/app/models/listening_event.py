from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from datetime import datetime

from app.database.session import Base


class ListeningEvent(Base):

    __tablename__ = "listening_events"


    id = Column(
        Integer,
        primary_key=True
    )


    user_id = Column(Integer)


    track_id = Column(Integer)


    location_bucket = Column(
        String
    )


    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )