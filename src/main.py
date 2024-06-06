import json
import logging
from datetime import timedelta

import requests
from prefect import task, Flow
from sqlalchemy.orm import sessionmaker

from models.characters import Character
from models.episodes import Episode
from db.database import engine

URL_API = "https://rickandmortyapi.com/api"


@task(max_retries=3, retry_delay=timedelta(seconds=5))
def get_rick_and_morty_characters():
    """
        Retorna todos os personagens. 
        Em caso de falha a task será reexecutada por mais 3 vezes com delay de 5s em cada tentativa.
    """

    try:
        response = requests.get(f"{URL_API}/character")
        response.raise_for_status()
        response_json = response.json()

        return response_json

    except requests.exceptions.RequestException as e:
        logging.info(f"Error: {e}")
        raise


@task(max_retries=3, retry_delay=timedelta(seconds=5))
def get_rick_and_morty_episodes():
    """
        Retorna todos os epsódios. 
        Em caso de falha a task será reexecutada por mais 3 vezes com delay de 5s em cada tentativa.
    """

    try:
        response = requests.get(f"{URL_API}/episode")
        response.raise_for_status()
        response_json = response.json()

        return response_json

    except requests.exceptions.RequestException as e:
        logging.info(f"Error: {e}")
        raise


@task
def save_data(characters, episodes):
    logging.info("Characters:", characters)
    logging.info("Episodes:", episodes)

    Session = sessionmaker(bind=engine)
    session = Session()
    for character in characters['results']:
        db_character = Character(
            id=character['id'],
            name=character['name'],
            status=character['status'],
            species=character['species'],
            type=character['type'],
            gender=character['gender'],
            origin=character['origin'],
            location=character['location'],
            image=character['image'],
            episode=json.dumps(character['episode']),
            url=character['url'],
            created=character['created']
        )
        session.merge(db_character)

    for episode in episodes['results']:
        db_episode = Episode(
            id=episode['id'],
            name=episode['name'],
            air_date=episode['air_date'],
            episode=episode['episode'],
            characters=json.dumps(episode['characters']),
            url=episode['url'],
            created=episode['created']
        )
        session.merge(db_episode)

    session.commit()
    session.close()


with Flow("Rick and Morty Data Pipeline") as flow:
    characters = get_rick_and_morty_characters()
    episodes = get_rick_and_morty_episodes()

    save_data(characters, episodes)

if __name__ == "__main__":
    flow.run()
