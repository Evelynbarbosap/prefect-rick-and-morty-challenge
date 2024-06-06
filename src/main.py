from prefect import task
import requests
import logging

URL_API = "https://rickandmortyapi.com/api"

@task(max_retries=3, retry_delay_seconds=5)
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


@task(max_retries=3, retry_delay_seconds=5)
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
