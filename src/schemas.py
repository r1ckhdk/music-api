from typing import List
from pydantic import BaseModel
from .database import Base

class ReleaseBase(BaseModel):
    title: str
    releaseType: str
    year: int
    genre: str
    artist_id:int
    label_id:int

class ReleaseCreate(ReleaseBase):
    artist_id:int
    label_id:int

class Release(ReleaseBase):
    id: int

    class Config:
        orm_mode = True

class ArtistBase(BaseModel):
    artistName: str
    country: str

class ArtistCreate(ArtistBase):
    pass

class Artist(ArtistBase):
    id: int
    releases: List[Release] = []

    class Config:
        orm_mode = True

class LabelBase(BaseModel):
    labelName: str

class LabelCreate(LabelBase):
    pass

class Label(LabelBase):
    id: int
    releases: List[Release] = []

    class Config:
        orm_mode = True