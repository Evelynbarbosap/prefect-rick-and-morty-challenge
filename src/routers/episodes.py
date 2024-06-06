import json

from db.database import get_db
from fastapi import APIRouter, Depends
from models import Episode
from schemas.episode import EpisodeCreate
from sqlalchemy.orm import Session
from validators.episodes.validator import ValidatorEpisode

router = APIRouter(tags=["Episodes"])


@router.post("/episodes/")
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


@router.get("/episodes/{episode_id}")
def read_episode(episode_id: int, db: Session = Depends(get_db)):
    episode = db.query(Episode).filter(Episode.id == episode_id).first()
    ValidatorEpisode.validate_not_episode(episode=episode)

    return episode
