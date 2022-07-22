from .database import Base, engine, SessionLocal
from . import models, schemas
import sqlalchemy.orm as orm

def create_database():
    return Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_artist(db: orm.Session, artist: schemas.ArtistCreate):
    db_artist = models.Artist(artistName=artist.artistName, country=artist.country)
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

def get_artists(db: orm.Session, skip:int=0):
    return db.query(models.Artist).offset(skip).all()

def get_artist_id(db: orm.Session, artist_id: int):
    return db.query(models.Artist).filter(models.Artist.id == artist_id).first()

def delete_artist(db:orm.Session, artist_id: int):
    db_artist = db.query(models.Artist).filter(models.Artist.id == artist_id).delete()
    if db_artist is None:
        response = {"msg": "this artist does not exist"}
    else:
        db.commit()
        response = {"msg": "the artist was deleted"}
    return response

def create_release(db: orm.Session, release: schemas.ReleaseCreate):
    db_release = models.Release(
        title=release.title,
        releaseType=release.releaseType,
        year=release.year,
        genre=release.genre,
        artist_id=release.artist_id,
        label_id=release.label_id)

    db.add(db_release)
    db.commit()
    db.refresh(db_release)
    return db_release

def get_releases(db:orm.Session, skip: int=0):
    return db.query(models.Release).offset(skip).all()

def get_labels(db:orm.Session, skip: int=0):
    return db.query(models.Label).offset(skip).all()

def create_label(db:orm.Session, label:schemas.LabelCreate):
    db_label = models.Label(name=label.labelName)
    db.add(db_label)
    db.commit()
    db.refresh(db_label)
    return db_label