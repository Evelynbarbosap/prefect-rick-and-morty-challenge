import json

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from models import Character, Episode
from schemas.character import CharacterCreate
from schemas.episode import EpisodeCreate
from validators.characters.validator import ValidatorCharacter
from validators.episodes.validator import ValidatorEpisode

app = FastAPI()


@app.post("/characters/")
def create_character(character_data: CharacterCreate,
                     db: Session = Depends(get_db)):
    character = Character(
        name=character_data.name,
        status=character_data.status,
        species=character_data.species,
        type=character_data.type,
        gender=character_data.gender,
        origin=character_data.origin,
        location=character_data.location,
        image=character_data.image,
        episode=json.dumps(character_data.episode),
        url=character_data.url,
        created=character_data.created
    )

    db.add(character)
    db.commit()
    db.refresh(character)
    db.add(character)
    db.commit()
    db.refresh(character)

    return character


@app.get("/characters/{character_id}")
def read_character(character_id: int, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    ValidatorCharacter.validate_not_character(character=character)

    return character


@app.post("/episodes/")
def create_episode(episode_data: EpisodeCreate, db: Session = Depends(get_db)):
    episode = Episode(
        name=episode_data.name,
        air_date=episode_data.air_date,
        episode=episode_data.episode,
        characters=json.dumps(episode_data.characters),
        url=episode_data.url,
        created=episode_data.created
    )

    db.add(episode)
    db.commit()
    db.refresh(episode)

    return episode


@app.get("/episodes/{episode_id}")
def read_episode(episode_id: int, db: Session = Depends(get_db)):
    episode = db.query(Episode).filter(Episode.id == episode_id).first()
    ValidatorEpisode.validate_not_episode(episode=episode)

    return episode
