from sqlalchemy import create_engine, Column, Integer, JSON, Base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///rickandmorty.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON)

class Episode(Base):
    __tablename__ = "episodes"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON)

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)
