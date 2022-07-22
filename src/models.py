from sqlalchemy import Column, ForeignKey, Integer, String, CheckConstraint
from sqlalchemy.orm import relationship
from .database import Base

class Artist(Base):
    __tablename__ = "artists"
    id = Column(Integer, primary_key=True, index=True)
    artistName = Column(String)
    country = Column(String)
    
    releases = relationship("Release", back_populates="artist")


class Release(Base):
    __tablename__ = "releases"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    releaseType = Column(String)
    year = Column(Integer)
    genre = Column(String)
    artist_id = Column(Integer, ForeignKey("artists.id"))
    release_id = Column(Integer, ForeignKey("labels.id"))

    artist = relationship("Artist", back_populates="releases")
    label = relationship("Label", back_populates="releases")
    # CheckConstraint("year > 0", name="check1")
    # CheckConstraint("year < 10000", name="check2")

class Label(Base):
    __tablename__ = "labels"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    releases = relationship("Release", back_populates="label")