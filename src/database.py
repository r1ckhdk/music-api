from enum import auto
import sqlalchemy as sql
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as declarative

SQLALCHEMY_DATABASE_URL = "sqlite:///./src/database.db"

engine = sql.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative.declarative_base()