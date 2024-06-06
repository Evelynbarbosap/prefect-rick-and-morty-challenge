import json

from db.database import get_db
from fastapi import APIRouter, Depends
from models.episodes import Episode
from schemas.episode import EpisodeCreate, EpisodeUpdate
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


@router.get("/episodes")
def get_episodes(db: Session = Depends(get_db)):
    episodes = db.query(Episode).all()

    return episodes


@router.put("/episodes/{episode_id}")
def update_episode(episode_id: int, episode: EpisodeUpdate,
                   db: Session = Depends(get_db)):
    db_episode = db.query(Episode).filter(
        Episode.id == episode_id).first()

    ValidatorEpisode.validate_not_episode(episode=db_episode)

    for key, value in episode.dict(exclude_unset=True).items():
        if key == 'characters':
            db_episode.set_episode(value)
        else:
            setattr(db_episode, key, value)

    db.commit()
    db.refresh(db_episode)

    return db_episode


@router.delete("/episodes/{episode_id}", response_model=dict)
def delete_episode(episode_id: int, db: Session = Depends(get_db)):
    db_episode = db.query(Episode).filter(
        Episode.id == episode_id).first()

    ValidatorEpisode.validate_not_episode(episode=db_episode)

    db.delete(db_episode)
    db.commit()

    return {"message": "Episode deleted successfully"}
