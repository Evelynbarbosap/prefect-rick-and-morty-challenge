from pydantic import BaseModel, Field


class CharacterCreate(BaseModel):
    name: str = Field(..., title="Name")
    status: str = Field(..., title="Status")
    species: str = Field(..., title="Species")
    type: str = Field(..., title="Type")
    gender: str = Field(..., title="Gender")
    origin: dict = Field(..., title="Origin")
    location: dict = Field(..., title="Location")
    image: str = Field(..., title="Image")
    episode: list = Field(..., title="Episode")
    url: str = Field(..., title="URL")
    created: str = Field(..., title="Created")

    class Config:
        schema_extra = {
                "example": {
                    "name": "Flower Morty",
                    "status": "Alive",
                    "species": "Human",
                    "type": "Human with a flower in his head",
                    "gender": "Male",
                    "origin": {
                        "name": "unknown",
                        "url": ""
                    },
                    "location": {
                        "name": "Citadel of Ricks",
                        "url": "https://rickandmortyapi.com/api/location/3"
                    },
                    "image": "https://rickandmortyapi.com/api/character/avatar/476.jpeg",
                    "episode": [
                        "https://rickandmortyapi.com/api/episode/28"
                    ],
                    "url": "https://rickandmortyapi.com/api/character/476",
                    "created": "2018-05-22T17:18:46.129Z"
                 }
        }