import json

from sqlalchemy import Column, Integer, Text, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


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
