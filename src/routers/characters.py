import json

from db.database import get_db
from fastapi import Depends, APIRouter
from models.characters import Character
from schemas.character import CharacterCreate, CharacterUpdate
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


@router.put("/characters/{character_id}")
def update_character(character_id: int, character: CharacterUpdate,
                     db: Session = Depends(get_db)):
    db_character = db.query(Character).filter(
        Character.id == character_id).first()

    ValidatorCharacter.validate_not_character(character=character)

    for key, value in character.dict(exclude_unset=True).items():
        if key == 'episode':
            db_character.set_episode(value)
        else:
            setattr(db_character, key, value)

    db.commit()
    db.refresh(db_character)

    return db_character


@router.delete("/characters/{character_id}", response_model=dict)
def delete_character(character_id: int, db: Session = Depends(get_db)):
    db_character = db.query(Character).filter(
        Character.id == character_id).first()

    ValidatorCharacter.validate_not_character(character=db_character)

    db.delete(db_character)
    db.commit()

    return {"message": "Character deleted successfully"}
