import json

from sqlalchemy import create_engine, Column, Integer, Text, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///rickandmorty.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(String)
    species = Column(String)
    type = Column(String)
    gender = Column(String)
    origin = Column(JSON)
    location = Column(JSON)
    image = Column(String)
    episode = Column(Text)
    url = Column(String)
    created = Column(String)

    def set_episode(self, episode):
        self.episode = json.dumps(episode)

    def get_episode(self):
        return json.loads(self.episode) if self.episode else []


class Episode(Base):
    __tablename__ = "episodes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    air_date = Column(String)
    episode = Column(String)
    characters = Column(Text)
    url = Column(String)
    created = Column(String)

    def set_characters(self, characters):
        self.characters = json.dumps(characters)

    def get_characters(self):
        return json.loads(self.characters) if self.characters else []


# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)
