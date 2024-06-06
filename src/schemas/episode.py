from pydantic import BaseModel, Field


class EpisodeCreate(BaseModel):
    name: str = Field(..., title="Name")
    air_date: str = Field(..., title="Air date")
    episode: str = Field(..., title="Epsode")
    characters: list = Field(..., title="Characters")
    url: str = Field(..., title="URL")
    created: str = Field(..., title="Created")

    class Config:
        schema_extra = {
            "example": {
                "name": "Pilot",
                "air_date": "December 2, 2013",
                "episode": "S01E01",
                "characters": [
                    "https://rickandmortyapi.com/api/character/1",
                    "https://rickandmortyapi.com/api/character/2"
                ],
                "url": "https://rickandmortyapi.com/api/episode/1",
                "created": "2017-11-10T12:56:33.798Z"
            }
        }


class EpisodeUpdate(BaseModel):
    name: str = Field(..., title="Name")
    air_date: str = Field(..., title="Air date")
    episode: str = Field(..., title="Epsode")
    characters: list = Field(..., title="Characters")
    url: str = Field(..., title="URL")

    class Config:
        schema_extra = {
            "example": {
                "name": "Pilot",
                "air_date": "December 2, 2013",
                "episode": "S01E01",
                "characters": [
                    "https://rickandmortyapi.com/api/character/1",
                    "https://rickandmortyapi.com/api/character/2"
                ],
                "url": "https://rickandmortyapi.com/api/episode/1"
            }
        }
