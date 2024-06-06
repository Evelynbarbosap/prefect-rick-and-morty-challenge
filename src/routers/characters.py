import json

from db.database import get_db
from fastapi import Depends, APIRouter
from models.characters import Character
from schemas.character import CharacterCreate
from sqlalchemy.orm import Session
from validators.characters.validator import ValidatorCharacter

router = APIRouter(tags=["Character"])


@router.post("/characters/")
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


@router.get("/characters/{character_id}")
def read_character(character_id: int, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    ValidatorCharacter.validate_not_character(character=character)

    return character


@router.get("/characters")
def get_characters(db: Session = Depends(get_db)):
    characters = db.query(Character).all()

    return characters
