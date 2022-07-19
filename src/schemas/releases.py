from typing import List
from pydantic import BaseModel
from ..database import Base

class ReleaseBase(BaseModel):
    title: str
    releaseType: str
    year: int
    genre: str
    artist_id:int

class ReleaseCreate(ReleaseBase):
    artist_id:int

class Release(ReleaseBase):
    id: int

    class Config:
        orm_mode = True