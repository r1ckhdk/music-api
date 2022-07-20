from typing import List
from fastapi import FastAPI
import fastapi
import sqlalchemy.orm as orm
from . import services, schemas

app = FastAPI()
services.create_database()


@app.post("/artists/", response_model=schemas.Artist)
def create_artist(
    artist: schemas.ArtistCreate,
    db: orm.Session = fastapi.Depends(services.get_db)
):
    return services.create_artist(db=db, artist=artist)


@app.get("/artists/", response_model=List[schemas.Artist])
def read_artists(skip: int=0, db: orm.Session=fastapi.Depends(services.get_db)):
    artists = services.get_artists(db=db)
    return artists


@app.get("/artists/{artist_id}",response_model=schemas.Artist)
def read_artist(artist_id: int, db: orm.Session=fastapi.Depends(services.get_db)):
    db_artist = services.get_artist_id(db=db, artist_id=artist_id)
    if db_artist is None:
        raise fastapi.HTTPException(
            status=404, detail="this artist does not exist"
        )
    return db_artist

@app.delete("/artists/{artist_id}")
def delete_artist(artist_id: int, db: orm.Session=fastapi.Depends(services.get_db)):
    response = services.delete_artist(db=db, artist_id=artist_id)
    return response

@app.post("/releases/")
def create_release(release: schemas.ReleaseCreate, db: orm.Session=fastapi.Depends(services.get_db)):
    return services.create_release(db=db, release=release)

@app.get("/releases/")
def get_releases(skip: int=0, db: orm.Session=fastapi.Depends(services.get_db)):
    return services.get_releases(db=db)