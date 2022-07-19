from typing import List
from pydantic import BaseModel
from ..database import Base
from . import Release

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