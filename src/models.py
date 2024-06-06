import json
from sqlalchemy import Column, Integer, Text, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


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
